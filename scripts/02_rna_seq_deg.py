import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def simulate_and_analyze_deg():
    print("[*] Generando matriz ligera de expresión de genes (Simulación RNA-Seq control vs tumor)...")
    
    # Fijar semilla para reproducibilidad
    np.random.seed(42)
    
    # Simular 500 genes y 20 muestras (10 controles, 10 tumores)
    n_genes = 500
    gene_names = [f"GENE_{i:03d}" for i in range(1, n_genes + 1)]
    
    samples_control = [f"Control_{i}" for i in range(1, 11)]
    samples_tumor = [f"Tumor_{i}" for i in range(1, 11)]
    all_samples = samples_control + samples_tumor
    
    # Matriz de expresión base (valores en escala log2)
    base_expression = np.random.normal(5, 2, size=(n_genes, len(all_samples)))
    
    # Introducir sobreexpresión y subexpresión artificial
    base_expression[10:25, 10:] += np.random.uniform(2, 4, size=(15, 10))
    base_expression[50:65, 10:] -= np.random.uniform(2, 4, size=(15, 10))
    
    df_expression = pd.DataFrame(base_expression, index=gene_names, columns=all_samples)
    print(f"[+] Matriz creada: {df_expression.shape[0]} genes, {df_expression.shape[1]} muestras.")
    
    # Calcular Fold Change y valor p (Prueba t de Student)
    results = []
    for gene in gene_names:
        ctrl_vals = df_expression.loc[gene, samples_control]
        tumor_vals = df_expression.loc[gene, samples_tumor]
        
        mean_ctrl = np.mean(ctrl_vals)
        mean_tumor = np.mean(tumor_vals)
        
        log2_fc = mean_tumor - mean_ctrl
        t_stat, p_val = stats.ttest_ind(tumor_vals, ctrl_vals)
        p_val = max(p_val, 1e-300)
        
        results.append({
            'gene': gene,
            'log2_fold_change': log2_fc,
            'p_value': p_val,
            'neg_log10_p': -np.log10(p_val)
        })
        
    df_results = pd.DataFrame(results)
    
    output_csv = "data/raw/deg_results_sample.csv"
    df_results.to_csv(output_csv, index=False)
    print(f"[+] Resultados de expresión diferencial guardados en: {output_csv}")
    
    # Generar Volcano Plot
    print("[*] Generando gráfico Volcano Plot...")
    plt.figure(figsize=(8, 6))
    
    significant = (df_results['p_value'] < 0.05) & (abs(df_results['log2_fold_change']) > 1.5)
    
    plt.scatter(df_results.loc[~significant, 'log2_fold_change'], 
                df_results.loc[~significant, 'neg_log10_p'], 
                color='gray', alpha=0.5, label='No significativo')
                
    plt.scatter(df_results.loc[significant, 'log2_fold_change'], 
                df_results.loc[significant, 'neg_log10_p'], 
                color='crimson', alpha=0.8, label='DEG Significativo')
                
    plt.axhline(y=-np.log10(0.05), color='black', linestyle='--', linewidth=0.8, label='p = 0.05')
    plt.axvline(x=1.5, color='blue', linestyle='--', linewidth=0.8, label='|Log2FC| > 1.5')
    plt.axvline(x=-1.5, color='blue', linestyle='--', linewidth=0.8)
    
    plt.title("Volcano Plot - Expresión Diferencial (Cáncer vs Control)", fontsize=12)
    plt.xlabel("Log2 Fold Change (Tumor / Control)", fontsize=10)
    plt.ylabel("-Log10(p-value)", fontsize=10)
    plt.legend(loc='upper right', fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plot_path = "data/raw/volcano_plot.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"[+] Gráfica guardada exitosamente en: {plot_path}")
    plt.close()

if __name__ == "__main__":
    simulate_and_analyze_deg()

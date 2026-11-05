import pandas as pd
import numpy as np
import os

def simulate_and_filter_vcf():
    print("[*] Iniciando módulo de análisis de variantes somáticas (DNA-Seq / VCF)...")
    
    # 1. Simular un archivo VCF en miniatura (normalmente leído con bcftools o pysam)
    np.random.seed(101)
    n_variants = 100
    
    chromosomes = [f"chr{i}" for i in range(1, 23)] + ["chrX"]
    data = {
        'CHROM': np.random.choice(chromosomes, n_variants),
        'POS': np.random.randint(100000, 150000000, n_variants),
        'REF': np.random.choice(['A', 'C', 'G', 'T'], n_variants),
        'ALT': np.random.choice(['A', 'C', 'G', 'T'], n_variants),
        'QUAL': np.random.uniform(10, 99, n_variants),
        'DP': np.random.randint(10, 200, n_variants),  # Profundidad de lectura
        'VAF': np.random.uniform(0.05, 0.95, n_variants) # Frecuencia alélica tumoral
    }
    
    df_vcf = pd.DataFrame(data)
    # Evitar REF == ALT por realismo biológico
    df_vcf = df_vcf[df_vcf['REF'] != df_vcf['ALT']].copy()
    
    print(f"[+] Archivo VCF simulado cargado: {len(df_vcf)} variantes crudas detectadas.")
    
    # 2. Aplicar filtros de calidad estándar de GitHub (Pipeline de filtrado somático)
    # Criterio: Calidad de variante > 30, Profundidad de lectura (DP) > 30, VAF > 0.15
    filtered_vcf = df_vcf[
        (df_vcf['QUAL'] > 30.0) & 
        (df_vcf['DP'] > 30) & 
        (df_vcf['VAF'] > 0.15)
    ].copy()
    
    print(f"[+] Filtrado aplicado: {len(filtered_vcf)} variantes somáticas de alta confianza retenidas.")
    
    # 3. Clasificar mutaciones por tipo de impacto simulado
    def classify_impact(row):
        if row['VAF'] > 0.6:
            return "Alta (Clonal / Loss of Heterozygosity)"
        elif row['VAF'] > 0.3:
            return "Moderada (Subclonal)"
        else:
            return "Baja (Pasajera / Passenger)"
            
    filtered_vcf['Predicted_Impact'] = filtered_vcf.apply(classify_impact, axis=1)
    
    # 4. Guardar resultados limpios
    os.makedirs("data/raw", exist_ok=True)
    output_path = "data/raw/filtered_somatic_variants.csv"
    filtered_vcf.to_csv(output_path, index=False)
    
    print(f"[+] Reporte de variantes somáticas guardado en: {output_path}")
    print("\nResumen de variantes filtradas por impacto:")
    print(filtered_vcf['Predicted_Impact'].value_counts())

if __name__ == "__main__":
    simulate_and_filter_vcf()

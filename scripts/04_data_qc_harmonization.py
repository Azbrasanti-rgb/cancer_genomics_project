import pandas as pd
import os

def harmonize_clinical_data():
    print("[*] Iniciando el Módulo de Control de Calidad y Armonización de Datos...")
    
    input_path = "data/raw/brca_tcga_clinical_sample.csv"
    
    if not os.path.exists(input_path):
        print(f"[-] No se encontró el archivo clínico en {input_path}. Ejecuta primero el Módulo 1.")
        return
        
    # 1. Cargar datos crudos
    df = pd.read_csv(input_path)
    print(f"[+] Datos clínicos cargados. Dimensiones originales: {df.shape}")
    
    # 2. Análisis de Calidad Inicial (QC Report)
    print("\n--- REPORTE DE CALIDAD (QC) INICIAL ---")
    print(f"Valores nulos totales detectados: {df.isna().sum().sum()}")
    print("Primeras columnas disponibles:", list(df.columns[:5]))
    
    # 3. Limpieza y Armonización
    # Eliminar filas completamente vacías o duplicados exactos
    df_clean = df.drop_duplicates().dropna(how='all').copy()
    
    # Normalizar texto en columnas de texto si existen (ej. estandarizar a minúsculas o limpiar espacios)
    for col in df_clean.select_dtypes(include=['object']).columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()
        
    # Filtrar registros inválidos simulados o vacíos ('nan', 'None')
    if 'value' in df_clean.columns:
        df_clean = df_clean[df_clean['value'].notna() & (df_clean['value'] != 'nan')]
        
    print(f"\n[+] Dimensiones después de la limpieza y QC: {df_clean.shape}")
    
    # 4. Guardar dataset armonizado listo para análisis avanzados
    os.makedirs("data/processed", exist_ok=True)
    output_csv = "data/processed/harmonized_clinical_data.csv"
    df_clean.to_csv(output_csv, index=False)
    
    print(f"[+] ¡Datos armonizados guardados exitosamente en: {output_csv}!")

if __name__ == "__main__":
    harmonize_clinical_data()

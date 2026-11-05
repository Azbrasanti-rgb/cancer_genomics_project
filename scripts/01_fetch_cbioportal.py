import requests
import pandas as pd

BASE_URL = "https://www.cbioportal.org/api"

def test_api_connection():
    print("[*] Conectando a la API de cBioPortal...")
    url = f"{BASE_URL}/studies"
    response = requests.get(url)

    if response.status_code == 200:
        studies = response.json()
        print(f"[+] ¡Conexión exitosa! Se encontraron {len(studies)} estudios disponibles en total.")
        df_studies = pd.DataFrame(studies)
        print("\nEjemplos de estudios oncológicos disponibles:")
        print(df_studies[['studyId', 'name', 'cancerTypeId']].head(5))
    else:
        print(f"[-] Error en la conexión: {response.status_code}")

def fetch_lightweight_clinical_data(study_id="brca_tcga"):
    print(f"\n[*] Descargando datos clínicos ligeros para el estudio: {study_id}...")
    url = f"{BASE_URL}/studies/{study_id}/clinical-data?projection=SUMMARY"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df_clinical = pd.DataFrame(data)

        output_path = f"data/raw/{study_id}_clinical_sample.csv"
        df_clinical.to_csv(output_path, index=False)
        print(f"[+] Datos guardados exitosamente en: {output_path}")
        print(f"[+] Dimensiones de la tabla clínica: {df_clinical.shape[0]} filas, {df_clinical.shape[1]} columnas.")
        print("\nVista previa de los datos clínicos:")
        print(df_clinical.head(3))
    else:
        print(f"[-] Error al obtener datos clínicos: {response.status_code}")

if __name__ == "__main__":
    test_api_connection()
    fetch_lightweight_clinical_data("brca_tcga")

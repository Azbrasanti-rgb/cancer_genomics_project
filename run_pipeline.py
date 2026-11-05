import subprocess
import sys
import os

def run_step(script_name):
    print(type(f"\n=================================================="))
    print(f"[*] Ejecutando: {script_name}...")
    print(f"==================================================")

    # Usar el intérprete de Python del entorno virtual actual
    python_executable = sys.executable
    result = subprocess.run([python_executable, script_name])

    if result.returncode != 0:
        print(f"[-] Error crítico al ejecutar {script_name}. Abortando pipeline.")
        sys.exit(1)
    else:
        print(f"[+] ¡{script_name} finalizado con éxito!\n")

def main():
    print("[*] Iniciando Pipeline Completo de Genómica del Cáncer (Lightweight)...")

    # Crear carpetas requeridas si no existen
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Ejecutar secuencialmente los módulos
    run_step("scripts/01_fetch_cbioportal.py")
    run_step("scripts/02_rna_seq_deg.py")
    run_step("scripts/03_somatic_variants.py")
    run_step("scripts/04_data_qc_harmonization.py")

    print("==================================================")
    print("[+] ¡PIPELINE EJECUTADO DE EXCELENTE MANERA!")
    print("[+] Todos los datos y gráficos procesados están listos en data/raw/ y data/processed/")
    print("==================================================")

if __name__ == "__main__":
    main()

## 💡 De la Biotecnología a la Bioinformática: Aprendizaje Autónomo y Ética Tecnológica

Iniciar en la bioinformática partiendo de bases universitarias tradicionales puede ser un desafío. Mi experiencia previa abarcaba desde simulaciones de acoplamiento molecular (*docking* uniendo proteínas y ligandos) hasta la investigación documental en PubMed y NCBI. Sin embargo, dar el salto hacia la informática avanzada como biotecnólogo es un paso tan complejo como necesario en la actualidad científica.

Hoy en día, el panorama laboral para los científicos es más competitivo, y uno de los mayores retos es la irrupción de la Inteligencia Artificial. Aprender a dominar la computación es vital no solo para adquirir experiencia, sino para entender cómo utilizar la IA de forma ética: diseñándola como una herramienta de apoyo y optimización —para perfeccionar código en Python o acortar tiempos de investigación— sin perder de vista que el investigador principal siempre debe ser el criterio humano. 

Este proyecto marca ese punto de inflexión en mi carrera. Es una demostración de cómo el uso responsable de la tecnología permite asimilar conceptos avanzados de forma autónoma.

### 🔬 Sobre este Proyecto (Pipeline Bioinformático)
Este repositorio implementa un flujo automatizado (*pipeline*) ligero y reproducible para el análisis de genómica del cáncer en computadoras con arquitectura Apple Silicon (M1/M2/M3), estructurado en los siguientes módulos:

1. **Adquisición y Análisis Clínico (Módulos 1 y 4):** Conexión automatizada a la API de cBioPortal para extraer metadatos de pacientes con cáncer de mama (estudio TCGA-BRCA, 18,488 registros), aplicando control de calidad y armonización tabular.
2. **Transcriptómica y Expresión Diferencial (Módulo 2):** Simulación de matrices de expresión de ARN-Seq y generación de un *Volcano Plot* para identificar genes estadísticamente significativos (oncogenes candidatos) entre tejido tumoral y control.
3. **Genómica de ADN y Variantes Somáticas (Módulo 3):** Simulación y filtrado riguroso de variantes en formato VCF basadas en métricas de calidad de secuenciación (`QUAL`, profundidad `DP` y frecuencia alélica `VAF`), aislando mutaciones clonales de alto impacto.
4. **Reproducibilidad y Orquestación (Módulos 5 y 6):** Automatización completa del flujo mediante un script maestro (`run_pipeline.py`) y control de versiones profesional en Git/GitHub.

## 💡 From Biotechnology to Bioinformatics: Autonomous Learning and Technological Ethics

Getting started in bioinformatics starting from traditional university fundamentals can be challenging. My previous experience ranged from molecular docking simulations (binding proteins and ligands) to literature reviews using PubMed and NCBI. However, bridging the gap toward advanced computing as a biotechnologist is both a complex and necessary step in modern science.

Today, the job market for scientists is increasingly competitive, and one of the greatest challenges is the rise of Artificial Intelligence. Learning to master computer science is vital not only to build experience, but also to understand how to use AI ethically: treating it as a supporting tool and optimization helper—to refine Python code or shorten research timelines—while ensuring that human critical thinking remains at the core of discovery.

This project marks that turning point in my career. It demonstrates how the responsible use of technology enables us to master advanced concepts autonomously.

### 🔬 About this Project (Bioinformatics Pipeline)
This repository implements a lightweight, reproducible automated pipeline for cancer genomics analysis optimized for Apple Silicon architectures (M1/M2/M3), structured into the following modules:

1. **Clinical Data Acquisition & Processing (Modules 1 & 4):** Automated connection to the cBioPortal API to extract breast cancer patient metadata (TCGA-BRCA study, 18,488 records), followed by rigorous data quality control (QC) and tabular harmonization.
2. **Transcriptomics & Differential Expression (Module 2):** Simulation of RNA-Seq expression matrices and generation of a *Volcano Plot* to identify statistically significant genes (candidate oncogenes) between tumor and control tissues.
3. **DNA Genomics & Somatic Variants (Module 3):** Simulation and stringent filtering of VCF variants based on sequencing quality metrics (`QUAL`, read depth `DP`, and allele frequency `VAF`), isolating high-impact clonal mutations.
4. **Reproducibility & Orchestration (Modules 5 & 6):** Complete automation of the end-to-end workflow using a master orchestrator script (`run_pipeline.py`) backed by professional Git/GitHub version control.

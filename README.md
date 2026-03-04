# Artificial Intelligence and Open Science in Research Software Engineering

![CI](https://github.com/asquillari/Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/actions/workflows/ci.yml/badge.svg)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18827695.svg)](https://doi.org/10.5281/zenodo.18827695)

---

# 📖 Descripción

Este proyecto implementa un **pipeline reproducible para analizar artículos científicos** utilizando herramientas de **Inteligencia Artificial y prácticas de Ciencia Abierta**.

El sistema descarga artículos de **arXiv**, extrae información estructurada utilizando **Grobid** y genera distintos análisis automáticos.

El objetivo es demostrar un flujo de trabajo reproducible que combine:

- Inteligencia artificial
- Automatización
- Contenedores Docker
- Integración continua
- Publicación abierta del software

---

## 📂 Estructura del proyecto

```

├── .github/workflows/
│   └── ci.yml                # Pipeline de integración continua (GitHub Actions)
│
├── data/
│   ├── pdfs/                 # PDFs descargados desde arXiv
│   ├── tei/                  # XML generados por Grobid
│   └── papers.csv            # Lista de papers a descargar
│
├── outputs/                  # Resultados del análisis
│   ├── abstract_keywords_top50.txt
│   ├── figures_per_paper.png
│   ├── links_per_paper.txt
│   └── wordcloud_abstracts.png
│
├── src/                      # Scripts del pipeline
│   ├── download_pdfs.py
│   ├── run_grobid.py
│   ├── wait_grobid.py
│   ├── wordcloud_abstracts.py
│   ├── count_figures.py
│   └── extract_links.py
│
├── tests/                    # Tests automáticos con pytest
│
├── Dockerfile                # Imagen Docker del pipeline
├── docker-compose.yml        # Orquestación de servicios (pipeline + Grobid)
├── requirements.txt          # Dependencias Python
├── LICENSE                   # Licencia del proyecto
└── README.md
```

---

## 🔄 Pipeline de procesamiento

El pipeline del proyecto sigue los siguientes pasos:
```
papers.csv
     │
     ▼
download_pdfs.py
     │
     ▼
PDFs
     │
     ▼
Grobid (Docker container)
     │
     ▼
TEI XML
     │
     ├── wordcloud_abstracts.py
     ├── count_figures.py
     └── extract_links.py
            │
            ▼
        outputs/
```

---

# ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/asquillari/Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering.git
cd Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

# 🐳 Ejecución con Docker 

El pipeline completo puede ejecutarse usando **Docker Compose**, lo que garantiza reproducibilidad.

```bash
docker compose up --build
```

Esto levanta automáticamente:

- Grobid
- El pipeline de procesamiento

---

# ▶️ Ejecución manual del pipeline

También puede ejecutarse paso a paso:

```bash
python src/download_pdfs.py
python src/wait_grobid.py
python src/run_grobid.py
python src/wordcloud_abstracts.py
python src/count_figures.py
python src/extract_links.py
```

---

# 🧪 Tests

El proyecto incluye tests automatizados utilizando **pytest**.

Ejecutar:

```bash
pytest
```

---

# 🔁 Integración Continua

Este repositorio utiliza **GitHub Actions** para:

- Ejecutar el pipeline automáticamente
- Correr los tests
- Verificar que el proyecto sea reproducible

Cada push o pull request dispara el workflow de CI.

---

# 📊 Resultados generados

El pipeline produce distintos outputs:

- **Wordcloud de abstracts**
- **Conteo de figuras en papers**
- **Extracción de links**
- **Archivos TEI XML generados por Grobid**

Los resultados se guardan en:

```
outputs/
```

y

```
data/tei/
```

---

# 📦 Dataset

Los artículos analizados se descargan automáticamente desde **arXiv** en formato PDF.

---

# 🔬 Reproducibilidad

Este proyecto sigue principios de **Open Science**:

- Código abierto
- Pipeline automatizado
- Entorno reproducible con Docker
- Tests automatizados
- Integración continua

---

# 📑 DOI del proyecto

El proyecto está archivado en **Zenodo**, lo que permite citarlo como software científico.

DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18827695.svg)](https://doi.org/10.5281/zenodo.18827695)

---

## 📚 Cómo citar este software

Si utilizas este proyecto en investigación o docencia, puedes citarlo usando el DOI generado por Zenodo:

```
@software{asquillari_ai_open_science_pipeline,
  author = {Asquillari},
  title = {Artificial Intelligence and Open Science in Research Software Engineering},
  year = {2026},
  doi = {10.5281/zenodo.18827695},
  url = {https://doi.org/10.5281/zenodo.18827695}
}
````

---

# 📜 Licencia

MIT License
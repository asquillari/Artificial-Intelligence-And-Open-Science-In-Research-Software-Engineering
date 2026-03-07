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
## 📂 Estructura del proyecto
- **src/download_pdfs.py**  
  Descarga los PDFs de artículos científicos desde arXiv usando las URLs definidas en `data/papers.csv` y los guarda en `data/pdfs/`.

- **src/wait_grobid.py**  
  Espera a que el servidor Grobid esté disponible antes de ejecutar el pipeline. Principalmente en Docker y CI para evitar errores de conexión.

- **src/run_grobid.py**  
  Envía los PDFs a **Grobid** para extraer información estructurada y genera archivos **TEI XML** en `data/tei/`.

- **src/wordcloud_abstracts.py**  
  Extrae los abstracts de los archivos TEI, limpia el texto y genera un **wordcloud** y un archivo con las **50 palabras más frecuentes**.

- **src/count_figures.py**  
  Analiza los archivos TEI y cuenta la cantidad de figuras en cada paper, generando un **gráfico de barras**.

- **src/extract_links.py**  
  Extrae los enlaces externos presentes en los artículos y guarda los resultados en `outputs/links_per_paper.txt`.

- **data/papers.csv**  
  Dataset de entrada con los artículos a analizar (`id`, `url`).

- **tests/**  
  Contiene los tests automatizados (datos, outputs, pipeline e integración) ejecutados con **pytest**.

- **Dockerfile**  
  Define el entorno reproducible del proyecto e instala las dependencias necesarias.

- **docker-compose.yml**  
  Permite ejecutar el pipeline completo junto con el servicio **Grobid** utilizando Docker.

- **.github/workflows/ci.yml**  
  Configuración de **GitHub Actions** que ejecuta el pipeline y los tests automáticamente en cada push o pull request.
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

# 🐳 Ejecución completa con Docker 

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

En una terminal:

```bash
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

Y en una segunda terminal:
```bash
python src/download_pdfs.py
python src/wait_grobid.py  
python src/run_grobid.py
python src/wordcloud_abstracts.py
python src/count_figures.py
python src/extract_links.py
```

---

## 🧪 Testing

El proyecto incluye un conjunto de **tests automatizados con pytest** para verificar que el pipeline funcione correctamente y que los datos generados tengan la estructura esperada.

Los tests están organizados en varias categorías:

### 1. Tests de datos (`test_data.py`)

Validan la integridad del dataset de entrada:

- Verifica que `data/papers.csv` exista.
- Comprueba que el CSV tenga las columnas requeridas (`id`, `url`).
- Verifica que el archivo no esté vacío.
- Valida que las URLs tengan formato correcto de PDF de arXiv.

Estos tests aseguran que el pipeline tenga **datos de entrada válidos**.

---

### 2. Tests de outputs (`test_outputs.py`)

Validan los resultados generados por el pipeline:

- Existencia del **wordcloud de abstracts**.
- Existencia del **gráfico de figuras por paper**.
- Existencia del archivo de **links extraídos**.
- Verificación de que los archivos generados **no estén vacíos**.

Estos tests aseguran que el pipeline produce **resultados correctos**.

---

### 3. Tests del pipeline (`test_pipeline.py`)

Comprueban que los distintos pasos del pipeline se hayan ejecutado correctamente:

- Verifica que los **PDFs se hayan descargado**.
- Verifica que **Grobid haya generado los archivos TEI XML**.
- Comprueba que los **outputs finales existan**.

---

### 4. Tests de integración (`test_pipeline_integration.py`)

Estos tests verifican el funcionamiento **end-to-end del pipeline**.

Incluyen:

- Validación de PDFs descargados
- Validación de XML generados
- Verificación del pipeline completo

Estos tests se marcan como:
@pytest.mark.integration


y pueden ejecutarse por separado.

---

## ▶️ Ejecutar los tests

Ejecutar todos los tests:

```
pytest
```

Ejecutar solo tests rápidos (sin integración):
```
pytest -m "not integration"
```

Ejecutar solo tests de integración:
```
pytest -m "integration"
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

# 💬 Cita

Si usa este repositorio, porfavor citarlo de la siguiente manera:

Squillari, A. (2026). Artificial Intelligence and Open Science in Research Software Engineering (Version 1.0) [Computer software]. https://doi.org/10.5281/zenodo.18827695

La cita tambien se encuentra disponible en `CITATION.cff`.

---

# 📜 Licencia

MIT License
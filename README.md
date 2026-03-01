# 📄 Análisis de Papers con Grobid

## 📌 Descripción

Este proyecto analiza un conjunto de artículos científicos de acceso abierto utilizando **Grobid** para extraer información estructurada a partir de PDFs.

El pipeline procesa hasta 10 papers y genera:

* Una **nube de palabras (wordcloud)** a partir de los abstracts
* Un **gráfico del número de figuras por paper**
* Una **lista de enlaces externos encontrados en cada paper**

El proyecto sigue principios de **reproducibilidad** y **open science**.

---

## 📂 Estructura del proyecto

```id="x2n1c0"
.
├── data/
│   ├── papers.csv        # Lista de papers (URLs)
│   ├── pdfs/             # PDFs descargados (ignorados en git)
│   └── tei/              # XML generados por Grobid (ignorados en git)
├── src/
│   ├── 01_download_pdfs.py
│   ├── 02_run_grobid.py
│   ├── 03_extract_abstracts.py
│   ├── 04_wordcloud_abstracts.py
│   ├── 05_count_figures.py
│   └── 06_extract_links.py
├── outputs/
│   ├── wordcloud_abstracts.png
│   ├── abstract_keywords_top50.txt
│   ├── figures_per_paper.png
│   └── links_per_paper.txt
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.x
* Docker
* Grobid (ejecutado con Docker)

Instalar dependencias:

```bash id="3v1n9f"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar

### 1. Levantar Grobid (Docker)

```bash id="g4m1n2"
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

---

### 2. Descargar los PDFs

```bash id="h7k2p3"
python src/download_pdfs.py
```

---

### 3. Extraer XML (TEI) con Grobid

```bash id="j8l4q5"
python src/run_grobid.py
```

---

### 4. Generar resultados

#### Nube de palabras (abstracts)

```bash id="k9m5r6"
python src/wordcloud_abstracts.py
```

#### Figuras por paper

```bash id="l0n6s7"
python src/count_figures.py
```

#### Links por paper

```bash id="m1o7t8"
python src/extract_links.py
```

---

## 📊 Resultados

Los resultados se guardan en la carpeta `outputs/`:

* `wordcloud_abstracts.png` → nube de palabras
* `abstract_keywords_top50.txt` → palabras más frecuentes (validación)
* `figures_per_paper.png` → gráfico de figuras
* `links_per_paper.txt` → enlaces externos

---

## 🧠 Metodología

1. Se define el dataset en `papers.csv` (reproducible)
2. Se descargan los PDFs automáticamente
3. Se procesan con **Grobid**
4. Grobid genera XML estructurado (TEI)
5. Scripts en Python extraen:

   * Abstracts
   * Figuras
   * Links
6. Se generan visualizaciones y outputs

---

## ✅ Validación

* **Wordcloud**: validado con las 50 palabras más frecuentes extraídas de los abstracts
* **Figuras**: conteo de elementos `<figure>` en el XML TEI y verificación manual en algunos papers
* **Links**: extraídos de `<ref target="">` y filtrados para conservar solo enlaces externos (http/https), eliminando referencias internas (ej. `#fig1`, `#b12`)

---

## ♻️ Reproducibilidad

* Dataset definido en `papers.csv`
* Dependencias en `requirements.txt`
* Entorno virtual (`.venv`)
* Grobid ejecutado con Docker
* Resultados regenerables desde cero

---

## 📜 Licencia

MIT License

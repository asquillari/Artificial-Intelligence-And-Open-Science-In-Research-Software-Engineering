import os
import glob
import pytest
import csv

def test_papers_csv_has_required_columns():
    path = os.path.join("data", "papers.csv")
    assert os.path.exists(path), "Falta data/papers.csv"

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])
    assert {"id", "url"}.issubset(cols), f"Columnas esperadas: id,url. Columnas actuales: {sorted(cols)}"

def _has_pdfs():
    return len(glob.glob("data/pdfs/*.pdf")) > 0

def _has_tei():
    return len(glob.glob("data/tei/*.xml")) > 0

def _has_outputs():
    return (
        os.path.exists("outputs/wordcloud_abstracts.png")
        and os.path.exists("outputs/figures_per_paper.png")
        and os.path.exists("outputs/links_per_paper.txt")
    )

@pytest.mark.integration
def test_pdfs_exist():
    if not _has_pdfs():
        pytest.skip("No hay PDFs: ejecutar primero el pipeline (download_pdfs.py)")
    assert _has_pdfs()

@pytest.mark.integration
def test_tei_generated():
    if not _has_tei():
        pytest.skip("No hay TEI: ejecutar primero run_grobid.py")
    assert _has_tei()

@pytest.mark.integration
def test_outputs_exist():
    if not _has_outputs():
        pytest.skip("No hay outputs: ejecutar scripts de análisis primero")
    assert _has_outputs()

@pytest.mark.integration
def test_links_not_empty():
    path = "outputs/links_per_paper.txt"
    if not os.path.exists(path):
        pytest.skip("No existe links_per_paper.txt: ejecutar extract_links.py primero")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    assert len(content) > 0, "El archivo de links está vacío"
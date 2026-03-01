import os
import glob

def test_pdfs_exist():
    pdfs = glob.glob("data/pdfs/*.pdf")
    assert len(pdfs) > 0, "No hay PDFs descargados"

def test_tei_generated():
    tei_files = glob.glob("data/tei/*.xml")
    assert len(tei_files) > 0, "No se generaron archivos TEI"

def test_outputs_exist():
    assert os.path.exists("outputs/wordcloud_abstracts.png"), "Falta wordcloud"
    assert os.path.exists("outputs/figures_per_paper.png"), "Falta gráfico de figuras"
    assert os.path.exists("outputs/links_per_paper.txt"), "Falta archivo de links"

def test_links_not_empty():
    path = "outputs/links_per_paper.txt"
    assert os.path.exists(path), "No existe archivo de links"

    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert len(content) > 0, "El archivo de links está vacío"
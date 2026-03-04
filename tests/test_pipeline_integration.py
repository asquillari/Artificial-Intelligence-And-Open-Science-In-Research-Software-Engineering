import glob
import pytest


@pytest.mark.integration
def test_pdfs_downloaded():
    pdfs = glob.glob("data/pdfs/*.pdf")

    if len(pdfs) == 0:
        pytest.skip("Ejecutar download_pdfs.py primero")

    assert len(pdfs) > 0


@pytest.mark.integration
def test_tei_generated():
    tei = glob.glob("data/tei/*.xml")

    if len(tei) == 0:
        pytest.skip("Ejecutar run_grobid.py primero")

    assert len(tei) > 0
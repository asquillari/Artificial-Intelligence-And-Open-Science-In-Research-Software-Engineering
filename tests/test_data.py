import csv
import os
import re

ARXIV_RE = re.compile(r"https://arxiv.org/pdf/\d{4}\.\d{5}(v\d+)?\.pdf")

def test_papers_csv_exists():
    assert os.path.exists("data/papers.csv")


def test_papers_csv_has_required_columns():
    with open("data/papers.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])

    assert {"id", "url"}.issubset(cols)


def test_papers_csv_not_empty():
    with open("data/papers.csv", newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    assert len(reader) > 0


def test_urls_are_arxiv_pdfs():
    with open("data/papers.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            assert ARXIV_RE.match(row["url"])
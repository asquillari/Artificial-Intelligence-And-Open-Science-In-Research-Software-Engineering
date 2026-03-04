import os


def test_wordcloud_exists():
    assert os.path.exists("outputs/wordcloud_abstracts.png")


def test_figures_plot_exists():
    assert os.path.exists("outputs/figures_per_paper.png")


def test_links_file_not_empty():
    path = "outputs/links_per_paper.txt"

    assert os.path.exists(path)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert len(content) > 0


def test_keywords_file_not_empty():
    path = "outputs/abstract_keywords_top50.txt"

    assert os.path.exists(path)

    with open(path, "r", encoding="utf-8") as f:
        lines = [l for l in f.readlines() if l.strip()]

    assert len(lines) <= 50
import os
import glob
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

TEI_DIR = "data/tei"
OUT_DIR = "outputs"

def count_figures(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ns = {"tei": "http://www.tei-c.org/ns/1.0"}

    figures = root.findall(".//tei:figure", ns)

    return len(figures)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    files = sorted(glob.glob(os.path.join(TEI_DIR, "*.xml")))

    names = []
    counts = []

    for f in files:
        paper = os.path.basename(f).replace(".tei.xml", "")
        n = count_figures(f)

        print(f"{paper}: {n} figuras")

        names.append(paper)
        counts.append(n)

    # gráfico
    plt.figure(figsize=(10, 5))
    plt.bar(names, counts)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Número de figuras")
    plt.xlabel("Paper")
    plt.title("Figuras por paper")

    out_path = os.path.join(OUT_DIR, "figures_per_paper.png")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    print(f"\nGráfico guardado en: {out_path}")

if __name__ == "__main__":
    main()
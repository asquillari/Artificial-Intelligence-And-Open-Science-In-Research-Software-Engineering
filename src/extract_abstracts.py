import os
import glob
import xml.etree.ElementTree as ET

TEI_DIR = "data/tei"

def extract_abstract(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ns = {"tei": "http://www.tei-c.org/ns/1.0"}

    abstract = root.find(".//tei:abstract", ns)

    if abstract is not None:
        return "".join(abstract.itertext()).strip()
    
    return ""

def main():
    files = glob.glob(os.path.join(TEI_DIR, "*.xml"))

    abstracts = []

    for f in files:
        text = extract_abstract(f)
        print(f"\n--- {os.path.basename(f)} ---")
        print(text[:300])
        
        if text:
            abstracts.append(text)

    print(f"\nTotal abstracts encontrados: {len(abstracts)}")

if __name__ == "__main__":
    main()
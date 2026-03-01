import os
import time
import requests

def main():
    grobid_url = os.getenv("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")
    base = grobid_url.split("/api/")[0]  
    probe = base + "/api/isalive"

    for i in range(60):
        try:
            r = requests.get(probe, timeout=2)
            if r.status_code == 200:
                print("Grobid listo ✅")
                return
        except Exception:
            pass
        print("Esperando a Grobid...")
        time.sleep(2)

    raise SystemExit("ERROR: Grobid no respondió a tiempo")

if __name__ == "__main__":
    main()
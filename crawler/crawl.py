import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin, urlparse
from domains_settings import DOMAINS, MAX_PAGES_PER_DOMAIN



def extract_snippet(text, max_len=200):
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_len] + ("..." if len(text) > max_len else "")

def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return None

def crawl_page(url):
    html = fetch(url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title else "Senza titolo"

    p = soup.find("p")
    snippet = extract_snippet(p.get_text()) if p else "Nessuna descrizione disponibile."

    return {
        "id": "doc_" + str(abs(hash(url)))[:8],
        "title": title,
        "url": url,
        "snippet": snippet
    }

def get_internal_links(domain, html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        # Link assoluto
        full = urljoin(domain, href)

        # Filtra solo link dello stesso dominio
        if urlparse(full).netloc == urlparse(domain).netloc:
            links.add(full)

    return list(links)

def crawl_domain(domain):
    print(f"\n=== Indicizzo dominio: {domain} ===")

    homepage = fetch(domain)
    if not homepage:
        print("Errore nel caricamento del dominio.")
        return []

    links = get_internal_links(domain, homepage)

    print(f"Trovati {len(links)} link interni.")

    results = []
    count = 0

    for link in links:
        if count >= MAX_PAGES_PER_DOMAIN:
            break

        print(f"  -> Indicizzo pagina: {link}")
        data = crawl_page(link)
        if data:
            results.append(data)
            count += 1

    return results

def generate_mini_db():
    all_results = []

    for domain in DOMAINS:
        pages = crawl_domain(domain)
        all_results.extend(pages)

    js_content = "const miniDb = " + json.dumps(all_results, indent=2) + ";"

    with open("mini-db.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print("\nmini-db.js generato con successo!")

if __name__ == "__main__":
    generate_mini_db()

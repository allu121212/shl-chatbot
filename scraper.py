import requests
from bs4 import BeautifulSoup
import json
import time
BASE_URL = "https://www.shl.com"

CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(CATALOG_URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

links = soup.find_all("a")

products = []

visited = set()


for link in links:

    href = link.get("href")

    text = link.get_text(strip=True)

    if not href:
        continue

    if "/products/" not in href:
        continue

    full_url = href

    if href.startswith("/"):
        full_url = BASE_URL + href

    if full_url in visited:
        continue

    visited.add(full_url)

    print("Scraping:", full_url)

    try:

        product_page = requests.get(
            full_url,
            headers=headers
        )

        product_soup = BeautifulSoup(
            product_page.text,
            "lxml"
        )

        title = product_soup.find("h1")

        title = title.get_text(strip=True) if title else text

        paragraphs = product_soup.find_all("p")

        description = " ".join([
            p.get_text(strip=True)
            for p in paragraphs[:5]
        ])

        product = {
            "name": title,
            "url": full_url,
            "description": description
        }

        products.append(product)

        time.sleep(1)

    except Exception as e:
        print("Error:", e)


with open("data/catalog.json", "w", encoding="utf-8") as f:

    json.dump(
        products,
        f,
        indent=2,
        ensure_ascii=False
    )


print("\nDONE")
print("Total products:", len(products))
import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne html stránku a vrátí seznam všech odkazů.
    Odkazy mohou být v tagu <a> v libovolném pořadí atributů.
    """
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Download of {url} failed with status code {response.status_code}")

    html = response.content.decode("utf-8", errors="ignore")
    hrefs = []

    # pro jednoduchost rozdělíme html na kousky po "<a"
    parts = html.split("<a")

    for part in parts[1:]:
        # najdeme pozici atributu href=
        pos = part.find("href=")
        if pos == -1:
            continue

        # začátek hodnoty href
        start = part.find('"', pos)
        end = part.find('"', start + 1)

        # pokud není v uvozovkách, zkusíme apostrofy
        if start == -1 or end == -1:
            start = part.find("'", pos)
            end = part.find("'", start + 1)

        if start == -1 or end == -1:
            continue

        link = part[start + 1:end]

        if link.startswith("http"):
            hrefs.append(link)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    except IndexError:
        print("Nebylo zadano url")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

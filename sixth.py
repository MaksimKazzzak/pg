import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    responses = requests.get(url)
    hrefs = []
    if responses.status_code == 200:
        # succesfully donwloaded html
        html_text = responses.content.decode('utf-8').split('\n')
        # nakrajene na liny
        for line in html_text:
            if '<a href="' in line:
                href = line.split('"')[1]
                if href.startswith('http'):
                    hrefs.append(href)
    else:
        raise Exception(f'Dowload of {url} failed with status code {responses.status_code}')
    return hrefs


if __name__ == "__main__":
    #For test only
    #url = 'https://www.jcu.cz/cz/prijimaci-zkousky/prijimaci-rizeni'
    try:
        # osetrete potencialni chyby pomoci vetve except
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    except IndexError:
        print("Nebylo zadano url")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

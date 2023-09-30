"""
Fichier pour faire des essais avec les requêtes, téléchargements, etc
"""

import bs4
import requests
import wget

HOST = "https://www.zone-telechargement.pink"
dl_link = "https://a-10.1fichier.com/c607463268"
SAVE_FOLDER = "/media/julien/Data/Vidéos/Films/A voir/"


def httpify_movie_name(name):
    return name.replace(" ", "+").replace("'", "+")


def get_movie_page(name):
    name2 = httpify_movie_name(name)
    param = {'p': 'films', 'search': name2}
    print(f"url : {HOST}\n\n")
    response = requests.get(HOST, params=param)
    print(f"url de la réponse : {response.url}")
    print(f"status code : {response.status_code}")
    print(f"historique des url : {[r.url for r in response.history]}")
    return response.content


def soupify(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    return soup


def extract_movie_posters(soup):
    covers_info_title = soup.find_all("div", class_="cover_infos_title")
    for cov in covers_info_title:
        print(cov)


def download_movie(url, movie_name):
    filename = wget.download(url, out=SAVE_FOLDER + movie_name)
    print(f'nom du fichier : {filename}')


def core_requests_main():
    name = "django"
    page = get_movie_page(name)
    souppage = soupify(page)
    # print(souppage)
    extract_movie_posters(souppage)

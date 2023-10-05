"""
Fichier pour faire des essais avec les requêtes, téléchargements, etc
"""

import bs4
import requests
import wget

HOST = "https://www.zone-telechargement.pink"
dl_link = "https://a-10.1fichier.com/c607463268"
SAVE_FOLDER = "/media/julien/Data/Vidéos/Films/A voir/"


def httpify_movie_name(name):  # retire les espces, accents, apostrophes, etc. du nom
    return name.replace(" ", "+").replace("'", "+").replace("é", "e").replace("à", "a").replace("è", "e")


def get_movies_list_page(name):  # returns the HTML code of the movies list page, unparsed
    name2 = httpify_movie_name(name)
    param = {'p': 'films', 'search': name2}
    # print(f"url : {HOST}\n\n")
    response = requests.get(HOST, params=param)
    # print(f"url de la réponse : {response.url}")
    # print(f"status code : {response.status_code}")
    # print(f"historique des url : {[r.url for r in response.history]}")
    return response.content


def get_movie_page(arg):
    movie_id = arg[11:]
    # print(f"movie id : {movie_id}")
    param = {'p': 'film', 'id': movie_id}
    response = requests.get(HOST, params=param)
    # print(f"url de la réponse : {response.url}")
    # print(f"status code : {response.status_code}")
    # print(f"historique des url : {[r.url for r in response.history]}")
    return response.content


def get_dlprotect_page(url):
    url2, args = url.split("?")
    fn = args[3: - 6]
    param = {'fn': fn, 'rl': 'a2'}
    response = requests.get(url2, params=param)
    print(f"url de la réponse : {response.url}")
    print(f"status code : {response.status_code}")
    return response.content


def soupify(html):  # parses the HTML code given as an argument, returns the parsed code
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    return soup


def extract_movie_posters(soup):
    return soup.find_all("div", class_="cover_infos_title")


def download_movie(url, movie_name):  # downloads what is at the given url
    filename = wget.download(url, out=SAVE_FOLDER + movie_name)
    print(f'nom du fichier : {filename}')


def core_requests_main():
    name = "django"
    page = get_movies_list_page(name)
    souppage = soupify(page)
    # print(souppage)
    movies = extract_movie_posters(souppage)
    # for cov in movies:
    #     print(cov)
    arg = movies[0].find("a").get("href")
    # print(arg)
    movie_page = soupify(get_movie_page("?p=film&id=24679-django-unchained"))
    # print(movie_page)
    lien_unfichier = movie_page.find(string="1fichier")
    dlprotect_link = lien_unfichier.find_next(string="Télécharger").parent.get("href")

    dlprotect_page = get_dlprotect_page(dlprotect_link)
    soup_dl = soupify(dlprotect_page)
    print(soup_dl.prettify())

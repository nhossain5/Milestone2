"""
This is the application file with functions made using the APIs
"""
import os
import random
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/trending/movie/day"
TMDB_KEY = os.getenv("TMDB_KEY")


def get_movie_data():
    """
    This function gives us certains details about random popular movies
    """
    params = {"api_key": TMDB_KEY}

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    random_int = random.randint(0, 19)

    movie_id = data["results"][random_int]["id"]

    def get_id():
        ids = []
        ids.append(data["results"][random_int]["id"])
        return ids

    def get_genre():
        genre_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?"
        genre_params = {"movie_id": get_id(), "api_key": TMDB_KEY}
        genre_response = requests.get(genre_url, params=genre_params)
        genre_data = genre_response.json()
        genres = []
        genres.append(genre_data["genres"][0]["name"])
        return genres

    def get_title():
        titles = []
        titles.append(data["results"][random_int]["title"])
        return titles
        # return data["results"]

    def get_poster_path():
        poster_paths = []
        poster_paths.append(data["results"][random_int]["poster_path"])
        return poster_paths

    def get_tagline():
        tagline_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?"
        tagline_params = {"movie_id": get_id(), "api_key": TMDB_KEY}
        tagline_response = requests.get(tagline_url, params=tagline_params)
        tagline_data = tagline_response.json()
        taglines = []
        taglines.append(tagline_data["tagline"])
        return taglines

    def get_wikilink():
        wiki_url = "https://en.wikipedia.org/w/api.php"
        title = get_title()
        wikilink_params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": title[0] + " articletopic:films",
        }
        wikilink_response = requests.get(wiki_url, params=wikilink_params)
        wikilink_data = wikilink_response.json()
        wikilinks = []
        wikilink = "https://en.wikipedia.org/?curid="
        wikilinks.append(wikilink + str(wikilink_data["query"]["search"][0]["pageid"]))
        return wikilinks

    return {
        "titles": list(get_title()),
        "poster_paths": list(get_poster_path()),
        "taglines": list(get_tagline()),
        "ids": list(get_id()),
        "genres": list(get_genre()),
        "wikilinks": list(get_wikilink()),
    }

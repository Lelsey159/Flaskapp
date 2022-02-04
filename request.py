from app import app
import urllib.request,json
from models import movie

Movie = movie.Movie
# Getting api key
api_key = app.config['462d283f88ed0e80ee60521433f1bccc']

# Getting the movie base url
base_url = app.config["https://api.themoviedb.org/3/movie/550?api_key=462d283f88ed0e80ee60521433f1bccc"]

...

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results
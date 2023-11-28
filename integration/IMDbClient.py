import imdb

from model.Movie import Movie


def _get_directors(movie: imdb.Movie.Movie) -> list[str]:
    directors = set()
    if 'director' in movie.keys():
        for director in movie['director']:
            directors.add(director['name'])
    elif 'writer' in movie.keys():
        for director in movie['writer']:
            directors.add(director['name'])
    return list(directors)


class IMDbClient:
    def __init__(self):
        self.api = imdb.IMDb()

    def search_movie(self, query: str) -> (Movie, str):
        try:
            imdb_matches = self.api.search_movie(query)
            movie = imdb_matches[0]
            self.api.update(movie)
            directors = _get_directors(movie)
            return Movie(movie['title'],
                         '',
                         movie['kind'],
                         movie['genre'],
                         movie['country'],
                         movie['year'],
                         directors,
                         movie['cover url'],
                         movie['rating'],
                         0,
                         []), None
        except Exception as e:
            return None, e

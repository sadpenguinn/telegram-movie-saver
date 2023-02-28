import imdb

from model.Movie import Movie


class IMDbClient:
    def __init__(self):
        self.api = imdb.IMDb()

    def search_movie(self, query: str) -> Movie:
        imdb_matches = self.api.search_movie(query)
        movie = imdb_matches[0]
        self.api.update(movie)
        return Movie(movie['title'],
                           '',
                           movie['kind'],
                           movie['genre'],
                           movie['country'],
                           movie['year'],
                           movie['cover url'],
                           movie['rating'],
                           0)

from kinopoisk.movie import Movie


class KinopoiskClient:
    def __init__(self):
        self.movie = Movie()

    def search_movie(self, title_query: str):
        movies = self.movie.objects.search(title_query)
        movie = movies[0]

        return movie.title, movie.rating

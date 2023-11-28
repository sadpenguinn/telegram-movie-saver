from kinopoisk.movie import Movie


class KinopoiskClient:
    def __init__(self):
        pass

    def search_movie(self, title_query: str) -> (str, str, str):
        movie = Movie()

        err_response = lambda x: (None, None, x)
        try:
            movies = movie.objects.search(title_query)
            if len(movies) == 0:
                return err_response('No matches')

            movie = movies[0]
            return movie.title, round(movie.rating, 1), None

        except Exception as e:
            return err_response(e)

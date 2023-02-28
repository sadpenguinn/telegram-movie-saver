from notion_client import Client as NotionAPI

import model


class NotionClient:
    def __init__(self):
        self.api = NotionAPI(auth="secret_8yz9x3fEYoXIgdp75DfZYjbHnXF8ZCy3MHSH7nKAXqU")
        self.database_id = "1a581b54346a467f87de567cce9e01a3"

    def add(self, movie: model.Movie):
        new_page = {
            "Title": {"title": [{"text": {"content": movie.title}}]},
            "Russian Title": {"rich_text": [{"text": {"content": movie.title_russian}}]},
            "Year": {"number": movie.year},
            "Kind": {"select": {"name": movie.kind}},
            "Genre": {"multi_select": [{"name": g} for g in movie.genre]},
            "Country": {"multi_select": [{"name": c} for c in movie.country]},
            "IMDb Rating": {"number": movie.rating},
            "Kinopoisk Rating": {"number": movie.kp_rating}
        }

        self.api.pages.create(parent={"database_id": self.database_id}, properties=new_page)

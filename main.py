import logging
import re
import os

import telebot

from integration import IMDbClient, KinopoiskClient, NotionClient

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

MovieBot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"], parse_mode=None)

IMDb = IMDbClient.IMDbClient()
Kinopoisk = KinopoiskClient.KinopoiskClient()
Notion = NotionClient.NotionClient()


def get_title_from_query(title_query: str):
    title_regexp = '(.*)\s[0-9]+$'
    if re.match(title_regexp, title_query):
        return re.match(title_regexp, title_query).group(1).title()
    else:
        return title_query.title()


@MovieBot.message_handler(func=lambda message: True)
def text_message(message):
    title_query = message.text.lower().title()
    logging.info('New query: {}'.format(title_query))

    ##title = get_title_from_query(title_query)

    movie = IMDb.search_movie(title_query)
    title_russian, kp_rating, err = Kinopoisk.search_movie(title_query)
    if err is None:
        movie.title_russian = title_russian
        movie.kp_rating = kp_rating

    Notion.add(movie)

    MovieBot.reply_to(message, f"""{movie.title}\n{movie.title_russian}""")


MovieBot.infinity_polling()

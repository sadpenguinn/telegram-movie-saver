import logging
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


@MovieBot.message_handler(func=lambda message: True)
def text_message(message):
    title_query = message.text.lower().title()
    logging.info('New query: {}'.format(title_query))

    movie, err = IMDb.search_movie(title_query)
    if err is not None:
        logging.info('Can\'t get movie from IMDb: {}, {}'.format(title_query, err))
        MovieBot.reply_to(message, "Не удалось найти фильм на IMDb")
        return

    title_russian, kp_rating, err = Kinopoisk.search_movie(title_query)
    if err is None:
        movie.title_russian = title_russian
        movie.kp_rating = kp_rating
        movie.technical_tags = []
    else:
        movie.title_russian = ""
        movie.kp_rating = 0
        movie.technical_tags = ["Unstable"]

    if Notion.exists_by_title(movie.title):
        logging.info('Movie exists: {}'.format(movie.title))
        MovieBot.reply_to(message, "Фильм уже сохранен")
        return

    Notion.add(movie)

    notice = ""
    if len(movie.technical_tags) > 0:
        notice = " (Unstable)"
    MovieBot.reply_to(message, "Фильм сохранен{}\n{}\n{}".format(notice, movie.title, movie.title_russian))


MovieBot.infinity_polling()

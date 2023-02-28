import logging
import re
import os

from pyrogram import Client, filters

from integration import IMDbClient, NotionClient

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

MovieBot = Client(
    "bot",
    bot_token=os.environ["TELEGRAM_BOT_TOKEN"],
    api_id=int(os.environ["TELEGRAM_API_ID"])
)

IMDb = IMDbClient.IMDbClient()
Notion = NotionClient.NotionClient()


def get_title_from_query(title_query: str):
    title_regexp = '(.*)\s[0-9]+$'
    if re.match(title_regexp, title_query):
        return re.match(title_regexp, title_query).group(1).title()
    else:
        return title_query.title()


@MovieBot.on_message(filters.text)
async def new_movie(bot, update):
    title_query = update.text.lower().title()
    logging.info('New query: {}'.format(title_query))

    title = get_title_from_query(title_query)

    movie = IMDb.search_movie(title_query)
    movie.title_russian = title

    Notion.add(movie)

    await update.reply_photo(photo=movie.cover_url, caption=f"""{movie.title}\n{movie.title_russian}""")


MovieBot.run()

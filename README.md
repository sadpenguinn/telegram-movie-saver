# telegram-movie-saver

## Description

Bot accept messages with film names,
scraps info about film from IMDb and Kinopoisk
and store it to Notion database.

## Dependencies

### Telegram Bot

Provide it's token with `TELEGRAM_BOT_TOKEN`.

### Notion Database

Schema should fit next requirements:

| Name             | Type         |
|------------------|--------------|
| Title            | title        |
| Russian Title    | text         |
| Year             | number       |
| Kind             | select       |
| Genre            | multi-select |
| Country          | multi-select |
| Directors        | multi-select |
| IMDb Rating      | float        |
| Kinopoisk Rating | float        |
| Avg Rating       | float        |
| Technical Tags   | multi-select |

## Build & Run

```
docker build -t telegram-movie-saver -f Dockerfile . && \
docker run -e TELEGRAM_BOT_TOKEN={your-bot-token} telegram-movie-saver
```

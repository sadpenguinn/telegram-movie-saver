# telegram-movie-saver

## Description

Bot accept messages with film names,
scraps info about film from IMDb and Kinopoisk
and store it in Notion database.

## Dependencies

### Telegram Bot

Provide it's token with `TELEGRAM_BOT_TOKEN`

### Python libs

```
pip3 install -r requirements.txt
```

### Notion Database

Schema should fit next requirements

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
python3 main.py
```

# Photo to telegram

space_photo allows download photo from spacex and nasa API.
tg_bot allows post photo to telegram channel with delay.

## Install

Python 3 must be installed.

- install requirements.txt with pip:

```
pip install -r requirements.txt
```

- create .env file with vars:

Key for [nasa](https://api.nasa.gov/) api, like:
```
NASA_API_KEY=Aa1a0aaAaAa1AA0AAAaaAAAaaaaAaaaaaAAAAaAA
```

Key for telegram bot using @BotFather, like:
```
TG_TOKEN=1010111111:AAAAAAA1A0aaaaaaaaaAaA1aaaa0AAaaaa0
```

Channel id which will be used for posting, like:
```
CHANNEL_ID=@YourGroupForSpacePhoto
```

Delay vars which using for pause beetween posting photo, default 24 hours, max 25 hours 1 min, like:
```
DELAY_SECONDS=10
DELAY_MINUTES=0
DELAY_HOURS=1
STORAGE_NAME=images
```

You need to create channel for posting photo and telegramm bot using @BotFather.

When you create telegramm bot and channel for posting photo, you need to add your bot to admin group of your channel for posting, then turn on all admin settings for your telegramm bot.  

## Get started

Download nasa photos in your project dir:
```
python3 fetch_nasa.py
```
You can use args:
- --apods=int, number of day to download nasa apods pics, default 10
- --epic=int, number of day to download nasa epic pics Earth planet, default 10

Find and download last spacex launch photos in your project dir:
```
python3 fetch_spacex.py
```

Start posting photo in your telegram channel, with delay which you set in .env
```
python3 tg_bot.py
```

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
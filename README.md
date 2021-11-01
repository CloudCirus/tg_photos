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

Channel id which will be used for for posting, like:
```
CHANNEL_ID=@YourGroupForSpacePhoto
```

Delay vars which using for pause beetween posting photo, default 24 hours, max 25 hours 1 min, like:
```
SEC=10
MIN=0
HOUR=1
```

You need to create channel for posting photo and telegramm bot using @BotFather.

When you create telegramm bot and channel for posting photo, you need to add your bot to admin group of your channel for posting, than tern on all admin settings for your telegramm bot.  

## Get started

Download photo in your project dir
```
python3 space_photo.py
```
You can use args:
- --spx=True/False for find and download spacex last spacex launch photos.
- --apods=int for download chosen number nasa apods pics, default 1
- --epic=int for download shosen number of nasa pics Earth planet, default 1

Start posting photo in your telegram channel, with delay which you input in .env vars
```
python3 tg_bot.py
```

## Project goals <a name = "project_goals"></a>

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
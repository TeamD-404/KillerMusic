import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

#❖ Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20851717"))
API_HASH = getenv("API_HASH", "0217fe5cd94ff3f4d4555b1551670144")

#❖ Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", None)

#❖  Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "KillerMusicBot")

#❖  Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "KILLER MUSIC")

#❖ get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "AVISHA_ASS")

#❖ Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7320662885:AAF7V6_xBh9Nfqa-RDHSJ7Svo3TTtxDbnmE")

#❖ Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://BWFMUSIC:BWFMUSIC@cluster0.xwnup2l.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600000))

#❖  Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002100219353"))

#❖ Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6454209118"))

#❖  Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

#❖  Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamD-404/KillerMusic",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  #❖ Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/royal_dp_tg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Royal_member_tg")

#❖ Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


#❖ Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e319091f771445b18c029299505d5d4f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "293c334a2861415197a697b2d11dd4de")


#❖ Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


#❖ Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
#❖ Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


#❖ Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQE-LAUAUYigEbRrsjk8_PUWFgMJqsu7qFMOjgeLpN9WCoubD0V2wKX45HiIVRs09DzAdxhhnYNR6TQxTcSMrjXBBmyMnJhyMxabmexJg4PKGc3MvhVoDJbbjy7jBSbfxtUqeRg0l3ULoMM3S4a4HjdNjFLu76hQS2JBA62lxtrD4ajsetKW5kbEQ_-du-A9ObXAav7eC5a5fMFW36fk9AvqlFxROlsv7vQz_lfOHIPpF_HipQkQ-b5qAAhLVIYzni_yFuFsVgib9ubnaEttlZGFj4Ki6zkHnl-n1sKWy5yVkI65--m2UUXwv47nPdIqc7O5Cl6RCAl2kH77v9fIavFpZ0QDDgAAAAGxC4UDAA"
")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/4358fe2224af4803eb4ef.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/dec61e858d57c14343455.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://graph.org/file/e4a11714fd2fb6bde0082.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

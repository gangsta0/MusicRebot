#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int("1225523")
API_HASH = "ec0ae6e668e4eaa669c536acf13c9f59"

## Get it from @Botfather in Telegram.
BOT_TOKEN = "5999040209:AAHU2BVcJ7dX_9kfQB8NmsVAzWzRw0Dy0KU"

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = "mongodb+srv://babsdiqaqas:bakir143@cluster0.9g48icy.mongodb.net/?retryWrites=true&w=majority"

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int("60")
  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int("180")
# Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int("-1001605064659")

# A name for your Music bot.
MUSIC_BOT_NAME = "Nurlan Musiqi"

# Your User ID.
OWNER_ID = [1464910930,1339412165]
  # Input type must be interger

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("asd", "9bb99fd0-8141-4593-be9f-0afbd937b58d")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("saf", "musiqimtestimbotumnurlan")

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamYukki/YukkiMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "https://t.me/c9ala", "https://t.me/nurlanstm"
)  # Example:- https://t.me/TheYukki
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/oldlaryurdu"
)  # Example:- https://t.me/YukkiSupport

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", True)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", True)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", False)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/c9alaa")

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "727813041fc142c28646a817f72f09cb")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "84122b4324db4659ac19f44808675f83")

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "15"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("STRING_SESSION", "AgBvmwDNDM6Q-mTotUlspgUuN5voddB4V7vjZ-ktXCVci3VRamSRaZ49xJhv6RhHtA3Gytl-A6QryCmDCBLMkWanswOCQ5BCqLis5_BCOBki3oubiT2sbzCsDwkd0RUHGgHIolyBc6QzHtKuMk8SO-CcxdUZ7CeXKFWY32eW-CiwuynY3TKdIA2dKLWdJAOeAvo-VwcSUKr9R5vS44Om0-Inb0gEZx8cTYjTa8n-bjI9BPPY8Y6qcA00gBFpyW0QXhHUZPBl9vnAXXC9sJi4ntkJU3AqCr92qRqtd943cIhs2L9yo1xVPAL6U_ymQBhA1WJI9PSKHATi7izphSG8aheuAAAAAXHnUUcA")
STRING2 = getenv("STRING_SESSION", "AgBQhlgY3JeWkOpjApMA346uKZNRixmajb-InK8LiygFzUT1T-llT8uvssdxLnsk52kYexM-F5OK2J8saWap22p98Jx1lPf0Bj9cXbO_Iriizcxt_UKuTTktDCVCp38v-jlrxIYDD2QblDShvXd45PinCBSyTgCKVB1FpTRDAVU11EsOtTIIQhJaSnHJZ2k-yS5hcsJERschNXagVP8QmPpShKtB-ZdN1rP_CV4nfdxtw_C59Y_RRT7CPlfBcrb8qaRtmWbgKBZo3LUsIJNNsfAddOiLvsUlvKPlcv5AiWkd1QgqjfRctMY6FIWK-thzqRqVPZP8M3Aj2NR0KtmQkU_8ZyZL0wA")
STRING3 = getenv("STRING_SESSION", "AgBvmwDNDM6Q-mTotUlspgUuN5voddB4V7vjZ-ktXCVci3VRamSRaZ49xJhv6RhHtA3Gytl-A6QryCmDCBLMkWanswOCQ5BCqLis5_BCOBki3oubiT2sbzCsDwkd0RUHGgHIolyBc6QzHtKuMk8SO-CcxdUZ7CeXKFWY32eW-CiwuynY3TKdIA2dKLWdJAOeAvo-VwcSUKr9R5vS44Om0-Inb0gEZx8cTYjTa8n-bjI9BPPY8Y6qcA00gBFpyW0QXhHUZPBl9vnAXXC9sJi4ntkJU3AqCr92qRqtd943cIhs2L9yo1xVPAL6U_ymQBhA1WJI9PSKHATi7izphSG8aheuAAAAAXHnUUcA")
STRING4 = getenv("STRING_SESSION", "AgBvmwDNDM6Q-mTotUlspgUuN5voddB4V7vjZ-ktXCVci3VRamSRaZ49xJhv6RhHtA3Gytl-A6QryCmDCBLMkWanswOCQ5BCqLis5_BCOBki3oubiT2sbzCsDwkd0RUHGgHIolyBc6QzHtKuMk8SO-CcxdUZ7CeXKFWY32eW-CiwuynY3TKdIA2dKLWdJAOeAvo-VwcSUKr9R5vS44Om0-Inb0gEZx8cTYjTa8n-bjI9BPPY8Y6qcA00gBFpyW0QXhHUZPBl9vnAXXC9sJi4ntkJU3AqCr92qRqtd943cIhs2L9yo1xVPAL6U_ymQBhA1WJI9PSKHATi7izphSG8aheuAAAAAXHnUUcA")
STRING5 = getenv("STRING_SESSION", "AgBvmwDNDM6Q-mTotUlspgUuN5voddB4V7vjZ-ktXCVci3VRamSRaZ49xJhv6RhHtA3Gytl-A6QryCmDCBLMkWanswOCQ5BCqLis5_BCOBki3oubiT2sbzCsDwkd0RUHGgHIolyBc6QzHtKuMk8SO-CcxdUZ7CeXKFWY32eW-CiwuynY3TKdIA2dKLWdJAOeAvo-VwcSUKr9R5vS44Om0-Inb0gEZx8cTYjTa8n-bjI9BPPY8Y6qcA00gBFpyW0QXhHUZPBl9vnAXXC9sJi4ntkJU3AqCr92qRqtd943cIhs2L9yo1xVPAL6U_ymQBhA1WJI9PSKHATi7izphSG8aheuAAAAAXHnUUcA")


#  __     ___    _ _  ___  _______   __  __ _    _  _____ _____ _____   ____   ____ _______
#  \ \   / / |  | | |/ / |/ /_   _| |  \/  | |  | |/ ____|_   _/ ____| |  _ \ / __ \__   __|
#   \ \_/ /| |  | | ' /| ' /  | |   | \  / | |  | | (___   | || |      | |_) | |  | | | |
#    \   / | |  | |  < |  <   | |   | |\/| | |  | |\___ \  | || |      |  _ <| |  | | | |
#     | |  | |__| | . \| . \ _| |_  | |  | | |__| |____) |_| || |____  | |_) | |__| | | |
#     |_|   \____/|_|\_\_|\_\_____| |_|  |_|\____/|_____/|_____\_____| |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", None)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()

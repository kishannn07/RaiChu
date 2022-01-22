import os
import heroku3
from decouple import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def fetch_heroku_git_url(api_key, app_name):
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")

class Var(object):
    # Mandatory
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    BOT_USERNAME = config("BOT_USERNAME", default=None)
    SESSION = config("SESSION", default=None)
    DB_URL = config("DATABASE_URL", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=None, cast=int)
    BLACKLIST_CHAT = set(int(x) for x in config("BLACKLIST_CHAT", "").split())
    OWNER_ID = config("OWNER_ID", default=None, cast=int)
    MONGO_DB = config("MONGO_DATABASE", default=None)
    try:
        HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
        HEROKU_API = config("HEROKU_API", default=None)
    except BaseException:
        HEROKU_APP_NAME = None
        HEROKU_API = None
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/ToxicCybers/kinguserbot"
    )
    U_BRANCH = "ToxicCyber"
    if HEROKU_API and HEROKU_APP_NAME:
        HEROKU_URL = fetch_heroku_git_url(HEROKU_API, HEROKU_APP_NAME)
    else:
        HEROKU_URL  =None

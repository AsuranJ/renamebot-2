import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "http://62.210.149.20:8000/direct.php?data=dTGWma%2FCRRXAx4l2AdBRZwiiqYBXGwmD2nkJqDQH3Mze67aaGNRf7N0wQKpocvFnAXix9l5bAT9Oz01CLy4qa2Ph%2FT8oF78lidZWlnxmkf4YbN6qs%2Bxs55W2Re%2F%2F%2FgauyieR4TbF4VAObB7gL0MyzHro%2FuBzmuv8iZWy9me6Mf1pB2YyDpwpOXnmI3752MOYYDyB7vnL291AFZHD0y0FWK%2BPId7vyQT6q4inlDpXEg7VcnwENkZ5SqnePut0AIsqAJjB8f%2FZ6bvBIHJc7hWmEfpQj6xSsOliX1Xap49vP9J0awyxIwZ30pE%2Fa65dHodF1XvwViWsFgF44Ne%2F576v%2BR9Vw8BrDWGAL5lGsyypRC9YmjQSeIQaHktQmrIhHzGgBkaSHs6tnyofnqFTuXy5S4wovawnJhJi6EaEEbF7UYL2BwjuC5FC%2BVfLpsuFjNt0EwrFidA2jtGmrt1m8UUH8BcbnkvvyTL1iTneFDsCuZjHkQW7OJqlkoLyeYtKszXk"
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "")

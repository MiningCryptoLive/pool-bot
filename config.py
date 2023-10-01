# The API token got from the bot father
API_TOKEN = '6478261573:AAGXV_nSxSdBU1rCon46R5EIryqwj7ai39s'

# The username of the channel the bot will post new blocks to
CHANNEL_USERNAME = '@solopoolpro_bot'

# The list of the ID of the people that are going to create or delete sellers.
ACTIVATE_MODERATOR_FILTERING = True
MODERATOR_USER_NAMES = ['solopool.pro']

# The map between the coin and the API url
COIN2URL_MAP = {
    "ETC-SOLO": "https://solopool.pro/api/pools/etcsolo",
    "RAVEN-SOLO": "https://solopool.pro/api/pools/ravensolo",
    "ERGO-SOLO": "https://solopool.pro/api/pools/ergosolo"
}

# The secret is a token (not the bot token though) for secure webhook connection
SECRET = "FFS3TgUB9WtZS3TgUFS3TgFS3TgUB9WtZUB9WtZB9WtZ"

# Message strings
FATAL_ERROR_MESSAGE = "Oooops ! Something unexpected occured."
NOT_MODERATOR_MESSAGE = "You not allowed to talk to this bot."
DATANOTFOUND_STR = "Not found"

# Some other technical configurations
APP_LOG_FILENAME = "cryptoapi_bot.log"
COUNTSDICT_FILENAME = "cryptoapi.sqlite"

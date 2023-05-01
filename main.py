from discord_bot_project.bot import client
from discord_bot_project.config import TOKEN, API_KEY
from discord_bot_project.api import validate_api_key

validate_api_key(API_KEY)

if __name__ == '__main__':
    client.run(TOKEN)
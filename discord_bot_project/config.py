import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
API_KEY = os.environ.get("CMC_API_KEY")
IMGUR_CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
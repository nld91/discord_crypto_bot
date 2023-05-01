import discord
from discord_bot_project.formatting import format_price_embed
from discord_bot_project.api import get_crypto_data
from discord_bot_project.chart import plot_historical_data
from discord_bot_project.config import IMGUR_CLIENT_ID
from discord_bot_project.error_handling import InvalidSymbolError, APIError

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """
    Prints a message to the terminal where the bot is running once it's ready
    """
    print(f'{client.user} is now running!')


@client.event
async def on_message(message):
    """
    Handles incoming messages from the server where the bot is running.
    Responds to commands given with an exclamation mark as a suffix. E.g: !BTC
    """
    # Checks if the message send was from the bot and ignores it if it is.
    if message.author == client.user:
        return

    channel = message.channel
    
    # Checks to see if the correct command suffix is used "!".
    if message.content.startswith("!"):
        
        # Get the token symbol from the message content.
        token_symbol = message.content[1:].upper()
        
        try:
            # Get the name and prices for the given token symbol.
            token_name, prices = get_crypto_data(token_symbol)

            # Get a URL for an image of a historical price chart for the token.
            imgur_url = plot_historical_data(token_name, 30, IMGUR_CLIENT_ID)
            
            # Format an embed message to post as a response
            embed = format_price_embed(token_name, token_symbol, prices, imgur_url)

            # Send the formatted message to the channel
            await channel.send(embed=embed)
            
        except (InvalidSymbolError, APIError, ValueError, IndexError) as e:
            await channel.send(str(e))
import discord
from discord_bot_project.utils import encode_token_name

def format_price_embed(token_name: str, token_symbol: str, prices: dict, changes_24h: dict, imgur_url: str) -> discord.Embed:
    """
    Formats an embed containing the current prices of a cryptocurrency in the specified currencies.

    Parameters:
    symbol (str): The symbol of the cryptocurrency to format the message for.
    prices (dict): A dictionary containing the prices of the cryptocurrency in different currencies.
    chart_image_path (str): The path to the chart image file.

    Returns:
    discord.Embed: The formatted message as an embed object.
    """
    # Define a currency symbol dictionary
    currency_symbols = {
        "USD": "$",
        "GBP": "£",
        "EUR": "€",
    }

    # Create an embed object
    embed = discord.Embed(title=f"{token_symbol} PRICES:", url=f"https://coinmarketcap.com/currencies/{encode_token_name(token_name).lower()}/", color=0xfdbe02)

    # Add fields to show price for each currency code to the embed
    for currency_code, price in prices.items():

        # Get correct FIAT symbol for currency code
        fiat_symbol = currency_symbols.get(currency_code, currency_code))

        # Determine whether to include a + or - sign before the 24h change value
        if changes_24h >= 0:
            sign = "+"
        else:
            sign = "-"

        # Add a field to the embed for the currency and price
        embed.add_field(name=currency_code, value=f"{fiat_symbol}{price:.2f}", inline=True)
        embed.add_field(name="24h", value=f"{sign}{abs(changes_24h):.4f}%", inline=True)
        embed.add_field(name=" ", inline=False)
  
    if imgur_url is not None:
        # Add chart image from imgur url
        embed.set_image(url=imgur_url)
    else:
        embed.add_field(name="Historical Data Not Available", value=f"Sorry, no historical data could be found for {token_symbol}, so no chart will be generated.", inline=False)    
   
    return embed

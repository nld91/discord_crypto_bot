import discord
from discord_bot_project.utils import encode_token_name

def format_price_embed(token_name: str, token_symbol: str, crypto_data: dict, imgur_url: str) -> discord.Embed:
    """
    Formats an embed containing the current prices of a cryptocurrency in the specified currencies.

    Parameters:
    token_name (str): The name of the cryptocurrency
    token_symbol (str): The symbol of the cryptocurrency to format the message for.
    crypto_data (dict): A dictionary containing the prices and 24h changes.
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
    for currency_code in crypto_data:
        price = crypto_data[currency_code][1]
        change_24h = crypto_data[currency_code][2]

        # Get correct FIAT symbol for currency code
        fiat_symbol = currency_symbols.get(currency_code, currency_code)

        # Determine whether to include a + or - sign before the 24h change value
        if change_24h >= 0:
            change_sign = "+"
        else:
            change_sign = "-"

        # Add a field to the embed for the currency and price
        embed.add_field(name=currency_code, value=f"{fiat_symbol}{price:.2f}", inline=True)
        embed.add_field(name="24h", value=f"{change_sign}{abs(change_24h):.4f}%", inline=True)
        embed.add_field(name=" ", value=" ", inline=False)
  
    if imgur_url is not None:
        # Add chart image from imgur url
        embed.set_image(url=imgur_url)
    else:
        embed.add_field(name="Historical Data Not Available", value=f"Sorry, no historical data could be found for {token_symbol}, so no chart will be generated.", inline=False)    
   
    return embed

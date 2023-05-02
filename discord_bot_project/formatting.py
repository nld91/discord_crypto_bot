import discord
from discord_bot_project.utils import encode_token_name

def format_price_embed(token_name: str, token_symbol: str, token_prices: dict, token_changes: list, imgur_url: str) -> discord.Embed:
    """
    Formats an embed containing the current prices of a cryptocurrency in the specified currencies.

    Parameters:
    token_name (str): The name of the cryptocurrency
    token_symbol (str): The symbol of the cryptocurrency to format the message for.
    token_prices (dict): A dictionary containing the prices.
    token_changes (list): A list containing the 1h, 24h, and 30d changes.
    imgur_url (str): The URL to the chart image file.

    Returns:
    discord.Embed: The formatted message as an embed object.
    """
    # Define a currency symbol dictionary
    currency_symbols = {
        "USD": "$",
        "GBP": "£",
        "EUR": "€",
    }

    # Define a list of change periods as text
    change_periods = ["1h", "24h", "30d"]

    # Create objects for various url's to be used within the embed
    embed_title_url = f"https://coinmarketcap.com/currencies/{encode_token_name(token_name).lower()}/"
    embed_author_url = "https://github.com/nld91"

    # Define the embed title and description objects
    embed_title = f"{token_name} {token_symbol}"
    embed_description = f"Current price data for the {token_name} token:"
    
    # Create an embed object
    embed = discord.Embed(title=embed_title, url=embed_title_url, description=embed_description, color=0xfdbe02)

    # Add the author object to the embed
    embed.set_author(name="nld91", url=embed_author_url)

    # Add fields to show price for each currency code to the embed
    for i, currency_code in enumerate(token_prices):
        token_price = token_prices[currency_code]
        token_change = token_changes[i]
        change_period = change_periods[i]
        
        # Get correct FIAT symbol for currency code
        fiat_symbol = currency_symbols.get(currency_code, currency_code)

        # Determine the number of decimal places to use for price
        decimal_places = 2
        if token_price < 1:
            decimal_places = 6

        # Format token price
        formatted_token_price = f"{token_price:.{decimal_places}f}"

        # Determine whether to include a + or - sign before the percent change value
        if token_change >= 0:
            change_sign = "+"
        else:
            change_sign = "-"

        # Add a field to the embed for the currency and price
        embed.add_field(name=currency_code, value=f"{fiat_symbol}{formatted_token_price}", inline=True)
        embed.add_field(name=change_period, value=f"{change_sign}{abs(token_change):.4f}%", inline=True)
        embed.add_field(name=" ", value=" ", inline=False)
  
    if imgur_url is not None:
        # Add field to explain graph data
        embed.add_field(name="Historical Price Data:", value=f"The chart below shows {token_name} price data plotted over the last 30 days, click to enlarge!")

        # Add chart image from imgur url
        embed.set_image(url=imgur_url)

    else:
        # If no historical data was found, generate an error message shown in a field
        embed.add_field(name="Historical Data Not Available!", value=f"Sorry, no historical data could be found for {token_symbol}, so no chart will be generated.", inline=False)    
   
    return embed

import requests
from enum import Enum
from typing import Tuple, List, Dict, Union
from datetime import datetime
from discord_bot_project.cache import cache_data
from discord_bot_project.error_handling import handle_api_error
from discord_bot_project.config import API_KEY
from discord_bot_project.utils import encode_token_name

ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

class FiatCurrency(Enum):
     USD = "USD"
     EUR = "EUR"
     GBP = "GBP"

def make_request(token_symbol: str) -> List[dict]:
    """
    Makes an HTTP request to the CoinMarketCap API with the specified parameters.

    Parameters:
    token_symbol (str): The symbol of the cryptocurrency to retrieve data for.

    Returns:
    List[dict]: A list of JSON responses from the API, one for each currency conversion.
    """
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }

    currencies = [currency.value for currency in FiatCurrency]
    responses = []

    for currency in currencies:
        params = {"symbol": token_symbol, "convert": currency}
        response = requests.get(ENDPOINT, headers=headers, params=params)
        handle_api_error(response, token_symbol)
        responses.append(response.json())

    return responses


@cache_data(cache_key_prefix="get_crypto_price")
def get_crypto_data(token_symbol: str) -> Tuple[str, Dict[str, List[Union[str, float, float]]]]:
    """
    Returns the current price of a cryptocurrency in the specified currency, utilising the CoinMarketCap API. 
    Caches data to be used in future searches using TTLCache.

    Parameters:
    token_symbol (str): The symbol of the cryptocurrency to retrieve the price of.

    Returns:
    Tuple[str, Dict[str, List[Union[str, float, float]]]]: A tuple containing the name of the cryptocurrency and a dictionary mapping each currency to a list containing the token symbol, price, and 24-hour percent change for the specified cryptocurrency.
    """
    data_list = make_request(token_symbol)

    name = data_list[0]["data"][token_symbol]["name"]

    crypto_data = {}
    
    for data, currency in zip(data_list, FiatCurrency):
        price = data["data"][token_symbol]["quote"][currency.value]["price"]
        percent_change_24h = data["data"][token_symbol]["quote"][currency.value]["percent_change_24h"]
        crypto_data[currency.value] = [token_symbol, price, percent_change_24h]

    print(crypto_data)        
    return name, crypto_data



@cache_data(cache_key_prefix="get_historical_data")
def get_historical_data(token_name: str, days: int) -> List[Tuple[datetime, float]]:
    """
    Returns historical price data for a given cryptocurrency using the CoinGecko API.

    Parameters:
    token_name (str): The symbol of the cryptocurrency to retrieve data for.
    days (int): The number of days of historical data to retrieve.

    Returns:
    list: A list of tuples containing the date and price for each day.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{encode_token_name(token_name).lower()}/market_chart?vs_currency=usd&days={days}"

    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    try:
        data = response.json()["prices"]
    except ValueError:
        return None

    formatted_data = [(datetime.utcfromtimestamp(timestamp/1000), price) for timestamp, price in data]

    return formatted_data


def validate_api_key(api_key: str) -> None:
    """
    Validates that the provided API key is not empty.

    Parameters:
    api_key (str): The API key to validate.

    Raises:
    ValueError: If the API key is empty.
    """
    if not api_key:
        raise ValueError("API key is missing. Please check correct CoinMarketCap API key is used.")
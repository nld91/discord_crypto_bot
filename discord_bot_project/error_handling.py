import requests

class InvalidSymbolError(ValueError):
    """
    Custom exception class for invalid symbol errors.
    """
    pass

class APIError(Exception):
    """
    Custom exception class for API errors.
    """
    pass


def raise_http_error(response: requests.Response) -> None:
    """
    Helper function to raise errors based on the HTTP status code.
    """
    if response.status_code == 400:
        raise InvalidSymbolError("Invalid symbol provided")
    elif response.status_code == 401:
        raise APIError("Unauthorized access to the API")
    elif response.status_code == 403:
        raise APIError("Forbidden access to the API")
    elif response.status_code == 429:
        raise APIError("API rate limit exceeded")
    elif response.status_code == 500:
        raise APIError("Internal server error on the API")
    else:
        raise APIError(f"An error occurred while retrieving the price data. Status code: {response.status_code}")


def handle_api_error(response: requests.Response, token_symbol: str) -> None:   
    """
    Function to handle API errors and raise custom exceptions based on the response.

    Parameters:
    response (requests.Response): The API response object.
    token_symbol (str): The symbol of the cryptocurrency.

    Raises:
    APIError: If the API response does not contain the required data or the HTTP status code is not 200.
    InvalidSymbolError: If the symbol provided is not found in the API response.
    """
    if response.status_code != 200:
        raise_http_error(response)
    
    data = response.json()
    
    if "data" not in data:
        raise APIError("No data returned while retrieving the price data from the CoinMarketCap API")

    if token_symbol not in data["data"]:
        raise InvalidSymbolError(f"Sorry, I could not find the price for {token_symbol}")
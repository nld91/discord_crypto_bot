def encode_token_name(token_name) -> str:
    """
    Returns an encoded token name with all spaces replaced by hyphens to prevents errors cause by malformed url addresses.

    Parameters:
    token_name (str): The name of the token.

    Returns:
    str: An encoded token name string where spaces have been replaced with hyphens.
    """
    encoded_name = token_name.replace(" ", "-")

    return encoded_name
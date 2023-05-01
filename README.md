# Discord Crypto Bot

A simple Discord bot that provides real-time cryptocurrency prices and historical data with a graph. Uses CoinMarketCap API for real-time data and CoinGecko for historical data.

Both API's are free use, CoinMarketCap requires an API key and account, CoinGecko does not but you are limited to a certain number of requests per hour.

Graphing is handled by matplotlib but the image is uploaded to Imgur via their API.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up a Discord bot account [here](https://discord.com/developers/applications) and obtain a token for your bot.
4. Set up a CoinMarketCap pro account [here](https://pro.coinmarketcap.com/account) to obtain your API key.
5. Set up an Imgur account and go [here](https://api.imgur.com/oauth2/addclient) to register an application for your bots graph images.
6. Create a .env file with the following format:
```
DISCORD_TOKEN=<your_discord_bot_token_here>
CMC_API_KEY=<your_coinmarketcap_api_key_here>
IMGUR_CLIENT_ID=<your_imgur_client_id_here>
```
7. Run the bot using `python3 main.py`.

## Usage

Once the bot is running, it will respond to commands structured:

- `!<token_symbol>`

For example:

- `!BTC`
- `!ETH`
- `!BNB`

*Where historical data can not be found the bot will still return current price information but no graph will be shown*

## Contributing

Contributions are welcome! Please open an issue or pull request for any feature requests or bug fixes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

# Discord Crypto Bot

A simple Discord bot that provides real-time cryptocurrency prices and historical data with a graph. Uses CoinMarketCap API for real-time data and CoinGecko for historical data.

Both API's are free use, CoinMarketCap requires an API key and account, CoinGecko does not but you are limited to a certain number of requests per hour.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up a Discord bot account and obtain its token.
4. Set the bot token in the `config.py` file.
5. Run the bot using `python3 main.py`.

## Usage

Once the bot is running, it will respond to commands structured:

- `!<token_symbol>`

For example:

- `!BTC`
- `!ETH`
- `!BNB`

## Contributing

Contributions are welcome! Please open an issue or pull request for any feature requests or bug fixes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

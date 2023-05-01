import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import requests
from discord_bot_project.api import get_historical_data

def plot_historical_data(name: str, days: int, imgur_client_id: str) -> str:
    """
    Plots a line graph of the historical price data for a given cryptocurrency using Matplotlib.

    Parameters:
    name (str): The name of the cryptocurrency to plot historical data for.
    days (int): The number of days of historical data to plot.
    imgur_client_id (str): The client ID for the Imgur API.

    Returns:
    str: The URL of the chart image file uploaded to Imgur.
    """
    data = get_historical_data(name, days)

    if data is None:
        return None

    dates = [d[0] for d in data]
    prices = [d[1] for d in data]

    # Set chart parameters
    plt.rcParams.update({
        'figure.figsize': [18, 9],
        'font.size': 10,
        'axes.titlesize': 32,
        'axes.labelsize': 20,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'axes.titlecolor': '#D8D8D8',
        'axes.labelcolor': '#D8D8D8',
        'axes.edgecolor': '#505050',
        'xtick.color': '#D8D8D8',
        'ytick.color': '#D8D8D8',
        'figure.facecolor': '#36393F',
        'axes.facecolor': '#36393F',
        'grid.color': '#505050'
    })

    # Create a new figure and axes
    fig, ax = plt.subplots()
  
    # Plot historical price data as a line graph, set axes labels and title
    ax.plot(dates, prices, color='orange')
    ax.set_xlabel("Date", labelpad=20)
    ax.set_ylabel("Price (USD)", labelpad=20)
    ax.set_title(f"Historical Price Data for {name.upper()} ({days} Days)", pad=20)

    # Use AutoDateLocator and AutoDateFormatter for X-axis ticks and labels
    date_locator = mdates.AutoDateLocator(minticks=30, maxticks=60)
    date_formatter = mdates.DateFormatter('%d-%b')
    ax.xaxis.set_major_locator(date_locator)
    ax.xaxis.set_major_formatter(date_formatter)
    plt.gcf().autofmt_xdate()

    # Get the current price value
    current_price = prices[-1]

    # Add a horizontal line at the current price level
    ax.axhline(y=current_price, color='#ADD8E6', linestyle='--', linewidth=1)

    # Add a label for the horizontal currnet price line
    ax.text(dates[-1], current_price, f'${current_price:.2f}', ha='left', va='bottom', color='#D8D8D8', fontsize="24")

    # Show plot grid
    ax.grid(True)
    
    # Save chart to file
    chart_file = os.path.abspath("chart.png")
    plt.savefig(chart_file)

    # Upload chart image to Imgur and get URL
    imgur_url = upload_image_to_imgur(chart_file, imgur_client_id)

    plt.close()  # Close the figure to free up memory

    return imgur_url


def upload_image_to_imgur(image_path: str, imgur_client_id: str) -> str:
    """
    Uploads an image file to Imgur and returns the URL of the uploaded image.

    Parameters:
    image_path (str): The path to the image file to upload.
    imgur_client_id (str): The client ID to use for the Imgur API.

    Returns:
    str: The URL of the uploaded image.
    """
    with open(image_path, "rb") as image_file:
        payload = {
            "image": image_file.read(),
            "type": "file"
        }

        headers = {
            "Authorization": f"Client-ID {imgur_client_id}"
        }
        response = requests.post("https://api.imgur.com/3/image", headers=headers, data=payload)

        return response.json()["data"]["link"]
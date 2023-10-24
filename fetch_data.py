from binance.client import Client
import os

BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
BINANCE_API_SECRET = os.environ.get("BINANCE_API_SECRET")

# Initialize the Binance client (In production, use environment variables or a config file for API keys)
client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)

def fetch_recent_trades(symbol="BTCUSDT", limit=100):
    """Fetch recent trade data from Binance."""
    trades = client.get_recent_trades(symbol=symbol, limit=limit)
    return trades

if __name__ == "__main__":
    data = fetch_recent_trades()
    for trade in data:
        print(trade)

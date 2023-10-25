from binance.client import Client
import os
from models import init_db, SessionLocal, add_trade

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
    session = SessionLocal()
    init_db()

    for trade in data:
        trade_data = {
            "symbol": "BTCUSDT",
            "price": float(trade["price"]),
            "quantity": float(trade["qty"]),
            "time": trade["time"]
        }
        add_trade(session, trade_data)

    session.close()


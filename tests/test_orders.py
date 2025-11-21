# tests/test_orders.py

from bot.basic_bot import BasicBot
from bot.config import settings


def test_market_order():
    bot = BasicBot(settings["API_KEY"], settings["API_SECRET"], testnet=True)

    # dry run with very low qty to avoid errors
    result = bot.place_market_order("BTCUSDT", "BUY", 0.001)

    print("\nTEST MARKET ORDER:")
    print(result)


def test_limit_order():
    bot = BasicBot(settings["API_KEY"], settings["API_SECRET"], testnet=True)

    result = bot.place_limit_order("BTCUSDT", "SELL", 0.001, 50000)

    print("\nTEST LIMIT ORDER:")
    print(result)

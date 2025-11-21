import argparse
import logging
import sys
from bot.basic_bot import BasicBot
from bot.config import API_KEY, API_SECRET

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/trading_bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--order_type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"])
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    bot = BasicBot(API_KEY, API_SECRET)

    if args.order_type == "MARKET":
        result = bot.place_market_order(args.symbol, args.side, args.quantity)

    elif args.order_type == "LIMIT":
        result = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)

    elif args.order_type == "STOP_LIMIT":
        result = bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)

    print("\nOrder Result:")
    print(result)

if __name__ == "__main__":
    main()

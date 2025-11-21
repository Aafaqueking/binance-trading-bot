import logging
from binance import Client, BinanceAPIException
from binance.enums import *
from typing import Dict

logger = logging.getLogger("TradingBot")

class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """Initialize trading bot"""
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            logger.info("Bot initialized successfully.")
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            raise e

    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict:
        try:
            logger.info(f"Market order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market order executed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Market order failed: {e.message}")
            return {"error": e.message}

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> Dict:
        try:
            logger.info(f"Limit order: {side} {quantity} {symbol} @ {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                price=price,
                quantity=quantity,
                timeInForce='GTC'
            )
            logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Limit order failed: {e.message}")
            return {"error": e.message}

    def place_stop_limit_order(self, symbol: str, side: str, quantity: float, price: float, stop_price: float) -> Dict:
        try:
            logger.info(f"Stop-Limit order: {side} {quantity} {symbol} @ {price}, stop {stop_price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='STOP',
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce='GTC'
            )
            logger.info(f"Stop-limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Stop-limit order failed: {e.message}")
            return {"error": e.message}

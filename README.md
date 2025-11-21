# A simple Python-based trading bot that allows you to place MARKET, LIMIT, and other order types on Binance Futures Testnet using command-line arguments.

---

 Features

* ✔ Binance Futures Testnet support
* ✔ Place Market, Limit, Stop orders
* ✔ Logging for every action
* ✔ Clean CLI flags (--symbol, --side, --quantity, etc.)
* ✔ Uses python-binance for secure API requests
* ✔ Fully modular project structure
* ✔ Error handling for notional limits, order failures, and API issues

---

 ## Project Structure


* trading-bot/
* │── main.py
* │── config.py
* │── bot/
* │     ├── __init__.py
* │     ├── basic_bot.py
* │     ├── cli.py
* │     ├── config.py
* │── logs/
* │── requirements.txt
* │── README.md


---

 Installation

1. Clone the repository

```bash
git clone https://github.com/Aafaqueking/binance-trading-bot.git
cd trading-bot
```

2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

 API Configuration

Open `config.py` and add your Testnet API keys:

```python
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_secret_key"
BASE_URL = "https://testnet.binancefuture.com"
```

You will see:

```
✓ config.py loaded successfully (Testnet API keys loaded).
```

---

 How to Run the Bot

Market Order Example

```bash
python main.py --symbol BTCUSDT --side BUY --quantity 0.002 --order_type MARKET
```

Limit Order Example

```bash
python main.py --symbol ETHUSDT --side SELL --quantity 0.01 --order_type LIMIT --price 2450
```

Available CLI Flags

Flag Meaning
* --symbol Trading pair (BTCUSDT, ETHUSDT, etc.)
* --side BUY / SELL
* --quantity Order quantity
* --order_type MARKET / LIMIT / STOP / STOP_MARKET
* --price Price (for LIMIT or STOP orders)

---

 Log Output Example

```
2025-11-21 13:18:56 - TradingBot - INFO - Market order executed: {
    'orderId': 10503611301,
    'symbol': 'BTCUSDT',
    'type': 'MARKET',
    'side': 'BUY'
}
```

---

 ### Notional Error Example (Common)

If order value < $100 (Binance minimum):

```
Order's notional must be no smaller than 100
```

Increase quantity.

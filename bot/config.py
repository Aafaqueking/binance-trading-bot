import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API Keys from .env file
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Binance Futures Testnet Base URL
BASE_URL = "https://testnet.binancefuture.com"

# ---- VALIDATION ----
if not API_KEY or not API_SECRET:
    raise ValueError(
        " API keys missing! Please create a .env file with API_KEY and API_SECRET.\n"
        "Example:\nAPI_KEY=your_key_here\nAPI_SECRET=your_secret_here"
    )

# Optional: Ensure no accidental spaces
API_KEY = API_KEY.strip()
API_SECRET = API_SECRET.strip()

# Optional safety check to avoid using real keys on testnet by mistake
if len(API_KEY) < 20 or len(API_SECRET) < 20:
    raise ValueError("Invalid API keys detected! Check your .env file.")

print("✓ config.py loaded successfully (Testnet API keys loaded).")

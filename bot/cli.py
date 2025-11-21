import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Buy or Sell')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--order_type', required=True,
                        choices=['MARKET', 'LIMIT', 'STOP_LIMIT'],
                        help='Type of order')
    parser.add_argument('--price', type=float, help='Limit price')
    parser.add_argument('--stop_price', type=float, help='Stop-limit stop price')

    return parser

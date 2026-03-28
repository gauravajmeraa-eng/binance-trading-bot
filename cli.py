import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.logging_config import setup_logging

def main():
    print("debug:script is running")
    setup_logging()
    client = get_client()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        logging.info(f"Sending {args.type} {args.side} order for {args.symbol}...")
        
        response = place_order(
            client, args.symbol, args.side, args.type, args.quantity, args.price
        )

        if response:
            logging.info(f"SUCCESS! Order ID: {response.get('orderId')}")
            print("\n--- Order Response ---")
            print(f"Status: {response.get('status')}")
            print(f"Avg Price: {response.get('avgPrice')}")
        
    except Exception as e:
        logging.error(f"FAILED: {str(e)}")

if __name__ == "__main__":
         main()
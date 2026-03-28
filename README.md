# Binance Futures Trading Bot
A Python CLI tool for executing market and limit orders on the Binance Testnet.
## Features
- Secure credential management via `.env`
- Real-time logging of order successes and failures
- Support for multiple symbols (e.g., BTCUSDT)
## Installation
`pip install -r requirements.txt`
##Quick Start Commands (for testing):

Market Order: python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005

Limit Order: python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 60000

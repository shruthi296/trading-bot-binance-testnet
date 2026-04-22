# Binance Futures Testnet Trading Bot

## Setup

1. Install Python 3.x

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create `.env` file:

```
API_KEY=your_key
API_SECRET=your_secret
```

## Run Examples

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Features

* Supports BUY and SELL orders
* Market and Limit orders
* Input validation
* Logging to file (bot.log)
* Error handling

## Assumptions

* Uses Binance Futures Testnet
* Only USDT-M pairs supported

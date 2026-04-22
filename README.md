\# Binance Futures Testnet Trading Bot



\## Setup



1\. Install Python 3.x



2\. Install dependencies:

&#x20;  pip install -r requirements.txt



3\. Create `.env` file:

&#x20;  API\_KEY=your\_key

&#x20;  API\_SECRET=your\_secret



\## Run Examples



\### MARKET Order



python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001



\### LIMIT Order



python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000



\## Features



\* Supports BUY and SELL orders

\* Market and Limit orders

\* Input validation

\* Logging to file (bot.log)

\* Error handling



\## Assumptions



\* Uses Binance Futures Testnet

\* Only USDT-M pairs supported




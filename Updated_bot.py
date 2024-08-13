import yfinance as yf
import pandas as pd
import numpy as np
import logging
import alpaca_trade_api as tradeapi
from datetime import datetime

#If you want to trade on paper trading follow this additional step

API_KEY = 'your_api_key_here'
SECRET_KEY = 'your_secret_key_here'
BASE_URL = 'https://paper-api.alpaca.markets'

# Create an instance of the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Download historical data
data = yf.download("AAPL", start="2022-01-01", end="2022-12-31")

def calculate_indicators(data):
    # Exponential Moving Averages
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    # Relative Strength Index
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

data = calculate_indicators(data)

def generate_signals(data):
    # Buy and Sell signals based on EMA and RSI
    data['Signal'] = 0
    buy_signal = (data['EMA_12'] > data['EMA_26']) & (data['RSI'] < 30)
    sell_signal = (data['EMA_12'] < data['EMA_26']) & (data['RSI'] > 70)
    data.loc[buy_signal, 'Signal'] = 1
    data.loc[sell_signal, 'Signal'] = -1
    data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')
    return data

data = generate_signals(data)

def backtest(data, initial_balance=10000):
    balance = initial_balance
    position = 0
    stop_loss = 0.95
    take_profit = 1.10
    entry_price = 0

    for i, row in data.iterrows():
        if row['Signal'] == 1 and balance != 0:
            position = balance / row['Close']
            balance = 0
            entry_price = row['Close']
            logging.info(f"BUY at {row['Close']} on {row.name.date()}")
        elif row['Signal'] == -1 and position != 0:
            balance = position * row['Close']
            position = 0
            logging.info(f"SELL at {row['Close']} on {row.name.date()}")
            entry_price = 0

        if position != 0:
            if row['Close'] <= entry_price * stop_loss:
                balance = position * row['Close']
                position = 0
                logging.info(f"STOP LOSS at {row['Close']} on {row.name.date()}")
            elif row['Close'] >= entry_price * take_profit:
                balance = position * row['Close']
                position = 0
                logging.info(f"TAKE PROFIT at {row['Close']} on {row.name.date()}")

    if position != 0:
        balance = position * data.iloc[-1]['Close']  # Close position at the last available price

    return balance

logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

final_balance = backtest(data)
print(f"Final Balance: ${final_balance:.2f}")


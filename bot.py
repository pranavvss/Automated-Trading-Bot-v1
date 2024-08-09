import yfinance as yf
import pandas as pd
import numpy as np
import logging

# Fetch historical data
data = yf.download("AAPL", start="2022-01-01", end="2022-12-31")

# Define the trading strategy
def moving_average_strategy(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['Signal'] = 0
    data['Signal'][50:] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1, 0)
    data['Position'] = data['Signal'].diff()
    return data

data = moving_average_strategy(data)

# Backtest the strategy
def backtest(data, initial_balance=10000):
    balance = initial_balance
    position = 0
    for i in range(len(data)):
        if data['Position'][i] == 1:
            position = balance / data['Close'][i]
            balance = 0
        elif data['Position'][i] == -1:
            balance = position * data['Close'][i]
            position = 0
    return balance

final_balance = backtest(data)
print(f"Final Balance: ${final_balance:.2f}")

# Set up logging
logging.basicConfig(filename='/home/pi/trading-bot/trading_bot.log', level=logging.INFO)

def log_trade(action, price):
    logging.info(f"{action} at {price}")

# Example usage
log_trade('BUY', 150.23)
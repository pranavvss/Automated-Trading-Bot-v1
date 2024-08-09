# Algorithmic-Automated-Trading-Bot-on-Raspberry-Pi
Developed and deployed an algorithmic trading bot that runs 24/7 on a Raspberry Pi. The bot implements a simple moving average crossover strategy to trade stocks and cryptocurrencies. The project involved data fetching, strategy implementation, backtesting, and automation.
------------------------------------------------------------------------------------------
### Key Features:

Automated Trading: The bot can execute trades based on predefined strategies without manual intervention. Backtesting: Historical data is used to test and optimize the trading strategy. Real-time Data: Integration with APIs to fetch real-time market data. 24/7 Operation: Hosted on a Raspberry Pi to ensure continuous operation.
------------------------------------------------------------------------------------------
### Tools and Technologies Used:

Programming Language: Python.

Python Libraries: Pandas, NumPy, Matplotlib, yfinance, ta, ccxt, alpaca-trade-api.

Hardware: Raspberry Pi 4, Mini sd card 16gb + (suggested), USB 2.0 card reader.

[Picture of Raspberry Pi 4](https://assets.raspberrypi.com/static/raspberry-pi-4-labelled-f5e5dcdf6a34223235f83261fa42d1e8.png)

[Picture of USB 2.0 card reader](https://www.kalitut.com/wp-content/uploads/2020/05/raspberry-pi-cardreader-1.jpg)

[Picture of Mini sd card](https://robu.in/wp-content/uploads/2019/08/sandisk-32-gb-card.jpg)

Software: Raspbian OS, SSH, cron jobs. 

APIs: Yahoo Finance (yfinance) for stock data, CCXT for cryptocurrency data, Alpaca API for stock trading
------------------------------------------------------------------------------------------
### Detailed Explanation:

1. Setup and Configuration: Installed Raspbian OS on a Raspberry Pi and set up the necessary environment. Enabled SSH for remote access and installed required Python libraries.

2. Data Fetching: Utilized yfinance to download historical stock data. Used ccxt to fetch real-time cryptocurrency data from various exchanges.

3. Strategy Implementation: Implemented a simple moving average crossover strategy. Calculated short-term (50-day) and long-term (200-day) moving averages. Generated buy/sell signals based on the crossover points.

4. Backtesting: Developed a backtesting framework to evaluate the strategy against historical data. Simulated trades and calculated final balance to assess performance. Automation:

5. Created a shell script to start the bot and configured it to run at system boot using cron jobs. Ensured 24/7 operation by hosting the bot on the Raspberry Pi. Logging and Monitoring:

6. Implemented logging to record all trading actions and decisions. Set up log monitoring to track the bot’s performance and actions in real-time.

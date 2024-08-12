# Automated Trading Bot on Raspberry Pi 

>[!NOTE]
>For intermediate Python programmers.

>[!NOTE]
>Must read this whole Document.
------------------------------------------------------------------------------------------

>ABOUT THIS PROJECT -
>I Developed and deployed an algorithmic trading bot that runs 24/7 on a Raspberry Pi. The bot implements a simple moving average crossover strategy to trade stocks and cryptocurrencies. The project involved data fetching, strategy implementation, backtesting, and automation. Once you are able to understand this you can expand on this by adding more advanced strategies, risk management techniques, and real-time data analysis.

------------------------------------------------------------------------------------------

**About Raspberry pie -**

Unlike any Arduino models, you dont have to connect raspberry pie to a computer/laptop, because technically raspberry pie is a computer in itself. It has multiple pins You can connect your mouse, keyboard and monitor to the raspberry pi directly, it uses a quad kit micro processor, it has upto 8 gb of ram, built in wifi and bluetooth, 4 usb ports, Micro SD card and much more. We can also run our trading bot on a cloud server, where you buy a cloud service and upload and run your code on a cloud server for 24/7, Cloud servers on one hand can be costly becuase you'll have to purchase them every month while Raspberry pie could be a one time investment. Think of it as a very small computer that can easily run our python program 24/7.

![raspberry-pi-4-labelled-f5e5dcdf6a34223235f83261fa42d1e8](https://github.com/user-attachments/assets/8883085d-8a9e-4550-b74f-be2318cd04cd)

------------------------------------------------------------------------------------------

>[!WARNING]
>I highly recommend that you test your bot on paper trading(Fake Money).

------------------------------------------------------------------------------------------
**Key Features:**

- Automated Trading: The bot can execute trades based on predefined strategies without manual intervention. 
- Backtesting: Historical data is used to test and optimize the trading strategy. 
- Real-time Data: Integration with APIs to fetch real-time market data. 
- 24/7 Operation: Hosted on a Raspberry Pi to ensure continuous operation.

------------------------------------------------------------------------------------------
> [!IMPORTANT]
>Tools and Technologies Used:

- Programming Language: Python.
- Python Libraries: Pandas, NumPy, Matplotlib, yfinance, ta, ccxt, alpaca-trade-api.
- Hardware: Raspberry Pi 4, Mini sd card 16gb + (suggested), USB 2.0 card reader.

[Picture of Raspberry Pi 4](https://assets.raspberrypi.com/static/raspberry-pi-4-labelled-f5e5dcdf6a34223235f83261fa42d1e8.png)

[Picture of USB 2.0 card reader](https://www.kalitut.com/wp-content/uploads/2020/05/raspberry-pi-cardreader-1.jpg)

[Picture of Mini sd card](https://robu.in/wp-content/uploads/2019/08/sandisk-32-gb-card.jpg)

- Software: Raspbian OS, SSH, cron jobs. 
- APIs: Yahoo Finance (yfinance) for stock data, CCXT for cryptocurrency data or (If you want to trade in forex, ill suggest ForexConnect API- Provided by OANDA), Alpaca API for stock trading.

[yfinance Documentation](https://pypi.org/project/yfinance/)

[CCXT Documentation](https://docs.ccxt.com/#/)

------------------------------------------------------------------------------------------
**Detailed Explanation:**

1. Setup and Configuration: Installed Raspbian OS on a Raspberry Pi and set up the necessary environment. Enabled SSH for remote access and installed required Python libraries.

   [Quick tutorial on Raspbian Setup](https://www.youtube.com/watch?v=CQtliTJ41ZE)
   
   [Detailed Documentation on Raspbian Setup by Raspberry pie](https://www.raspberrypi.com/documentation/computers/getting-started.html)

   <img src="https://github.com/user-attachments/assets/2def3fe8-2c89-4403-9a62-8e4428283a1a" width="600" />
   
3. Data Fetching: Utilized yfinance to download historical stock data. Used ccxt to fetch real-time cryptocurrency data from various exchanges.
4. Strategy Implementation: Implemented a simple moving average crossover strategy. Calculated short-term (50-day) and long-term (200-day) moving averages. Generated buy/sell signals based on the crossover points.
5. Backtesting: Developed a backtesting framework to evaluate the strategy against historical data. Simulated trades and calculated final balance to assess performance. Automation:
6. Created a shell script to start the bot and configured it to run at system boot using cron jobs. Ensured 24/7 operation by hosting the bot on the Raspberry Pi. Logging and Monitoring:
7. Implemented logging to record all trading actions and decisions. Set up log monitoring to track the bot’s performance and actions in real-time.

------------------------------------------------------------------------------------------
**SETUP BELOW**
------------------------------------------------------------------------------------------

**Step 1 (Get the Hardware Ready)**

Step 1.1 Setting up Raspberry Pi (Get the Hardware Ready)
- Raspberry Pi (preferably model 4)
- MicroSD card (at least 16GB)
- Power supply
- Monitor, keyboard, and mouse (for initial setup)
- Ethernet cable (Preffered) or Wi-Fi connection

Step 1.2. Install Raspbian OS
- Download the Raspbian OS image from the [official Raspberry Pi website](https://www.raspberrypi.com/software/operating-systems/)
  
  [Detailed Tutorial on Raspbian Setup](https://www.youtube.com/watch?v=wvxCNQ5AYPg)
  
- Use a tool like [Etcher](https://etcher.download/) to write the image to your microSD card.
- Insert the microSD card into the Raspberry Pi and connect the power supply, monitor, keyboard, and mouse.
- Follow the on-screen instructions to complete the setup.

Step 1.3. Update Your System - Open a terminal on your Raspberry Pi (you can find it in the main menu) and run this command
```
sudo apt-get update
sudo apt-get upgrade
```

Step 1.4. Enable SSH for Remote Access (run the following command in the terminal)
```
sudo raspi-config
```

Step 1.5. Find Your Raspberry Pi’s IP Address (in terminal paste this code and press enter, once you get the ip adress note it somehwere)
```
ifconfig
```
------------------------------------------------------------------------------------------

**## Step 2 (Setting Up Your Development Environment)**

Step 2.1 SSH into Your Raspberry Pi from Your Main Computer
- Open a terminal (Mac/Linux) or cmd (w admin permissions)(Windows).
- Connect to your Raspberry Pi using its IP address
``` 
ssh pi@<Raspberry_Pi_IP_Address>
```
You may be asked a password, bydeafult is 'raspberry'.

Step 2.2 Install Python and its Libraries
- In the SSH terminal paste these commands
```
sudo apt-get install python3 python3-pip
pip3 install pandas numpy matplotlib yfinance ta ccxt alpaca-trade-api
```
------------------------------------------------------------------------------------------

**Step 3 Coding our Trading Bot**

Step 3.1 Create a Directory(Folder) for Your Trading Bot
- In terminal run this command to make a new directory and open it  
```
mkdir trading-bot
cd trading-bot
```

Step 3.2 Create a Python File for Your Bot
- In termianl run
```
nano bot.py # replace 'bot' with any name you want, Nano is not a name, Nano is a text editor.
```
Then

1. Import Libraries
```python
import yfinance as yf
import pandas as pd
import numpy as np
import logging

```
Explanation - 
yfinance: A Python library to download historical market data from Yahoo Finance. 
pandas: Used for data manipulation and analysis.
numpy: A library for numerical operations. It is used here to perform element-wise conditions.
logging: Used to log messages (like trades made during the whole day) to a file for future tracking.

------------------------------------------------------------------------------------------ 

2. Fetch Historical Data
```python
data = yf.download("AAPL", start="2022-01-01", end="2022-12-31")
```
Explanation - This line fetches historical stock price data for Apple Inc. (AAPL) from January 1, 2022, to December 31, 2022.


------------------------------------------------------------------------------------------  

3. Defining the Trading Strategy

```python
def moving_average_strategy(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['Signal'] = 0
    data['Signal'][50:] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1, 0)
    data['Position'] = data['Signal'].diff()
    return data

```
Explanation - 
- Simple Moving Averages - The code calculates two moving averages from the closing prices—SMA over 50 days and 200 days. 

[(Read Documentation on SMA by geeksforgeeks)](https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/) 

[(Read Documentation on SMA by Gregorycernera Medium)](https://gregorycernera.medium.com/computing-simple-moving-average-sma-with-python-pandas-yfinance-0458bb0b5d3b)

- Signal: This is a binary indicator (1 or 0). A '1' signal is generated when the 50-day SMA crosses above the 200-day SMA.
- Position: Indicates a change in the signal (buy or sell). If the signal changes from 0 to 1, it suggests buying. If from 1 to 0, it suggests selling.

------------------------------------------------------------------------------------------  

4. Backtesting the Strategy

```python
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
```
Explanation - This function simulates trading based on the signals. It starts with an initial balance (e.g., 10,000 INR ). It buys stocks when the signal is to buy (position=1) and sells all when the signal is to sell (position=-1). The final balance after processing all signals is returned.

------------------------------------------------------------------------------------------  

5. Calculate Final Balance
```python
final_balance = backtest(data)
print(f"Final Balance: ${final_balance:.2f}")
```
Explanation - Executes the backtest and prints out the final balance after following the trading strategy. (How much did we gain, or loose will be adjusted in our final balance which will be rounded of to two 2 float values (upto 2 decimals)

------------------------------------------------------------------------------------------  

6. Setup Logging
```python
logging.basicConfig(filename='/home/pi/trading-bot/trading_bot.log', level=logging.INFO)
```
Explanation - Configures the logging system to write informational messages into a file named trading_bot.log.

------------------------------------------------------------------------------------------ 

- Remember to press enter to save this file.
- You may exit Nano editor now.

------------------------------------------------------------------------------------------ 

**Step 4 Automating and Running our Bot 24/7**

Step 4.1 Create a Shell Script to Start Your Bot (in terminal run)
```
nano start_bot.sh
```
- Copy and paste the following content into start_bot.sh
```
#!/bin/bash
cd /home/pi/trading-bot
python3 bot.py
```
- save and exit.
- Now run this command to make our script executable

```
chmod +x start_bot.sh
```

Step 4.2 Set Up a Cron Job to Run our Bot at Boot
- In the SSH terminal, run
```
crontab -e
```
- Add the following line at the end of the file to run the script at reboot
```
@reboot /home/pi/trading-bot/start_bot.sh
```
- save and exit

Step 4.3 Reboot Your Raspberry Pi
- In the SSH terminal, run
```
sudo reboot
```
------------------------------------------------------------------------------------------  

## Step 5 Monitor the bot's activity
- After rebooting, SSH back into your Raspberry Pi
- Check the logs to ensure your bot is running
```
tail -f /home/pi/trading-bot/trading_bot.log (Edit the command!! Make sure to add file name of your bot)

```
------------------------------------------------------------------------------------------  


>[!NOTE]
>We are done. Make sure you trade on paper tarding(Fake Money). Use real Money to trade with this bot on your own risk. This is posted only for education purpose and should be used for that only.

>[!NOTE]
>If you like more content like this, Read my [Automated-Trading-Bot-No-hardware-required](https://github.com/pranavvss/Automated-Trading-Bot-No-hardware-required) to learn how to make a automated trading bot using python language and deploying our code on a cloud server and trade on it 24/7. (If you follow this method you won't have to buy any raspberry pi or any other hardware for deploying your code, we will only use a laptop and a 1 year free AWS subscription(if you have'nt yet made a account on AWS).


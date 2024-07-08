import yfinance as yf
import pandas as pd
import talib
import matplotlib.pyplot as plt

# Download historical stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

# Calculate Moving Average
data['MA20'] = talib.SMA(data['Close'], timeperiod=20)

# Calculate Relative Strength Index (RSI)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

# Calculate Bollinger Bands
data['UpperBand'], data['MiddleBand'], data['LowerBand'] = talib.BBANDS(data['Close'], timeperiod=20)

# Plot the results
plt.figure(figsize=(14, 7))

# Plot closing price and MA
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price')
plt.plot(data['MA20'], label='20-Day SMA', color='orange')
plt.title(f'{ticker} Close Price and 20-Day SMA')
plt.legend()

# Plot RSI
plt.subplot(3, 1, 2)
plt.plot(data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.title(f'{ticker} Relative Strength Index')
plt.legend()

# Plot Bollinger Bands
plt.subplot(3, 1, 3)
plt.plot(data['Close'], label='Close Price')
plt.plot(data['UpperBand'], label='Upper Band', color='red')
plt.plot(data['MiddleBand'], label='Middle Band', color='blue')
plt.plot(data['LowerBand'], label='Lower Band', color='green')
plt.title(f'{ticker} Bollinger Bands')
plt.legend()

plt.tight_layout()
plt.show()

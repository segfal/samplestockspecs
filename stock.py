import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


import matplotlib
import datetime as dt
import urllib.request
import json
import yfinance as yf


##interface for stock data


class Stock_Data:
    def __init__(self,ticker) -> None:
        self.ticker = yf.Ticker(ticker)
        self.price = self.ticker.history(period='max')
        self.min_date = self.price.index.min()
        self.max_date = self.price.index.max()
        self.volume = self.price['Volume']
        self.open = self.price['Open']
        self.close = self.price['Close']
        self.high = self.price['High']
        self.low = self.price['Low']
        



TSLA = Stock_Data('TSLA')
print(TSLA.price)
        

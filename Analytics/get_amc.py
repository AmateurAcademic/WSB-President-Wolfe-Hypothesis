import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime


def calculate_change(start, end):
    return round(((end - start)/start)*100, 2)


def get_change(symbol, date):

    return calculate_change(yf.Ticker(symbol).history(start=date, end=date)["Open"].to_list()[0], yf.Ticker(symbol).history(start=date, end=date)["Close"].to_list()[-1])


date_str =  str(20210105)
date = datetime(year=int(date_str[0:4]), month=int(date_str[4:6]), day=int(date_str[6:8]))

print(date)
print (get_change("AMC", date))
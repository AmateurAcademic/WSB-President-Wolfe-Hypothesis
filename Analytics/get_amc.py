import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta
import os
from contextlib import closing
import shutil
import requests

# THE list to track
symbols = ["GME", "AMC", "BB", "TSLA", "PLTR", "NOK", "TLRY", "SNDL", "AAPL", "MSFT"]
# days to look back
lookback_days = 15


def calculate_change(start, end):
    return round(((end - start)/start)*100, 2)


def get_change(symbol, date):
    start_of_day = yf.Ticker(symbol).history(start=date, end=date)["Open"].to_list()[0]
    end_of_day = yf.Ticker(symbol).history(start=date, end=date)["Close"].to_list()[-1]
    return calculate_change(start_of_day, end_of_day)

def getDataFromDate(start_date):
    day_to_be_scraped = start_date
    today = datetime.today()
    days_without_data = []
    
    bx_url = 'ftp://ftp.nasdaqtrader.com/files/shortsaledata/daily/bx/NQBXshvol'
    psx_url = 'ftp://ftp.nasdaqtrader.com/files/shortsaledata/daily/psx/NPSXshvol'
    finra_url = 'http://regsho.finra.org/CNMSshvol'
    
    if (not os.path.isdir('B')):
        os.mkdir('B')
    if (not os.path.isdir('P')):
        os.mkdir('P')
    if (not os.path.isdir('F')):
        os.mkdir('F')

    while (day_to_be_scraped <= today):
        filename = (day_to_be_scraped).strftime('%Y%m%d') + '.txt'
        try:

            # must be done with requests. 403 Forbidden otherwise
            # TODO: clean the files that are failed http requests
            finra_query = requests.get(finra_url+filename)
            with open('F/'+filename, 'wb') as outfile:
                outfile.write(finra_query.content)


            with closing(request.urlopen(bx_url+filename)) as bx_query:
                with open('B/'+filename, 'wb') as f:
                    shutil.copyfileobj(bx_query, f)

            with closing(request.urlopen(psx_url+filename)) as psx_query:
                with open('P/'+filename, 'wb') as f:
                    shutil.copyfileobj(psx_query, f)


        except:
            print('no data for '+ filename)

            #kinda hacky
            days_without_data +=[filename]


        day_to_be_scraped += timedelta(days=1)
        
    return days_without_data




today = datetime.today()
day_to_be_scraped = today - timedelta(days=lookback_days)

files_to_be_removed = getDataFromDate(day_to_be_scraped)

# clean finra files that have no data
for finra_file in files_to_be_removed:
    os.remove('F/'+finra_file)





# TODO filter out only the interesting symbols

# TODO add together the files to 1 dataframe



day_to_be_scraped = today - timedelta(days=lookback_days)

while (day_to_be_scraped <= today):
    filename = (day_to_be_scraped).strftime('%Y%m%d') + '.txt'

    Bvol_df = pd.read_csv('B/'+filename, sep='|', header=0)
    Bvol_df['date'] =  pd.to_datetime(Bvol_df['Date'], errors='coerce', format='%Y%m%d')

    Fvol_df = pd.read_csv('F/'+filename, sep='|', header=0)
    Fvol_df['date'] =  pd.to_datetime(Fvol_df['Date'], errors='coerce', format='%Y%m%d')

    Pvol_df = pd.read_csv('P/'+filename, sep='|', header=0)
    Pvol_df['date'] =  pd.to_datetime(Pvol_df['Date'], errors='coerce', format='%Y%m%d')


    date_str =  str(Bvol_df['Date'][0])
    date = datetime(year=int(date_str[0:4]), month=int(date_str[4:6]), day=int(date_str[6:8]))


    one_day_change = []

    for symbol in symbols:
        try:
            one_day_change.append(get_change(symbol, date))
        except:
            one_day_change.append(np.nan)


    day_to_be_scraped += timedelta(days=1)
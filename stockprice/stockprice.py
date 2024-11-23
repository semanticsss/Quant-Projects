import yfinance as yf
import pandas as pd
import requests
from io import StringIO
import streamlit as st

nasdaq_tickers_url = "https://raw.githubusercontent.com/datasets/nasdaq-listings/refs/heads/main/data/nasdaq-listed.csv"


def access_data(ticker_symbol, period):

    ticker_symbol = ticker_symbol.upper()
    ticker_data_req = requests.get(nasdaq_tickers_url)
    reader = pd.read_csv(StringIO(ticker_data_req.text))
    # st.write(reader)
    # st.write(type(reader))
    for _, row in reader.iterrows():
        if row['Symbol'] == ticker_symbol:
            ticker = yf.Ticker(ticker_symbol)
            historical = ticker.history(period=period)
            st.write(historical)
            st.write(historical)
            return historical
    return None
        
    

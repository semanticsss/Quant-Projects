import streamlit as st
import yfinance as yf
import stockprice as stock

st.title("historical stock price visualizer")

ticker = st.chat_input("Stock ticker?")
# st.write(type(ticker))
# st.write(ticker)
with st.sidebar:
    st.title('specifications')
    period = st.segmented_control('period', ['day', 'month', 'year'])
if ticker != None:
    st.write(stock.access_data(ticker, period))








import streamlit as st
import yfinance as yf
import stockprice as stock

st.title("historical stock price visualizer")

ticker = st.text_input("Stock ticker?")
def get_data(ticker, period):
    st.write(stock.access_data(ticker, period))
# st.write(type(ticker))
# st.write(ticker)
with st.sidebar:
    st.title('specifications')
    segment = st.selectbox('period', ['1d','1mo','1y'])
    period = segment
if ticker != None:
    get_data(ticker, period)








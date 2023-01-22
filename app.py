import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

### Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# define the ticker symbol
tickerSymbol = 'RY.TO'

st.markdown(f'* Stock price : {tickerSymbol}*')

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2011-09-27', end='2020-09-26')

# Open High Low Close Volumne Dividends Stock Splits

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)

# Markdown cheatsheet
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

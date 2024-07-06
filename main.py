import json
import openai
import pandas as pd
import matplotlib.pyplot as plot
import streamlit as sl
import yfinance as yf

openai.api_key = open('API_Key', 'r').read()

# assumes chatgpt knows
def getStockPrice(ticker):
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)

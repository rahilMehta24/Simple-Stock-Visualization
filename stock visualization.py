import streamlit as st 
import yfinance as yf 
import pandas as pd 
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


# Heading 
st.write(
    """
    # Simple Stock Price App 
    """
)



def todayDate():
    """ 
    geting today date 
    """
    today = date.today()
    return today


def yearsOld(year):
    """
    geting years back date from today 
    """
    start = datetime.now() - relativedelta(years=int(year))
    return start


def plot():
    companysStock_name = stockName().strip()
    start_date = yearsOld(userInput())
    today_date = todayDate()
    #The Ticker module, which allows you to access ticker data in a more Pythonic way
    stockData = yf.Ticker(companysStock_name)
    stockDataFrame = stockData.history(period = '1d', start = start_date ,end = today_date)
    st.write("From:",str(start_date)[0:10],'To',str(today_date))
    st.write(" ### Close ")
    st.line_chart(stockDataFrame.Close)
    st.write(" ### Volume")
    st.line_chart(stockDataFrame.Volume)

# side bar 
def stockName():
    companysStock_name = st.sidebar.text_input("Enter the Company's Stock Name")
    return companysStock_name
def userInput():
    #st.sidebar.write("### Years ago  ")
    year = st.sidebar.slider('From ____ years ago ',1,15,5)
    return year




st.sidebar.write("# User input")
plot()

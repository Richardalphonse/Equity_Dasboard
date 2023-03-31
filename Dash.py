import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
st.title("NSE Dashboard")

uploadedFile = st.file_uploader("choose a file", type=[
                                'csv', 'xlsx'], accept_multiple_files=False, key="fileUploader")

# Check if a file was uploaded
if uploadedFile is not None:
    # Read the uploaded file into a Pandas DataFrame

    df2 = pd.read_csv(uploadedFile)

    def line_plot():
        df2 = pd.read_csv('10-11-2022-TO-07-02-2023TCSALLN.csv')
        df2['Date'] = pd.to_datetime(df2['Date'])
        fig = px.line(df2, x=df2['Date'], y=df2['Open Price'],title="Tcs Equity ")
        fig.add_scatter(x=df2['Date'], y=df2['High Price'])
        return fig

    fig2 = line_plot()

    st.plotly_chart(fig2, use_container_width=True)

    def candle_plot():
        fig = go.Figure(data=[go.Candlestick(x=df2['Date'],
                                             open=df2['Open Price'],
                                             high=df2['High Price'],
                                             low=df2['Low Price'],
                                             close=df2['Close Price'])])
        return fig

    fig3 = candle_plot()
    st.plotly_chart(fig3, use_container_width=True)

    def moving_avergae_plot():
        df2["SMA_Close_Price"] = df2['Close Price'].rolling(
            10, min_periods=1).mean()
        df2['Date'] = pd.to_datetime(df2['Date'])
        fig = px.line(df2, x=df2['Date'], y=df2['Open Price'],title="TCS SMA")
        fig.add_scatter(x=df2['Date'], y=df2['High Price'])
        fig.add_scatter(x=df2['Date'], y=df2['SMA_Close_Price'])
        return fig

    fig4 = moving_avergae_plot()
    st.plotly_chart(fig4, use_container_width=True)

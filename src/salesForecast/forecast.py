
# Import libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset
from io import StringIO
import os

def forecastSales(start_date, end_date):
    
    # Get the absolute data path
    data_path = os.path.abspath('data/forecast.csv') 
    # Load the dataset
    df = pd.read_csv(data_path)
    # print(df.head(5))
    
    ## Cleaning up the data
    df.columns=["Month","Sales"]
    
    ## Drop last 2 rows
    df.dropna(axis=0,inplace=True)
    # Convert Month into Datetime
    df['Month']=pd.to_datetime(df['Month'])
    df.set_index('Month',inplace=True)
    
    # Differencing
    df['Sales First Difference'] = df['Sales'] - df['Sales'].shift(1)
    df['Sales'].shift(1)
    df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)
    df.dropna(axis=0, inplace=True)
    # print(df.head())
    
    # Building the model
    model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
    results = model.fit()
    
    # Testing the model 
    # df['forecast']=results.predict(start=80,end=103,dynamic=True)
    # df[['Sales','forecast']].plot(figsize=(12,8))
    # plt.show()
    
    # Extending date for future prediction
    # Make prediction to 2030
    future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,700)]
    future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
    
    # print(future_datest_df.tail())
    
    # concatinating the extended data with the dataframe
    future_df=pd.concat([df,future_datest_df])
    
    # Forecasting the future sales
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    future_df['forecast'] = results.predict(start = start_date, end = end_date, dynamic=True)  
    
    fig = plt.figure(figsize=(12,8))
    plt.plot(future_df[['Sales', 'forecast']])
    plt.ylabel('Annual Total Sales', color='red')
    plt.xlabel('Year', color='red')
    plt.legend(['Sales', 'Forecast']) 
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    graph = imgdata.getvalue()
    # plt.show()
    return graph

# forecastSales()
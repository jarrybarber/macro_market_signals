import numpy as np
import pandas as pd
import fredapi
import yfinance as yf

from dotenv import load_dotenv
import os

from .common import FRED_INDICATORS, TICKERS



def load_fred_data(observation_start='1995-01-01'):
    load_dotenv()
    fred = fredapi.Fred(api_key=os.getenv('FRED_API_KEY'))

    df = pd.DataFrame({
        name: fred.get_series(series_id, observation_start=observation_start)
            for name, series_id in FRED_INDICATORS.items()
    })

    df.index = df.index.normalize()

    return df


def load_yfinance_data(start_date = "1995-01-01"):
    dfs = {}
    for name, ticker in TICKERS.items():
        # Load all ticker info
        df = yf.Ticker(ticker).history(start=start_date)
        
        # Index currently made of date and time, let's remove time and timezone info
        # This will make it easier to merge with the FRED data
        df.index = df.index.tz_localize(None).normalize()
        
        # Save df
        dfs[name] = df
        
    return dfs


if __name__ == "__main__":
    pass
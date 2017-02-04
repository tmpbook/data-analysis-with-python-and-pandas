import quandl
import pandas as pd
import pickle

api_key = open('../02-Building_dataset/quandlapikey.txt', 'r').read()

def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df = df.resample('M').mean()

    df.columns = ['M30']
    return df

def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"] - df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df = df.resample('M')
    print(df.head())
    df.rename(columns={'Adjusted Close': 'sp500'}, inplace=True)
    print(df.head())
    df = df['sp500']
    return df

if __name__ == '__main__':
    pass
    # M30 = mortgage_30y()
    # HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')
    print(sp500_data())
    # state_HPI_M30 = HPI_data.join(M30)
    # print(state_HPI_M30.corr()['M30'].describe())

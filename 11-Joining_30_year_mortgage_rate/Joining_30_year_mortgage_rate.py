import quandl
import pandas as pd
import pickle

api_key = open('quandlapikey.txt', 'r').read()

def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df = df.resample('M').mean()

    df.columns = ['M30']
    return df

if __name__ == '__main__':
    M30 = mortgage_30y()
    HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')

    state_HPI_M30 = HPI_data.join(M30)
    print(state_HPI_M30.corr()['M30'].describe())

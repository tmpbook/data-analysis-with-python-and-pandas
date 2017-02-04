import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')
HPI_data['TX2'] = HPI_data['TX'] * 2
print(HPI_data[['TX', 'TX2']])
print(HPI_data[['TX', 'OH']].corr())
print(HPI_data[['TX', 'OH']].corr().describe())

HPI_data_pct_change = HPI_data.pct_change()
print(HPI_data_pct_change)

HPI_data_pct_change.plot()
plt.legend().remove()
plt.show()

api_key = open('../02-Building_dataset/quandlapikey.txt', 'r').read()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={'Value': "United States"}, inplace=True)
    return df

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

benchmark = HPI_Benchmark()
benchmark.plot(ax=ax1, color='k', linewidth=10)

plt.legend().remove()
plt.show()

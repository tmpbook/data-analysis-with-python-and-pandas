import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
print(HPI_data[['TX', 'TX1yr']])

# UNCOMMENT ONE BY ONE

# 1
# drop colume if one NaN in it
HPI_data.dropna(inplace=True)
print(HPI_data[['TX', 'TX1yr']])

# 2
# # `bfill` = backforward
# # `ffill` = forward
# HPI_data.fillna(method='bfill', inplace=True)
# print(HPI_data[['TX', 'TX1yr']])

# 3
# # Also can fill a value whatever you want
# HPI_data.fillna(value=-99999, limit=10, inplace=True)
# print(HPI_data[['TX', 'TX1yr']])

# count top 20 column which `isnull() = True`
print(HPI_data.head(20).isnull().values.sum())

HPI_data[['TX', 'TX1yr']].plot(ax=ax1)
plt.legend(loc=4)
plt.show()

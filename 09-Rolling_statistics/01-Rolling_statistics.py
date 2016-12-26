import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')

# 1
HPI_data['TX12MA'] = HPI_data['TX'].rolling(center=False, window=12).mean()

# 2
# HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)
# # FutureWarning: pd.rolling_std is deprecated for Series and will be removed in a future version, replace with
# # Series.rolling(center=False,window=12).std()

HPI_data['TX12STD'] = HPI_data['TX'].rolling(center=False, window=12).std()


print(HPI_data[['TX', 'TX12MA', 'TX12STD']])

HPI_data[['TX', 'TX12MA']].plot(ax=ax1)
HPI_data['TX12STD'].plot(ax=ax2)
plt.legend(loc=4)
plt.show()

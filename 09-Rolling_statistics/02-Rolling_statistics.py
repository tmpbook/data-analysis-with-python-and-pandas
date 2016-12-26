import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')
TX_AK_12corr = HPI_data['TX'].rolling(window=12).corr(other=HPI_data['AK'])

HPI_data['TX'].plot(ax=ax1, label='TX HPI')
HPI_data['AK'].plot(ax=ax1, label='AK HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

plt.legend(loc=4)
plt.show()

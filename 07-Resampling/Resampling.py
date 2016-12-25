import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

HPI_data = pd.read_pickle('../05-Pickling/fiddy_states.pickle')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

# More alias in README.md
HPI_resample_year_end = HPI_data['TX'].resample('A').mean()
# HPI_resample_year_end = HPI_data['TX'].resample('A').ohlc()

HPI_data['TX'].plot(ax=ax1, legend="Mouthly TX HPI")
HPI_resample_year_end.plot(ax=ax1, legend="Yearly TX HPI")
plt.legend(loc=4)
plt.show()

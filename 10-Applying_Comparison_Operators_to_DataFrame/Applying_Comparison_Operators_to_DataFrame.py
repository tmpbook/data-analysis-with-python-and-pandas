import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

bridge_height = {'meters': [10.26, 10.31, 10.27, 10.22, 10.33, 6212.42, 10.28, 10.25, 10.31]}

df = pd.DataFrame(bridge_height)
df['STD'] = df['meters'].rolling(window=2, center=False).std()
print(df)

df_std = df.describe()['meters']['std']
print(df_std)

df = df[(df['STD'] < df_std)]
print(df)

df['meters'].plot()
plt.show()

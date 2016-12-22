import pandas as pd

df = pd.read_csv('ZILL-Z77006_MPC.csv')
print(df.head())

df = pd.read_csv('ZILL-Z77006_MPC.csv', index_col=0)
print(df.head())

df.columns = ['Median_Price_Cut']
print(df.head())
df.to_csv('newcsv.csv')
df.to_csv('newcsv_no_header.csv', header=False)

df = pd.read_csv('newcsv_no_header.csv', names=['Date', 'Median_Price_Cut'], index_col=0)
print(df.head())

df.to_html('table.html')

df = pd.read_csv('newcsv_no_header.csv', names=['Date', 'Median_Price_Cut'])
print(df.head())

df.rename(columns={'Median_Price_Cut': '77006_MPC'}, inplace=True)
print(df.head())
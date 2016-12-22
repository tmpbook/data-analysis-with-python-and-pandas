import pandas as pd

df1 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55]
}, index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [7, 8, 9, 6],
    'US_GDP_Thousands': [50, 55, 65, 55]
}, index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [7, 8, 9, 6],
    'Low_tier_HPI': [50, 52, 50, 53]
}, index=[2001, 2002, 2003, 2004])

# single column
# print(pd.merge(df1, df2, on='HPI'))

# multipal columns
# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3, on='Int_rate', how='left', lsuffix='_left', rsuffix='_right')
print(joined)

print("------")

df4 = pd.DataFrame({
    'Year': [2001, 2002, 2003, 2004],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55]
})

df5 = pd.DataFrame({
    'Year': [2000, 2001, 2002, 2003],
    'Int_rate': [7, 8, 9, 6],
    'US_GDP_Thousands': [50, 55, 65, 55]
})

# `how='inner'` is the default
merged = pd.merge(df4, df5, on='Year')
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4, df5, on='Year', how='left')
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4, df5, on='Year', how='right')
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4, df5, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4, df5, on='Year', how='inner')
merged.set_index('Year', inplace=True)
print(merged)

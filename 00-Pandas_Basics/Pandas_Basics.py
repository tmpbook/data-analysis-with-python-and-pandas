# coding:utf8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [43, 53, 34, 45, 64, 34],
    'Bounce_Rate': [65, 72, 62, 64, 54, 66]
}

df = pd.DataFrame(web_stats)

# <class 'pandas.core.frame.DataFrame'>
print(type(df))
print(df)
print(df.head(2))
print(df.tail(2))

# 设置默认索引
df.set_index('Day', inplace=True)
print(df.head())

# 取指定列
print(df['Visitors'])
# 属性的方式访问
print(df.Visitors)
# 取指定多列
print(df[['Bounce_Rate', 'Visitors']])

print(df.Visitors.tolist())

# <class 'numpy.ndarray'>
print(type(np.array(df)))

# <class 'numpy.ndarray'> to <class 'pandas.core.frame.DataFrame'>
numpy__ndarray_type = np.array(df)
df2 = pd.DataFrame(numpy__ndarray_type)
print(df2)

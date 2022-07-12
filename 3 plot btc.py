import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read data
read_data = pd.read_csv('BCHAIN-MKPRU.csv')

# dataframe
df = pd.DataFrame(read_data)

# print(df.info)
# sort
df.sort_index(ascending=False)

# convert data to datetime
df['Date'] = pd.to_datetime(df['Date'],format ='%Y-%m-%d')

# fig
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
# define x and y
x = df['Date']
y = df['Value']

# plot 0
# x and y axis name
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Price')
axes[0].set_title('BTC/USD Price Line Plot')
axes[0].plot(x,y,lw = 1,label='BTC/USD')

# plot 1
# x and y axis name
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Price')
axes[1].set_title('BTC/USD Price Bar Plot')
axes[1].bar(x,y,lw = 0.7,label='BTC/USD Bar Plot')

# layout fix
plt.autoscale()
plt.tight_layout()

# label legend
axes[0].legend(loc=2)
axes[1].legend(loc=2)


plt.show()


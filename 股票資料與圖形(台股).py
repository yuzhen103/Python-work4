#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd


# In[2]:


start_date = '1990-01-01'
end_date = '2023-03-03'


# In[3]:


ticker = "AMZN"


# In[4]:


data = yf.download(ticker, period = '10y', interval = '1d')


# In[5]:


data.head()


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


data['Adj Close'].plot(figsize = (10,7))
plt.title("Adjusted Close Price of %s" % ticker, fontsize = 16)
plt.ylabel("Price", fontsize = 14)
plt.xlabel("year", fontsize = 14)
plt.grid(which = 'major', color = 'k', linestyle = '-.', linewidth = 0.5)
plt.show()


# In[8]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


tickers_list = ["1201.TW", "1216.TW", "1236.TW"]


# In[10]:


data = pd.DataFrame(columns = tickers_list)


# In[11]:


for ticker in tickers_list:
    data[ticker] = yf.download(ticker, period = "10y", interval = "1d")['Adj Close']


# In[12]:


data.plot(figsize = (10, 7))
plt.legend()
plt.title("Adjusted Close Price", fontsize = 16)
plt.ylabel("Price", fontsize = 14)
plt.xlabel("Year", fontsize = 14)
plt.grid(which = 'major', color = 'k', linestyle = '-.', linewidth = 0.5)
plt.show()


# In[ ]:





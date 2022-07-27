#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


url = "https://www.tashiara.com/search/max-results=7?q=Fashion+Trends"


# In[4]:


req = requests.get(url)


# In[5]:


content = BeautifulSoup(req.content, 'html.parser')


# In[9]:


data = content.find_all('div',{'class':'thumb'})


# In[11]:


links = []
trend = []
start_link = "https://www.tashiara.com"


# In[ ]:


for items in data:
    rest_link = items.find('a')['href']
    name = items.find('font', attrs={'class':'retitle'})
    trend.append(name.text)
    links.append(start_link+rest_link)


# In[ ]:


dataframe = {'Latest in Trends':trend, 'Links':}
Final_dataframe = pd.DataFrame(dataframe)
print(Final_dataframe)


# In[ ]:


Final_dataframe.to_csv('fk_data_url.csv')


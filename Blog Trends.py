import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.tashiara.com/search/max-results=7?q=Fashion+Trends"
req = requests.get(url)
content = BeautifulSoup(req.content, 'html.parser')
data = content.find_all('div',{'class':'thumb'})

links = []
trend = []
start_link = "https://www.tashiara.com"

for items in data:
    rest_link = items.find('a')['href']
    name = items.find('font', attrs={'class':'retitle'})
    trend.append(name.text)
    links.append(start_link+rest_link)

dataframe = {'Latest in Trends':trend, 'Links':}
Final_dataframe = pd.DataFrame(dataframe)
print(Final_dataframe)

Final_dataframe.to_csv('fk_data_url.csv')
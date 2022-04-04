import requests
import pandas as pd

url = 'https://www.naehrwertrechner.de/naehrwerte/C133000/Hafer+Flocken'

html = requests.get(url).content
df_list = pd.read_html(html)

#for table_index in range(10): #there are 10 tables on the website
#    table = df_list[table_index].to_numpy

table_index = 9

df = df_list[table_index]
print(df.to_numpy)
#df.to_csv('my data.csv')
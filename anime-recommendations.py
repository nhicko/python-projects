'''
USING JIKAN API FOR MYANIMELIST
'''
import requests
import json

url = "https://api.jikan.moe/v4/recommendations/anime"

response = requests.get(url)
data = response.json()

# print(data['data'][1]['entry'][0]['title'])

data_lst = []
data_lst = data['data']

for i in data_lst:
    for x, y in i.items():
        if x == 'entry':
            print(y[0]['url'] + "," + y[0]['title'])

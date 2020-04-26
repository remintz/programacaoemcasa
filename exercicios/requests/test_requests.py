import requests
import json
from matplotlib import pyplot as plt 
from matplotlib.dates import date2num
import datetime

r = requests.get('https://corona-api.com/countries?include=timeline')
print(r.status_code)
data = json.loads(r.text)
for d in data['data']:
    country = d['name']
    timeline = d['timeline']
    deaths = {}
    for t in timeline:
        date = t['date']
        deaths[date] = t['deaths']
    x = []
    for date in deaths.keys():
        x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
    y = deaths.values()
    # x = [date2num(datetime.datetime.strptime(date, '%Y-%m-%d')) for date in deaths.keys()]
    # y = [value for value in deaths.values()]

    plt.figure(figsize=(10, 10))
    plt.plot_date(x, y, 'r-o')
    # plt.plot(x, y, 'r-o')
    # plt.set_xticks(x)
    # plt.set_xticklabels([date.strftime('%Y-%m-%d') for date in deaths.keys()])
    plt.savefig('out.pdf')
    # print(deaths)
    break

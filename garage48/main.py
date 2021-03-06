from bs4 import BeautifulSoup as BS
import requests as rq
from garage48 import country, tools
import json

url = "http://garage48.org/hackthecrisis/?fbclid=IwAR2B8USw8Vf99Nemf3kqDA1PG8gDzRYqUXQb_gmkiwPERJgvhzrSGCIgiwQ"

res = rq.get(url)
soup = BS(res.content, 'lxml')
events = soup.findAll('div', {"class": "gr-event"})


def parse_event(e):
    infolist = e.findAll('div', 'gr-flex')
    title = str.strip(e.find('h4', {"class": "gr-event__title"}).text)
    img = e.find('div', {"class": "gr-event__image"})
    c = infolist[1].find('strong').text
    img_url = tools.parse_bg_image(img['data-bg'])

    # det_url = img.find('a')['href']

    country_id = country.match_country_id(c)
    data = {
        "name": title,
        "logo_url": img_url,
        "country_id": country_id
    }

    return data


l = []
for event in events:
    e = parse_event(event)
    l.append(e)

target = json.dumps(l)

f = open('output/group_list.json', 'w')
f.write(target)
f.close()
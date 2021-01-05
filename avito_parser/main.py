from lxml import html
import requests
import pandas as pd
from datetime import datetime as dt



header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
          ' Chrome/87.0.4280.88 Safari/537.36'}

main_link = 'https://www.avito.ru'

def reguets_avito():

    response = requests.get(main_link, headers=header)
    root = html.fromstring(response.text)
    items = root.xpath('//div[@class="styles-list-2HFYr"]/div[@data-marker]')

    list_items = []
    i = len(items)

    for item in items:
        i -= 1

        dict_items = {}
        dict_items['title'] = str(item.xpath("//span[contains(@itemprop,'name')]/text()")[i])
        dict_items['link'] = main_link + str(item.xpath('//div[@class="styles-titleRow-2eBLq"]//a/@href')[i])
        dict_items['price'] = item.xpath('//span/meta[@itemprop="price"]/@content')[i].replace('...', 'Не указано')

        list_items.append(dict_items)

    return list_items

def to_csv(data):

    df = pd.DataFrame(data)
    time = dt.now().isoformat("-").split(".")[0].replace(":", "-")
    df.to_csv(f'{time}_avito.csv',encoding='utf-8')


avito_data = reguets_avito()
to_csv(avito_data)
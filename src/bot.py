import requests
import json


def find_item(item):
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    html = requests.get(url=url)
    output = json.loads(html.text)
    print(output['products_and_categories'])


find_item(None)

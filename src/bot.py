import requests
import json


def find_item(name):
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    for category in output['products_and_categories']:
        for item in output['products_and_categories'][category]:
            if name in item['name']:
                print(item['name'])
                print(item['id'])
                return item['id']


# Type the item name inside find the exact item
find_item('Cargo Pant')

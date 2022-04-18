
import requests
import json


def find_item(name):
    # find a specific item
    # Insert the URL below of the json data of the website you want to get an item from
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    for category in output['products_and_categories']:
        for item in output['products_and_categories'][category]:
            if name in item['name']:
                print(item['name'])
                print(item['id'])
                # Use the ID printed to find all the info about the specific item by typing in 'www.supremenewyork.com/shop/{id}' to your browser.
                return item['id']


def get_color(item_id, color, size):
    # find specific color of the item found above
    url = f'https://www.supremenewyork.com/shop/{item_id}.json'
    html = requests.get(url=url)
    output = json.loads(html.text)
    # print(output)

    for product_color in output['styles']:
        if color in product_color['name']:
            for product_size in product_color['sizes']:
                if size in product_size['name']:
                    return product_color['id']


if __name__ == '__main__':
    item_id = find_item('Cargo Pant')
    # after the item_id add color you want followed by the size
    color_id = get_color(item_id, 'Orange', '34')
    print(color_id)


import requests
import json


def find_item(name):
    # Find an item of a store and print name and id
    # Use .json url of all items for whatever site is being searched
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    # Enter the category that contains all the items of the store
    for category in output['products_and_categories']:
        for item in output['products_and_categories'][category]:
            if name in item['name']:
                print('Selected Item: ' + item['name'])
                print('Item ID: ' + str(item['id']))
                return item['id']


def get_color(item_id, color, size):
    # Get the color and id of the item selected
    url = f'https://www.supremenewyork.com/shop/{item_id}.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    # Enter sub category of item chosen to further filter resutls
    for product_color in output['styles']:
        if color in product_color['name']:
            for product_size in product_color['sizes']:
                if size in product_size['name']:
                    return product_color['id']


# # Type the item name inside find the exact item
# find_item('Cargo Pant')

if __name__ == '__main__':
    item_id = find_item('Cargo Pant')
    color_id = get_color(item_id, 'Olive', '30')
    print('Color ID: ' + str(color_id))

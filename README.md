# Supreme Bot

### Description

> This is a program that is designed to find specific items inside a webstore and display/access all the info pertaining to that item.

> The full bot has not been created yet, this program is only 2 methods to access information from the webstores json data.

## How to Run the Program for a Specific Item of Supreme

1. > Check the url in Line 9 and find the name of the item

   - https://www.supremenewyork.com/mobile_stock.json
     <img width="1181" alt="Screen Shot 2022-04-19 at 1 16 42 PM" src="https://user-images.githubusercontent.com/77586218/164059570-a038e2ee-c43d-4d6c-bfaf-51c0b0e569d4.png">

<br/>

2. > Enter the name of the item in Line 41

   - item_id = find_item('Small Box Sweatpant')

<br/>

3. > Run the program and the Item ID will be printed in the console

   - Selected Item: Small Box Sweatpant
   - Item ID: 174981

<br/>

4. > Take the Id and paste it into the url from Line 24 and view it in the browser

   - https://www.supremenewyork.com/shop/{item_id}.json
   - https://www.supremenewyork.com/shop/174981.json
     <img width="1190" alt="Screen Shot 2022-04-19 at 1 19 20 PM" src="https://user-images.githubusercontent.com/77586218/164059966-da80b0c8-c204-4cf5-8ee8-2f81842e6736.png">

<br/>

5. > Determine which color and size the specific item is. Add that info to Line 43

   - color_id = get_color(item_id, 'Grey', 'Small')

<br/>

6. > Run the pgrogram again and the item, item id, and the color id will be printed in the console for future use.

   - <img width="327" alt="Screen Shot 2022-04-19 at 1 23 14 PM" src="https://user-images.githubusercontent.com/77586218/164060480-7f3c35aa-5d43-4eb9-967b-74441f1585de.png">

---

---

---

## How to Set up the Methods for Other Sites (Not Supreme)

1. > First, find the url that has all the json data from the specific webstore (This is already completed for Supreme)

   - Supreme - https://www.supremenewyork.com/mobile_stock.json

<br/>

2. > Enter that in the 'find_item' method as the 'url' variable, line 9 (This is already completed for Supreme)

   - url = 'https://www.supremenewyork.com/mobile_stock.json'

<br/>

3. > Go to that link in the browser and determine the category of items that will be searched and enter that on line 14 and 15 (This is already completed for Supreme)

   - for category in output['products_and_categories']:
   - for item in output['products_and_categories']

 <br/>

4. > Adjust Lines 16-19 to match the keys from the json data viewed in the browser to the appropriate lines (This is already completed for Supreme)

<br>

5. > Enter the url for the 'get_color' method so that the 'item_id' variable will be dynamically called, Line 24 (This is already completed for Supreme)

   - url = f'https://www.supremenewyork.com/shop/{item_id}.json'

<br/>

6. > Check the subcategory of the item by following the link with id of the item inserted to determine the key for the subcategory, Line 29 (This is already completed for Supreme)

   - for product_color in output['styles']:

<br/>

7. > Adjust Lines 30-33 to match the keys from the json data viewed in the browser to the appropriate lines (This is already completed for Supreme)

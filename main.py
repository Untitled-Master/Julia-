import requests
from bs4 import BeautifulSoup

url = 'https://www.jumia.com.dz/flash-sales/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a', class_='core')

    for item in items:
        brand_name = item.get('data-ga4-item_brand', 'N/A')
        category = item.get('data-gtm-category', 'N/A')
        item_id = item.get('data-ga4-item_id', 'N/A')

        item_name_tag = item.find('h3', class_='name')
        item_name = item_name_tag.text if item_name_tag else 'N/A'

        img_div = item.find('div', class_='img-c')
        img_tag = img_div.find('img') if img_div else None
        img_link = img_tag.get('data-src', 'N/A') if img_tag else 'N/A'

        stars_div = item.find('div', class_='stars _s')
        star_rating = stars_div.text.strip() if stars_div else 'N/A'

        price_tag = item.find('div', class_='prc')
        price = price_tag.text if price_tag else 'N/A'

        output = f"""
Item Details: {item_id}
-------------
Item Name: {item_name}
Brand Name: {brand_name}
Category: {category}
Star Rating: {star_rating}
Price: {price}
Image Link: {img_link}
-------------
        """
        print(output)

else:
    print("Failed to retrieve the webpage")

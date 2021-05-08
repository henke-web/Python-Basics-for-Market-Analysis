import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

cats = soup.find_all(class_='nav nav-list')

for categor in cats:
    for a in categor.find_all('a', href=True):
        links = (a['href'])
        all_links = links.replace('index.html', '').replace('catalogue/category/books_1/', '')
        full_link_page = 'http://books.toscrape.com/' + all_links + 'index.html'

        next_page = requests.get(full_link_page)
        next_soup = BeautifulSoup(next_page.content, 'html.parser')

        books = next_soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        for book in books:
            book_url = book.find('a')
            find_product_url = book_url.get('href')

            if 'catalogue' not in find_product_url:

                partial_product_url = find_product_url.split('/')
                split_partial_product_url = partial_product_url[3]
                product_page_url = 'http://books.toscrape.com/catalogue/' + split_partial_product_url + '/index.html'

                product_page = requests.get(product_page_url)
                product_soup = BeautifulSoup(product_page.content, 'html.parser')

                title = product_soup.find('h1').get_text()

                divs = product_soup.find_all('tr')
                upc = (divs[0].get_text().replace('UPC', '')).replace('\n', '')
                price_excl_tax = (divs[2].get_text().replace('Price (excl. tax)', '')).replace('\n', '')
                price_incl_tax = (divs[3].get_text().replace('Price (incl. tax)', '')).replace('\n', '')
                tax = (divs[4].get_text())
                in_stocks = (divs[5].get_text().replace('Availability', '').replace('In stock ', '')).replace('\n', '')
                Number_reviews = (divs[6].get_text())

                descri = product_soup.find_all('p')
                product_description = (descri[3].get_text())

                category = next_soup.find('h1').get_text()

                product_main = product_soup.find(class_='col-sm-6 product_main')
                all_p = product_main('p')
                ptag = (all_p[-1])
                star_rating = ptag.get('class')

                image_url = product_soup.find('img')
                image_src = image_url.get('src').split('../')
                partial_image_url = image_src[2]
                full_image_url = 'http://books.toscrape.com/' + partial_image_url

                all_page_url = f'Product page url: {product_page_url}'
                all_upc = f'UPC: {upc}'
                all_title = f'Title: {title}'
                all_price_with_tax = f'Price Incl Tax: {price_incl_tax}'
                all_price_no_tax = f'Price Excl Tax: {price_excl_tax}'
                all_stocks = f'Availability: {in_stocks}'
                full_description = f'Product description: {product_description}'
                all_category = f'Category: {category}'
                all_rating = f'Star rating: {star_rating}'
                img_url = f'Img url: {full_image_url}''\n'

                with open('toscrape.csv', mode='a+', encoding='utf-8') as product_file:
                    product_writer = csv.writer(product_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    product_writer.writerow(
                        [all_page_url, all_upc, all_title, all_price_with_tax, all_price_no_tax, all_stocks, full_description, all_category, all_rating,
                         full_image_url])

                    print(all_page_url)
                    print(all_upc)
                    print(all_title)
                    print(all_price_with_tax)
                    print(all_price_no_tax)
                    print(all_stocks)
                    print(full_description)
                    print(all_category)
                    print(all_rating)
                    print(img_url)

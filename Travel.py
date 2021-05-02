import requests
from bs4 import BeautifulSoup
import csv


page = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
soup = BeautifulSoup(page.content, 'html.parser')


books = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    book_url = book.find('a')
    find_product_url = book_url.get('href').split('/')
    partial_product_url = find_product_url[3]
    product_page_url = 'http://books.toscrape.com/catalogue/' + partial_product_url + '/index.html'

    product_page = requests.get(product_page_url)
    product_soup = BeautifulSoup(product_page.content, 'html.parser')

    title = product_soup.find('h1').get_text()

    divs = product_soup.find_all('tr')
    upc = (divs[0].get_text().replace('UPC', '')).replace('\n', '')
    Price_excl_tax = (divs[2].get_text().replace('Price (excl. tax)', '')).replace('\n', '')
    Price_incl_tax = (divs[3].get_text().replace('Price (incl. tax)', '')).replace('\n', '')
    tax = (divs[4].get_text())
    In_stocks = (divs[5].get_text().replace('Availability', '').replace('In stock ', '')).replace('\n', '')
    Number_reviews = (divs[6].get_text())

    descri = product_soup.find_all('p')
    product_description = (descri[3].get_text())


    category = soup.find('h1').get_text()

    product_main = product_soup.find(class_='col-sm-6 product_main')
    all_p = product_main('p')
    ptag = (all_p[-1])
    Star_rating = ptag.get('class')

    image_url = product_soup.find('img')
    image_src = image_url.get('src').split('../')
    partial_image_url = image_src[2]
    full_image_url = 'http://books.toscrape.com/' + partial_image_url

    Page_url = f'Product page url: {product_page_url}'
    UPC = f'UPC: {upc}'
    Title = f'Title: {title}'
    Price_with_tax = f'Price Incl Tax: {Price_incl_tax}'
    Price_no_tax = f'Price Excl Tax: {Price_excl_tax}'
    Availability = f'Availability: {In_stocks}'
    Description = f'Product description: {product_description}'
    Category = f'Category: {category}'
    Stars = f'Star rating: {Star_rating}'
    img_url = f'Img url:{full_image_url}'

    with open('Fullpage.csv', mode='a+') as product_file:
        product_writer = csv.writer(product_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


        product_writer.writerow([Page_url, UPC, Title, Price_with_tax, Price_no_tax, Availability, Description, Category, Stars, full_image_url, ])

#    print(Page_url)
#    print(UPC)
#    print(Title)
#    print(Price_with_tax)
#    print(Price_no_tax)
#    print(Availability)
#    print(Description)
#    print(Category)
#    print(Stars)
#    print(img_url)










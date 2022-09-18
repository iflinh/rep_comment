# C:\Users\DELL\Desktop\Python
import time
from bs4 import BeautifulSoup

from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.etsy.com/search?q=shirt');

source = driver.page_source
print(source)
exit()
soup = BeautifulSoup(source, 'html.parser')
print(soup)
type_soup = type(soup)
pr(f'type soup = {type_soup}')

data = soup.find_all("h3", class_='v2-listing-card__title')

for i in data:
    title = i.text
    link = i.parent.parent.parent['href']
    price = i.parent.find("span", class_='currency-value').text + 'đ'
    print(title)
    print(link)
    print(price)

driver.quit()


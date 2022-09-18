import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome('chromedriver')

info_all = [] #vì nhiều trang nên ở ngoài
for p in range(1,2):
    print(f'Đang làm việc ở trang thứ {p}')
    driver.get(f'https://www.etsy.com/search?q=shirt&ref=pagination&page={p}');

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find_all("h3", class_='v2-listing-card__title')

    # info_all = [] ở trong khi chỉ 1 trang
    for i in data:
        long_title = i.text
        title = (long_title.split('\n                        '))[1].split('\n                ')[0]
        long_link = i.parent.parent.parent['href']
        id_listing = (long_link.split('https://www.etsy.com/listing/'))[1].split('/')[0]
        link = 'https://www.etsy.com/listing/' + id_listing
        price = i.parent.find("span", class_='currency-value').text + 'đ'
        # long_review = i.parent.find("span", class_='
        #                      wt-text-caption 
                            
        #                 wt-text-gray wt-display-inline-block
        #                  wt-nudge-l-3 wt-pr-xs-1').text
        # review = (long_title.split(''))[1].split('\n                ')[0]
        info = {
            'link' : link,
            'title' : title,
            'price' : price
        }
        info_all.append(info)

driver.quit()
# print(info_all)
print('So ao la: ',len(info_all))

df = pd.DataFrame(info_all)
file_name = 'info_all2.csv'
df.to_csv(file_name, index = True)

# to excel
read_file = pd.read_csv ('info_all2.csv')
read_file.to_excel ('info_excel2.xlsx', index = None, header=True)
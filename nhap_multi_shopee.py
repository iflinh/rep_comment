import time
import threading
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def open_chrome_1(n_page):
    driver = webdriver.Chrome('chromedriver')
    # driver.maximize_window()#full màn hình

    driver.set_window_size(1360, 600)#kích thước màn hình lấy ở trang selenium.dev
    driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang selenium.dev
    info_all_1 = []
    for p in range(0, n_page):
        link_first = f'https://shopee.vn/search?keyword=d%C3%A9p&page={p}'
        # driver.execute_script("document.body.style.zoom='50%'")
        driver.get(link_first);

        # js_zoom_in = "document.body.style.zoom='1.7'"
        # driver.execute_script(js_zoom_in)
        js_zoom_out = "document.body.style.zoom='0.10'"
        driver.execute_script(js_zoom_out)#Zoom to lấy code ở trang: https://pythonmana.com/2021/11/20211125073454264A.html

        time.sleep(4)

        def scroll_chrome():#Function scroll
            for i in range(3):
                driver.execute_script(f"window.scrollTo(0, {i+1}*300)")
                time.sleep(2)#3s scroll 1 time
                print(f'scroll = {i+1}')

        scroll_chrome()

        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        data = soup.find_all("div", class_="ie3A+n bM+7UW Cve6sh")
        print(len(data))

        #lấy dữ liệu
        for i in data:
            title = i.text
            long_link = 'https://shopee.vn' + i.parent.parent.parent.parent.parent.parent['href']
            link = long_link[:long_link.index('?sp_atk=')]#Lấy từ đầu đến vị trí của cụm từ: '?sp_atk'
            print(link)
            place = i.parent.parent.parent.find("div", class_='zGGwiV').text
            print(f'place = {place}')
            sold_text = i.parent.parent.parent.find("div", class_='r6HknA').text#Ở đây gặp lỗi là tìm class: 'r6HknA uEPGHT' mà class này chỗ có chỗ không nên .text không được, chỗ không bán được thì chỉ có class: 'r6HknA' nên search này mới được, nếu bỏ class kia nnos sẽ ra lỗi:'NoneType' object has no attribute: 'text' Error in Python, lỗi này sửa được nhờ xem trang này: https://nsikakimoh.com/blog/fix-nonetype-object-has-no-attribute-text 
            #đoạn .text này khó làm vì lỗi không phải chỗ nào cũng có class này mà .text, nên phải tìm xem class đó có đủ 60 không
            # print(f'sold_text = {sold_text}')
            # print(f'sold_text[-1] = {sold_text[-1]}')
            if sold_text:#sold_text == True hay là khác rỗng
                if sold_text[-1]=='k':
                    sold_num = sold_text.replace('Đã bán ', '').replace(',', '.').replace('k','')
                    sold = int(float(sold_num)*1000)
                else:
                    sold = int(float(sold_text.replace('Đã bán ', "")))
                print(f'sold = {sold}')

                # link = i.parent.parent.parent['href']
                # price = i.parent.find("span", class_='currency-value').text + 'đ'
                # print(title)
                # print(link)
                # print(price)
            else:#sold_text == False là rỗng(không bán được)
                sold = 0
                print(f'sold = {sold}')
            info = {
                'link' : link,
                'title' : title,
                # 'price' : price
                'place' : place
            }
            info_all_1.append(info)

        # data = soup.find_all("div", data-sqe="link")
        # print(f'data class "" = {data}')
    driver.quit()

n_page = 4
open_chrome_1(n_page)

# Câu hỏi, nếu def 1 hàm thôi, thì file excel xuất ra sẽ cùng tên phải làm sao để kết nối 3 excel lại 1 hoặc làm sao để đổi tên file



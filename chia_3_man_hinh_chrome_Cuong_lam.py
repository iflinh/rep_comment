import threading
import time
from selenium import webdriver
import pyautogui

screenWidth, screenHeight = pyautogui.size()

w_one_display = 300
h_one_display = 500

# Define a function for the thread
def mot(link, content, postion ):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(postion, 0)#vị trí màn hình lấy ở trang selenium.dev
    driver.set_window_size(200, 400)#kích thước màn hình lấy ở trang selenium.dev
    print(content)
    driver.get(f'{link}')
    time.sleep(60)

itm = ['https://shopee.vn/search?keyword=d%C3%A9p&page=1', 'https://shopee.vn/search?keyword=hoa&page=1','https://shopee.vn/search?keyword=xe&page=1']
thread = []
postion = 0
for i in itm:
    thread += [threading.Thread(target = mot, args = (i,"content", postion,))]
    postion += w_one_display 

for t in thread:
    t.start()

time.sleep(135)

# t1.join()
# t2.join()
# t3.join()

# MB:3619051998:
# ten: Nguyen chi Cuong
# 10: 1.6tr
#lấy dữ liệu
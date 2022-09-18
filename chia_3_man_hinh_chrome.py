import threading
import time
from selenium import webdriver

# Define a function for the thread
def mot(a):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang selenium.dev
    driver.set_window_size(360, 768)#kích thước màn hình lấy ở trang selenium.dev
    print('ben trai')
    driver.get(f'{a}');
    time.sleep(60)

def hai(b):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(360, 0)#kích thước màn hình lấy ở trang selenium.dev
    driver.set_window_size(360, 768)#kích thước màn hình lấy ở trang selenium.dev
    print('o giua')
    driver.get(f'{b}');
    time.sleep(60)

def ba(c):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(720, 0)#kích thước màn hình lấy ở trang selenium.dev
    driver.set_window_size(360, 768)#kích thước màn hình lấy ở trang selenium.dev
    print('ben phai')
    driver.get(f'{c}');
    time.sleep(60)

a = 'https://shopee.vn/search?keyword=d%C3%A9p&page=1'
b = 'https://shopee.vn/search?keyword=hoa&page=1'
c = 'https://shopee.vn/search?keyword=xe&page=1'

t1 = threading.Thread(target = mot, args = (a,))
t2 = threading.Thread(target = hai, args = (b,))
t3 = threading.Thread(target = ba, args = (c,))

t1.start()
t2.start()
t3.start()

time.sleep(135)

# t1.join()
# t2.join()
# t3.join()
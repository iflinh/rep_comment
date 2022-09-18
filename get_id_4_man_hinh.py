# f = open("id_comment_csv.csv",'r',encoding = 'utf-8')
# for i in range(4):
#     a = f.readlines(1:3)
#     print (f'Nội dung dòng {i+1}:',(a))
#     # b = f.readline()
#     # print ('Nội dung dòng 2: ', (b))
#     # c = f.readline()
#     # print ('Nội dung dòng 3: ', (c))
#     # d = f.readline()
#     # print ('Nội dung dòng 4: ', (d))
from concurrent.futures import thread
import threading
import time
from selenium import webdriver
import pyautogui
l = 2#input số luồng
link = 'https://www.google.com/search?q='#input
#.....................................................
#.....................................................
screenWidth, screenHeight = pyautogui.size()

#mở file lấy ID comment
f = open("id_comment_csv.csv",'r',encoding = 'utf-8')
id_out = []
for i in range(4):#Hàm for này là để lấy mấy dòng trong file
    a = int(f.readline().strip())
    id_out.append(a)#id_out là id đã lấy ra, sau này khỏi trùng
    print (f'Nội dung dòng {i+1}:',(a))

#Mở đa luồng:
# Define a function for the thread
def mot(link, content, w, h, x, y):
    driver = webdriver.Chrome('chromedriver')
    driver.set_window_position(x, y)#vị trí màn hình lấy ở trang selenium.dev
    driver.set_window_size(w, h)#kích thước màn hình lấy ở trang selenium.dev
    print(content)
    link_new = 'https://www.google.com/search?q='+ str(link)
    driver.get(f'{link_new}')
    time.sleep(2)

thread = []
if l < 4:
    thread_up = l#số luồng trên bằng l
    height_up = screenHeight
    print(f'screenHeight = {screenHeight}')
    with_up = screenWidth/thread_up
    postion_y_up = 0#có thể thay vào trực tiếp nhưng mình muốn để vậy để giống bên dưới l>3
    for i in range(l):
        thread += [threading.Thread(target = mot, args = (i,"in ra ABC", with_up, height_up, i*with_up, postion_y_up))]

else:#l>=4
    thread_up = l//2#số luồng trên
    thread_down = l - thread_up#số luồng dưới
    height_up = screenHeight/2#chiều cao cửa sổ trên
    with_up = screenWidth/thread_up#chiều rộng cửa sổ trên
    height_down = height_up#chiều cao cửa sổ dưới bằng chiều cao cửa sổ trên
    with_down = screenWidth/thread_down#chiều rộng bên dưới
    postion_y_up = 0#vị trí y của cửa sổ trên
    postion_y_down = screenHeight/2#vị trí y của cửa sổ dưới
    for j in range(l//2):
        thread += [threading.Thread(target = mot, args = (j,"in ra ABC", with_up, height_up, j*with_up, postion_y_up))]
        
    for j in range(l - l//2):
        thread += [threading.Thread(target = mot, args = (l//2 + j,"in ra ABC", with_down, height_down, j*with_down, postion_y_down))]
        
#chạy đa luồng
for t in thread:
    t.start()

time.sleep(5)
# print('x')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

ser = Service(r"C:/Users/DELL/Desktop/Python/chromedriver")
driver = webdriver.Chrome(service=ser)

# driver.maximize_window()#Max window: https://www.selenium.dev/documentation/webdriver/browser/windows/
driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
driver.set_window_size(1366, 500)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
time.sleep(15) # Let the user actually see something!

driver.quit()
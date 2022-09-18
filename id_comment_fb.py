from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
driver.get('https://www.facebook.com/');
time.sleep(5) # Let the user actually see something!
txt_User = driver.find_element_by_id('email')

txt_User.send_keys('abcxyz')
#
# search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

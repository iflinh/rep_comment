from operator import index
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
from selenium.webdriver.common.by import By
from login_fb_class import Login_fb
full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'

i = Login_fb(full_2fa, teardown=False)
i.go_driver()
time.sleep(2) # Let the user actually see something!

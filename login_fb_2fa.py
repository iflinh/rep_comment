from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
driver.get('https://www.facebook.com/');
time.sleep(5) # Let the user actually see something!

#Đây là 2 fb mẫu, thường mua fb nó có dạng UID|PASS|2FA có chỗ thì UID|PASS|2FA|Cookie|Email|PassEmail|... tùy chỗ bán
#100079633475311|r4DdyaYq65w3u|CWYG RUKA LFI3 AXEA OK2N GGF4 6YKK 7XUF
#100079562139644|b3X9caHwQD51P|FTGI HWBP NIZZ HQX5 SXEV XALL VXBM FYB5

full_2fa = '100079562139644|b3X9caHwQD51P|FTGI HWBP NIZZ HQX5 SXEV XALL VXBM FYB5'#yêu cầu phải dạng UID|pass|2fa    không có gạch đứng hay gì cuối 2FA, mỗi cái cách nhau gạch đứng

class Get_id:
  def __init__(self, full_2fa):
    self.uid = full_2fa[: full_2fa.index('|')]
    self.un_uid = full_2fa.replace(self.uid + '|', '')
    self.upass = self.un_uid[: self.un_uid.index('|')]
    self.u_2fa = self.un_uid.replace(self.upass + '|', '')

i = Get_id(full_2fa)#i là Class Get_id từ string UID|PASS|2FA
fb_id = i.uid#id facebook
fb_pass = i.upass#pass facebook
fb_2fa = i.u_2fa#mã 2FA
fb_2fa = fb_2fa.replace(' ','')#mã 2FA xóa dấu cách

#tim vi tri uid, pass:
id_User = driver.find_element('id', 'email')#vi tri email
pass_User = driver.find_element('id', 'pass')#vi tri pass
#input uid, pass:
id_User.send_keys(fb_id)#nhap uid
pass_User.send_keys(fb_pass)#nhap pass
pass_User.send_keys(Keys.ENTER)#bam Enter
time.sleep(15) # Let the user actually see something!

#Chuyển sang trang nhập OTP 6 số của 2FA:
code_box = driver.find_element('id', 'approvals_code')#vi tri nhap 2FA
import pyotp#thu vien lay 2FA
totp = pyotp.TOTP(fb_2fa)#khong hieu(code copy)
now_2fa = totp.now()#OTP now
code_box.send_keys(now_2fa)#nhập mã OTP 6 số vào code box
code_box.send_keys(Keys.ENTER)
driver.find_element('id','checkpointSubmitButton').click()

#Đoạn này nếu đăng nhập sai quốc gia nó nghi ngờ thì hỏi mình để khẳng định lại 3 lần
if driver.find_element('id', 'checkpointSubmitButton'):# nếu có nút check
    driver.find_element('id', 'checkpointSubmitButton').click()
    if driver.find_element('id', 'checkpointSubmitButton'):  # nếu có nút check
        driver.find_element('id', 'checkpointSubmitButton').click()
        driver.find_element('id', 'checkpointSubmitButton').click()

#đóng chrome:
driver.quit()
#Câu hỏi: làm sao cuộn thanh nhỏ bên trong nếu có nhiều thanh cuộn
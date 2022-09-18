from operator import index
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
from selenium.webdriver.common.by import By

class Login_fb():
    def __init__(self, full_2fa, teardown=False):
        self.teardown = teardown#Thêm teardown để ngăn trình duyệt tự tắt sau khi xong theo link: https://stackoverflow.com/questions/72090951/how-to-avoid-selenium-driver-closing-automatically
        self.uid = full_2fa[: full_2fa.index('|')]
        self.un_uid = full_2fa.replace(self.uid + '|', '')
        self.upass = self.un_uid[: self.un_uid.index('|')]
        self.u_2fa = self.un_uid.replace(self.upass + '|', '')

        # i = Get_id(full_2fa)#i là Class Get_id từ string UID|PASS|2FA
        self.fb_id = self.uid#id facebook
        self.fb_pass = self.upass#pass facebook
        self.fb_2fa = self.u_2fa#mã 2FA
        self.fb_2fa = self.fb_2fa.replace(' ','')#mã 2FA xóa dấu cách
    
    def go_driver(self):
        driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
        driver.get('https://www.facebook.com/');
        time.sleep(2) # Let the user actually see something!
        driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
        driver.set_window_size(1366, 768)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
        #tim vi tri uid, pass:
        id_User = driver.find_element('id', 'email')#vi tri email
        pass_User = driver.find_element('id', 'pass')#vi tri pass
        #input uid, pass:
        id_User.send_keys(self.fb_id)#nhap uid
        pass_User.send_keys(self.fb_pass)#nhap pass
        pass_User.send_keys(Keys.ENTER)#bam Enter
        time.sleep(2) # Let the user actually see something!

        #Chuyển sang trang nhập OTP 6 số của 2FA:
        code_box = driver.find_element('id', 'approvals_code')#vi tri nhap 2FA
        import pyotp#thu vien lay 2FA
        totp = pyotp.TOTP(self.fb_2fa)#khong hieu(code copy)
        now_2fa = totp.now()#OTP now
        code_box.send_keys(now_2fa)#nhập mã OTP 6 số vào code box
        code_box.send_keys(Keys.ENTER)
        driver.find_element('id','checkpointSubmitButton').click()

        if driver.current_url != 'https://www.facebook.com/':#nếu lỗi đăng nhập khác quốc gia, phải click 3 lần
            #Đoạn này nếu đăng nhập sai quốc gia nó nghi ngờ thì hỏi mình để khẳng định lại 3 lần
            if driver.find_element('id', 'checkpointSubmitButton'):# nếu có nút check
                driver.find_element('id', 'checkpointSubmitButton').click()
                if driver.find_element('id', 'checkpointSubmitButton'):  # nếu có nút check
                    driver.find_element('id', 'checkpointSubmitButton').click()
                    driver.find_element('id', 'checkpointSubmitButton').click()

full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'
i = Login_fb(full_2fa)
i.go_driver()
time.sleep(2) # Let the user actually see something!
#Câu hỏi: vì sao vào fb xong cái nó tắt ngay
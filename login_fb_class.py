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
        #chuyển dưới lên
        self.driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
    
    def go_driver(self):
        # driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
        self.driver.get('https://www.facebook.com/');
        time.sleep(2) # Let the user actually see something!
        self.driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
        self.driver.set_window_size(1366, 768)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
        #tim vi tri uid, pass:
        id_User = self.driver.find_element('id', 'email')#vi tri email
        pass_User = self.driver.find_element('id', 'pass')#vi tri pass
        #input uid, pass:
        id_User.send_keys(self.fb_id)#nhap uid
        pass_User.send_keys(self.fb_pass)#nhap pass
        pass_User.send_keys(Keys.ENTER)#bam Enter
        time.sleep(2) # Let the user actually see something! 
        #Nếu via đã chết thì đến đoạn này nó ra link: https://www.facebook.com/checkpoint/disabled/?next và không ra trang nhập 2fa, cần if cho nó
        self.url_after_mailpass = self.driver.current_url
        if self.url_after_mailpass == 'https://www.facebook.com/checkpoint/disabled/?next':
            pass
        else:
            #Chuyển sang trang nhập OTP 6 số của 2FA:
            self.code_box = self.driver.find_element('id', 'approvals_code')#vi tri nhap 2FA
            import pyotp#thu vien lay 2FA
            totp = pyotp.TOTP(self.fb_2fa)#khong hieu(code copy)
            now_2fa = totp.now()#OTP now
            self.code_box.send_keys(now_2fa)#nhập mã OTP 6 số vào code box
            self.code_box.send_keys(Keys.ENTER)
            self.driver.find_element('id','checkpointSubmitButton').click()

            #Đoạn này có thể via checkpoint 282, do đó cần check có bị chết fb dạng 282 không hoặc bị disable hay không
            self.url_now_class = self.driver.current_url
            if self.url_now_class == 'https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F' or self.url_now_class == 'https://www.facebook.com/checkpoint/disabled/?next' or self.url_now_class == 'https://www.facebook.com/checkpoint/828281030927956/?next=https%3A%2F%2Fwww.facebook.com%2F':
                pass#self.val_break = True#break này sẽ giúp thoát khỏi via hiện tại, đúng ra là nên có 1 file được tạo ra để ghi lại via lỗi này
            else:#link hiện tại khác link checckpoint 282
                if self.driver.current_url != 'https://www.facebook.com/':#nếu lỗi đăng nhập khác quốc gia, phải click 3 lần
                    #Đoạn này nếu đăng nhập sai quốc gia nó nghi ngờ thì hỏi mình để khẳng định lại 3 lần
                    if self.driver.find_element('id', 'checkpointSubmitButton'):# nếu có nút check
                        self.driver.find_element('id', 'checkpointSubmitButton').click()
                        if self.driver.find_element('id', 'checkpointSubmitButton'):  # nếu có nút check
                            self.driver.find_element('id', 'checkpointSubmitButton').click()
                            self.driver.find_element('id', 'checkpointSubmitButton').click()#có khi nó checkpoint địa điểm xong nớ mới báo 282: https://www.facebook.com/checkpoint/?next

        def __exit__(self, exc_type, exc_val, exc_tb):# hàm này thêm vào để ngăn trình duyệt exit theo link: https://stackoverflow.com/questions/72090951/how-to-avoid-selenium-driver-closing-automatically
            if self.teardown:
                self.driver.quit()

    # full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'
    # i = Login_fb(full_2fa, teardown=False)
    # i.go_driver()
    # time.sleep(2) # Let the user actually see something!
    #Câu hỏi: vì sao vào fb xong cái nó tắt ngay
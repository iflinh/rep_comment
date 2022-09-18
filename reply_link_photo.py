from operator import index
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
driver.get('https://www.facebook.com/');
time.sleep(2) # Let the user actually see something!
driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
driver.set_window_size(1366, 768)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/

#Đây là 2 fb mẫu, thường mua fb nó có dạng UID|PASS|2FA có chỗ thì UID|PASS|2FA|Cookie|Email|PassEmail|... tùy chỗ bán
#100079633475311|r4DdyaYq65w3u|CWYG RUKA LFI3 AXEA OK2N GGF4 6YKK 7XUF
#100079562139644|b3X9caHwQD51P|FTGI HWBP NIZZ HQX5 SXEV XALL VXBM FYB5
# 100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY


full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'#yêu cầu phải dạng UID|pass|2fa    không có gạch đứng hay gì cuối 2FA, mỗi cái cách nhau gạch đứng
# post = 'https://www.facebook.com/Erikaalexanderthegreat/posts/627076168789407?comment_id=1376789906178260'


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
time.sleep(2) # Let the user actually see something!

#Chuyển sang trang nhập OTP 6 số của 2FA:
code_box = driver.find_element('id', 'approvals_code')#vi tri nhap 2FA
import pyotp#thu vien lay 2FA
totp = pyotp.TOTP(fb_2fa)#khong hieu(code copy)
now_2fa = totp.now()#OTP now
code_box.send_keys(now_2fa)#nhập mã OTP 6 số vào code box
code_box.send_keys(Keys.ENTER)
driver.find_element('id','checkpointSubmitButton').click()

print(driver.current_url)
if driver.current_url != 'https://www.facebook.com/':
    #Đoạn này nếu đăng nhập sai quốc gia nó nghi ngờ thì hỏi mình để khẳng định lại 3 lần
    if driver.find_element('id', 'checkpointSubmitButton'):# nếu có nút check
        driver.find_element('id', 'checkpointSubmitButton').click()
        if driver.find_element('id', 'checkpointSubmitButton'):  # nếu có nút check
            driver.find_element('id', 'checkpointSubmitButton').click()
            driver.find_element('id', 'checkpointSubmitButton').click()

id_comment_list = [762782358342714,1101729964098318,1093509774636243,837452104306056,846847212889215]
for id in id_comment_list:
  try:
    post = f'https://www.facebook.com/photo/?fbid=627076168789407&set=a.291635429000151&comment_id={id}'
    #Vào link post id comment:
    driver.get(post);#link post
    time.sleep(5) # Let the user actually see something!
    #Bấm nút like:
    #rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd
    t = driver.find_elements(By.XPATH, "//div[@class='rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd']")#.click()#tìm like
    # print(t)
    # print(len(t), 'len(t)')
    t[0].click()#click like
    time.sleep(2)#3s scroll 1 time
    t = driver.find_elements(By.XPATH, "//div[@class='qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd']")#.click()
    t[0].click()#click reply
    box = driver.find_elements(By.XPATH, "//p[@class='kmwttqpk kjdc1dyq l7ghb35v m8h3af8h']")#vi tri pass
    reply = f'Your shirt here: https://moteefe.com/may'
    box[0].send_keys(reply)#nhap nội dung reply
    box[0].send_keys(Keys.ENTER)#bam Enter
    print('Đã reply, đã enter')
    time.sleep(1)#3s scroll 1 time
  except:
    continue

#đóng chrome:
# driver.quit()
#Câu hỏi: làm sao cuộn thanh nhỏ bên trong nếu có nhiều thanh cuộn
#https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/xu-ly-file-trong-python/doc-file-trong-python/
#Đọc trang này để đọc file và xóa kí tự xuống dòng trong file id commment
from operator import index
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
driver = webdriver.Chrome('C:/Users/DELL/Desktop/Python/chromedriver')
driver.get('https://www.facebook.com/');
time.sleep(2) # Let the user actually see something!
driver.set_window_position(0, 0)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/
driver.set_window_size(1366, 500)#kích thước màn hình lấy ở trang https://www.selenium.dev/documentation/webdriver/browser/windows/

#Đây là 2 fb mẫu, thường mua fb nó có dạng UID|PASS|2FA có chỗ thì UID|PASS|2FA|Cookie|Email|PassEmail|... tùy chỗ bán
#100079633475311|r4DdyaYq65w3u|CWYG RUKA LFI3 AXEA OK2N GGF4 6YKK 7XUF
#100079562139644|b3X9caHwQD51P|FTGI HWBP NIZZ HQX5 SXEV XALL VXBM FYB5
# 100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY


full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'#yêu cầu phải dạng UID|pass|2fa    không có gạch đứng hay gì cuối 2FA, mỗi cái cách nhau gạch đứng
post = 'https://www.facebook.com/Erikaalexanderthegreat/posts/627076168789407?comment_id=1376789906178260'

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

#Vào link post:
driver.get(post);#link post
time.sleep(5) # Let the user actually see something!

def scroll_chrome():#Function scroll
    for i in range(2):
        driver.execute_script(f"window.scrollTo(0, {i+1}*300)")
        time.sleep(1)#3s scroll 1 time
        # print(f'scroll = {i+1}')
scroll_chrome()

# driver.find_element('class','i85zmo3j alzwoclg m8h3af8h l7ghb35v kjdc1dyq kmwttqpk gcj2zyi8').click()
print('Truoc khi chon')
#Click All Comments(-1) or Newest(-2) nếu có cũ nhất thì t[0].click()
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, "//div[@class='bdao358l om3e55n1 g4tp4svg i85zmo3j fxk3tzhb bq6c9xl4']").click()
print('Sau khi Click1')
t = driver.find_elements(By.XPATH, "//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl szxhu1pg glosn74e oog5qr5w tes86rjd rtxb060y ztn2w49o']")#.click()
print(t)
print(len(t), 'len(t)')
t[-1].click()#-1 là tất cả comment, nếu có mới nhất thì -2 là mới nhất, nếu có cũ nhất thì 0 là cũ nhất
#CÂU HỎI: LÀM SAO TÌM VỚI TEXT: VÍ DỤ All comments
# driver.find_element(By.XPATH, "//a[text()='All comments']").click()
# driver.find_element(By.XPATH, '//a[text()="All comments"]').click()
# https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/
# Gặp lỗi là tìm 1 cái duy nhất, nếu list thì không click được, một là tìm kiếm, 2 là len list hoặc in list ra
# list_class = driver.find_elements(By.XPATH, "//div[@class='bdao358l om3e55n1 g4tp4svg i85zmo3j fxk3tzhb bq6c9xl4']")
# print(list_class, 'list_class')
# list_class[0].click()
# driver.find_element(By.XPATH, //*[@class='bdao358l om3e55n1 g4tp4svg i85zmo3j fxk3tzhb bq6c9xl4']).click()

# list_class = driver.find_elements('style', 'background-image: url("https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/SCMVvzby_a1.png"); background-position: 0px -164px; background-size: auto; width: 16px; height: 16px; background-repeat: no-repeat; display: inline-block;')
# print(list_class, 'list_class')
# list_class[1].click()
# driver.find_element()


driver.execute_script("window.scrollTo(0, 1000);")
print('Mới cuộn đến 1000')

from bs4 import BeautifulSoup#in thử xem nó sao
source = driver.page_source
time.sleep(1)
soup = BeautifulSoup(source, 'html.parser')
time.sleep(1)
data = soup.find_all("span", class_="gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w innypi6y rtxb060y")
time.sleep(1)
print(len(data))#in thử xem nó sao
# print(data)
for i in data:
    if i.text == 'View more comments' or id.text == 'Xem thêm bình luận':
        print(data.index(i))
        print(i)
    print(data.index(i))
    print(i)

t = driver.find_elements(By.XPATH, "//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w innypi6y rtxb060y']")#.click()
# print(t)
print(len(t), 'len(t)')
t[-2].click()
print('Đã click vào view more lần: ')
time.sleep(2)#3s scroll 1 time

def scroll_click_view_more():
    driver.execute_script("window.scrollTo(0, 2000);")
    print('Mới cuộn đến 1000')
    time.sleep(1)#3s scroll 1 time
    t = driver.find_elements(By.XPATH, "//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w innypi6y rtxb060y']")#.click()
    # print(t)
    # print(len(t), 'len(t)')
    t[-2].click()
    time.sleep(2)#3s scroll 1 time
    print('Đã click vào view more')

# data = soup.find_all("span", class_="gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w innypi6y rtxb060y")
# time.sleep(1)
# print(len(data))#in thử xem nó sao

for i in range(10):
    scroll_click_view_more()

source = driver.page_source
time.sleep(1)
soup = BeautifulSoup(source, 'html.parser')
time.sleep(1)
data = soup.find_all("a", class_="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq cxfqmxzd rtxb060y gh55jysx")
# data = soup.find_all("div", class_="om3e55n1 d2hqwtrz oxkhqvkx rl78xhln gt60zsk1 alzwoclg jl2a5g8c icdlwmnq")#(49, vì cái đầu tiên khác),class này cũng 51 cái: jg3vgc78 cgu29s5g lq84ybu9 hf30pyar r227ecj6
#Khi nào link có id comment nó mới hiện lên cái reply của chính comment đó, làm tăng thêm class, cái đoạn class con này thì 50:oxkhqvkx rl78xhln gt60zsk1
time.sleep(1)
print(len(data))#in thử xem nó sao
# print(data)
list_id_comment = []
for i in data:
    long_link = i['href']
    id_comment = long_link[long_link.index('comment_id=') + 11 : long_link.index('&__cft__')]
    list_id_comment.append(id_comment)

print(len(list_id_comment), 'so id comment')
print(list_id_comment)

#Lưu list vào five csv:
import pandas as pd#copy thì thêm vào
df = pd.DataFrame(list_id_comment)
file_name = 'login_fb_get_id_comment.csv'
df.to_csv(file_name, index = False)

# time.sleep(10)#3s scroll 1 time
#đóng chrome:
driver.quit()
#Câu hỏi: làm sao cuộn thanh nhỏ bên trong nếu có nhiều thanh cuộn
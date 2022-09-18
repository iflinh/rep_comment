from operator import index
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
from selenium.webdriver.common.by import By
from login_fb_class import Login_fb
full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'

i = Login_fb(full_2fa, teardown=False)#Chú ý: làm gì cũng có 'i.' mới gọi được các biến trong class Login_fb
i.go_driver()
time.sleep(2) # Let the user actually see something!

#ghép thêm reply link photo:
id_comment_list = [762782358342714,1101729964098318,1093509774636243,837452104306056,846847212889215]
link_photo_id = 'https://www.facebook.com/photo/?fbid=627076168789407&set=a.291635429000151&comment_id=762782358342714'
photo_id = link_photo_id[ : link_photo_id.index('_id=')] + '_id='
for id in id_comment_list:
  try:
    post = f'{photo_id}{id}'#có thể thay bằng: post = photo_id + id
    #Vào link post id comment:
    i.driver.get(post);#link post   #driver.get('https://www.facebook.com/');
    time.sleep(5) # Let the user actually see something!
    #Bấm nút like:
    #rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd
    t = i.driver.find_elements(By.XPATH, "//div[@class='rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd']")#.click()#tìm like
    # print(f't = {t}')
    # print(len(t), 'len(t)')
    t[0].click()#click like
    time.sleep(2)#3s scroll 1 time
    t = i.driver.find_elements(By.XPATH, "//div[@class='qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq rtxb060y fsf7x5fv aglvbi8b igjjae4c om3e55n1 cxfqmxzd']")#.click()
    t[0].click()#click reply
    box = i.driver.find_elements(By.XPATH, "//p[@class='kmwttqpk kjdc1dyq l7ghb35v m8h3af8h']")#vi tri pass
    reply = f'Your shirt here: https://moteefe.com/may'
    box[0].send_keys(reply)#nhap nội dung reply
    box[0].send_keys(Keys.ENTER)#bam Enter
    print(f'Đã reply id: {id}')
    time.sleep(1)#3s scroll 1 time
  except:
    continue
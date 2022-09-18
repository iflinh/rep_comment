#Open list via
#input post photo:
#for via
    #time bắt đầu
    # try:
        #login fb#thường lỗi đây là chuyển
        #open id comment
        #open file caption
        #open file link
        #rep cmt(mặc định 10 lần)
            #for id 1-10
                #read id comment
                #rep comment#có thể lỗi spam ở đây và nó đứng không chạy kéo dài thời gian, cần qua via mới
                #add id vào file id đã comment
                #remove id khỏi file id cmt đã dùng để sau có chạy lại thì chỉ chạy cái chưa dùng
    #except: #nếu lỗi thì lưu lại via lỗi qua via khác
        #open file via lỗi và ghi vào #nên có 1 cái chạy đa luồng để check login fb, đỡ lỗi
        #countinue
from operator import index#hình như cái này để teardown tức không tự tắt trình duyệt
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys# to send Keys
from selenium.webdriver.common.by import By
from login_fb_class import Login_fb
import random

# full_2fa = '100079653724245|hCwzMsUfO0I1q|UH4V OLYH LBQS SSYF BSSP PPWJ CXRG 7BRY'

open_via = open("via_file.csv",'r',encoding = 'utf-8')
# for i in range(4):
#     a = f.readlines(1:3)
#     print (f'Nội dung dòng {i+1}:',(a))
#     # b = f.readline()
open_photo = open("photo_file.csv",'r',encoding = 'utf-8')
open_caption = open("caption_file.csv",'r',encoding = 'utf-8')
open_link = open("link_file.csv",'r',encoding = 'utf-8')
open_id_comment = open("id_comment_csv.csv",'r',encoding = 'utf-8')
number_rep = 10#tùy ý thay đổi


lines_caption = open_caption.readlines()#các dòng trong file caption để làm random caption
lines_link = open_link.readlines()

# random_int_caption = random.randint(0,len(lines_caption)-1)
# random_caption = lines_caption[random_int_caption].strip() + ' '#xóa dấu enter cuối dòng, sau đó công thêm khoảng cách
# random_int_link = random.randint(0,len(lines_link)-1)
# random_link = lines_link[random_int_link].strip()#strip để xóa dấu enter cuối dòng
# reply = f'{random_caption}{random_link}'
# print(reply)
# exit()

#Bắt đầu vào
via_list = open_via.readlines()#láy 1 dòng từ file via, tức là lấy 1 via ra
link282 = 'https://www.facebook.com/checkpoint/1501092823525282'#link checkpoint #bỏ ngoài for để khỏi gán cả trăm lần
link956 = 'https://www.facebook.com/checkpoint/828281030927956'
link_photo_id = open_photo.readline().strip()#Cái này phải nằm ngoài for via, hoặc mỗi lần phải lấy từ đầu
photo_id = link_photo_id[ : link_photo_id.index('_id=')] + '_id='#có 1 link, nên bỏ trong vòng for, nó có gì đâu nữa mà read lại nên lỗi không tồn tại string '_id='
for via in via_list:
  #Login gọi login fb class:
  full_2fa = via.strip()#cho nó mất dấu enter và dấu cách nếu có
  i = Login_fb(full_2fa, teardown=False)
  i.go_driver()
  time.sleep(5) # Đến đây đã login xong, giờ chuẩn bị rep, cần chuẩn bị id comment
  url_now = i.driver.current_url#i. vì trong class
  if url_now == 'https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F' or url_now == 'https://www.facebook.com/checkpoint/disabled/?next' or url_now == 'https://www.facebook.com/checkpoint/828281030927956/?next=https%3A%2F%2Fwww.facebook.com%2F':
    #chỗ này là để thêm via checkpoint vào file via checkpoint
    continue# break#nếu nó checkpoint 282 thì bỏ via này, thêm via này vào list via bị checpoint trước khi break
  else:#via OK thì rep
    #REP CMT:
    id_comment_list = []#Này và hàm for bên dưới là để tạo ra id_comment_list có 10 id như file cũ
    for num in range(number_rep):#0-9
        id_comment = int(open_id_comment.readline().strip())#chưa biết cách để xóa dòng đã lấy trong, có thể edit: https://stackoverflow.com/questions/72444994/how-to-edit-a-line-of-a-text-file-in-python
        id_comment_list.append(id_comment)
    # print(id_comment_list)
    # id_comment_list = [762782358342714,1101729964098318,1093509774636243,837452104306056,846847212889215]
    #LẤY VẬY CÓ CÁI DỞ LÀ VIA DIE GIỮA CHỪNG THÌ COMMENT BỊ BỎ QUA LUÔN, NÊN READ LÀ HAY NHẤT VÀ FOR NÊN LÀ I IN RANGE(NUMBER_REP)

    for id in id_comment_list:#Vòng lặp rep id comment, trong quá trình lặp này via có thể bị checkpoint(chưa nói bị chặn)
      try:#thực hiện cái này nếu lỗi thì countinue
        post = f'{photo_id}{id}'#có thể thay bằng: post = photo_id + id
        #Vào link post id comment:
        i.driver.get(post);#link post   #driver.get('https://www.facebook.com/');
        time.sleep(1) # Let the user actually see something!
        url_now_in_id = i.driver.current_url#i. vì trong class
        if link282 in url_now_in_id or link956 in url_now_in_id:#tức là bị check point 282, hoặc 956: https://www.facebook.com/checkpoint/1501092823525282/?next={post}
          #Đến đây là giải quyết được 282 và 956 nhưng chưa giải quyết được việc bị hạn chế bình luận và lỗi chưa hoàn thành mà rời đi id khác
          #nếu nó checkpoint ở đây thì, nhiều id trong list 10 cái chưa được comment phải bỏ qua
          break#khi break khỏi vòng lặp này thì thoát khỏi vòng for này, vì đây lệnh cuối nên qua via tiếp theo, cũng có thể cho lệnh breack cuối, ngoài vòng for này ddeer nó sang vòng for mới
        else:#không bị checkpoint
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

          #tạo random caption và random link để reply:
          random_int_caption = random.randint(0,len(lines_caption)-1)
          random_caption = lines_caption[random_int_caption].strip() + ' '#xóa dấu enter cuối dòng, sau đó công thêm khoảng cách
          random_int_link = random.randint(0,len(lines_link)-1)
          random_link = lines_link[random_int_link].strip()#strip để xóa dấu enter cuối dòng
          reply = f'{random_caption}{random_link}'

          box[0].send_keys(reply)#nhap nội dung reply
          time.sleep(2)#Chờ 2 giấy xem, sao nó cứ báo lỗi là bạn có muốn thoát không, chứng tỏ đã ghi mà chưa xóa hoặc enter được
          box[0].send_keys(Keys.ENTER)#bam Enter
          time.sleep(2)
          #chỗ này chắc phải hiện lên áo mới gọi là comment thành công
          #Đoạn này dễ bị hạn chế, nếu có cửa sổ hạn chế bình luận hiện lên thì sang via khác: break
          #b6ax4al1 lq84ybu9 hf30pyar om3e55n1 oshhggmv qm54mken rt9i6ysf
          restrict_comment = i.driver.find_element(By.XPATH, "//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1 oshhggmv qm54mken rt9i6ysf']")
          print(restrict_comment)
          # exit()
          if restrict_comment != '':
            break#Là qua via mới, thử với via chưa bị gì xem có lỗi không
          print(f'Đã reply id: {id}')
          # time.sleep(1000)#3s scroll 1 time
      except:
        continue#nếu xảy ra lỗi thì chuyển sang vòng lặp tiếp theo, tức lf id mới, nhưng có vấn để lỡ nó lâu quá 1 tác vụ thì sao, phải bỏ qua nếu mỗi via quá 2 phút

i.driver.quit()

#Những cái cần làm: xóa id đã lấy, ghi file via hỏng, ghi id đã comment, đánh số commment đã rep được, chạy đa luồng, nhập vào link post khác, số id khác, chạy tuần tự khỏi thay
#up được file hình
#tạo ra phần check login riêng
#về phần get i thì có số 0 ở đầu
#làm thành file exe, giao diện

#CÓ thể phát hiện và click leave ở https://stackoverflow.com/questions/19003003/check-if-any-alert-exists-using-selenium-with-python
#Lỗi mới: tự nhiên nó out via, nghĩa là via không còn login, (có thể id đó không còn tồn tại nên ra comment mới làm các cái sau cứ rep vào comment của mình, trước đó thì bỏ qua mãi không được, cuối cùng via bị chặn thử lại)
#Những lỗi đã gặp khi viết này: break ngoài vòng lặp, gọi hàm trong class không có i. i là tên hàm, trường hợp khác xảy ra, trùng tên biến i với class i, 
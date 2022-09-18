import csv
str = 'Đây là ca khúc trong tập 16 - Thỉnh kinh nữ nhi quốc. Thầy trò Đường Tăng tới Tây Lương quốc - đất nước chỉ toàn nữ nhi. Động lòng trước dung mạo của “Ngự đệ” nhà Đường, nữ vương xinh đẹp đem lòng ái mộ và thuyết phục Đường Tăng ở lại để cùng nàng kết tóc se tơ. Trước sự si tình của nữ vương, trái tim Đường Tăng cũng có phút lay động, bởi vậy mới ngập ngừng câu nói: “Nếu có kiếp sau”. Dù vậy, quyết tâm phổ độ chúng sinh vẫn chiến thắng ái tình nam nữ, Đường Tăng từ biệt nữ vương, tiếp tục hành trình đi Tây Thiên lấy kinh. Sau khi quay xong tập 16, đạo diễn Dương Khiết muốn nhạc sĩ Hứa Kính Thanh viết một ca khúc dành riêng cho mối tình Tây Lương nữ vương và Đường Tăng. Nhạc sĩ họ Hứa kể lại: “Kịch bản câu chuyện này rất hay, cảnh quay cũng rất đẹp, dù ở nhân gian mà ngỡ như nơi tiên cảnh”. Thế là, những nốt nhạc đầu tiên vang lên trong đầu ông: \“Khẽ hỏi thánh tăng \‘Thiếp có đẹp?\’\”.Sau khi phần nhạc của ca khúc hoàn tất, đạo diễn Dương Khiết phụ trách viết lời. Giai điệu đẹp với ca từ như thơ, đầy ý nghĩa giúp Tình nhi nữ trở thành một sáng tác kinh điển khác của Tây du ký. Ca khúc do Ngô Tĩnh thể hiện.'
# tạo ra list k có ký tự đặc biệt, và không viết hoa.
# for các phần tử nếu từ mới hoàn toàn thì tạo dict, key là từ, value là number, nếu từ có sẵn rồi thì thêm vào key có sẵn value + 1
str_vietthuong = str.lower()
#tách ra đưa vào list
list_str = str_vietthuong.split()
# print(f'list_str = {list_str}')
list_str_khong_dau = []
for word in list_str:
    word_khong_dau = ''.join(e for e in word if e.isalnum())
    list_str_khong_dau.append(word_khong_dau)
# print(list_str_khong_dau)

count={}
for i in list_str_khong_dau:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
# print(count)

dict = count
items_sorted = sorted(dict.items(), key = lambda x : x[1], reverse = True) #code này copy ở trang:https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/dictionary-trong-python/sap-xep-dictionary-python/
print(items_sorted)
#chuyển dict thành CSV
# with open('string_to_csv.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = [])
#     writer.writeheader()
#     writer.writerows(dict)

# my_dict = count
# with open('my_file.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in my_dict.items()]
#     # copy tại link(16 vote): https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value

mydict = count
import pandas as pd #     # copy tại link(36 vote): https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
(pd.DataFrame.from_dict(data=mydict, orient='index')
   .to_csv('dict_file.csv', header=False)) 

#hoặc ra excel tại link này:
# https://stackoverflow.com/questions/28555112/export-a-simple-dictionary-into-excel-file-in-python



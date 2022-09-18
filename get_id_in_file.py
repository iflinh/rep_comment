# Đây là file học
f = open("id_comment_csv.csv",'r',encoding = 'utf-8')#chế độ r là chỉ đọc read
id_out = []
for i in range(4):
    a = int(f.readline().strip())#strip là để xóa dấu enter cuối dòng, int là biến nó về số nguyên,
    id_out.append(a)
    print (f'Nội dung dòng {i+1}:',(a))
print(id_out)
    # b = f.readline()
    # print ('Nội dung dòng 2: ', (b))
    # c = f.readline()
    # print ('Nội dung dòng 3: ', (c))
    # d = f.readline()
    # print ('Nội dung dòng 4: ', (d))

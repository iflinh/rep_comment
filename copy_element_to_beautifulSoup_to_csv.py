from bs4 import BeautifulSoup#lập trình bằng VS Code thì có dấu abc ở trên tab giúp thu gọn dòng
copy_element = '''
'''
soup = BeautifulSoup(copy_element, "html.parser")
data = soup.find_all('a', class_='_6qw7')
y = len(data)
print(y)
list_id_comment = []
for i in data:
    link = i['href']
    print(link)
    exit()
    id_poistion = link.index('comment_id=')
    # print(f'id_poistion = {id_poistion}')
    len_find = len('comment_id=')
    id_comment = link[id_poistion + len_find :]
    # print(id_comment)
    list_id_comment.append(id_comment)

import pandas as pd#copy thì thêm vào
df = pd.DataFrame(list_id_comment)
file_name = 'id_comment_csv.csv'
df.to_csv(file_name, index = False)
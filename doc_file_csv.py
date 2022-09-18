import csv
list = ["dien thoai", "quan ao", "may tinh"]

for l in list:
    with open(f'shopee/{l}.csv', 'a', encoding="utf-8") as file:
        pass
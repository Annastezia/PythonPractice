import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import gspread

gs = gspread.service_account(filename='../../credits.json')  # подключаем файл с ключами и пр.
sh = gs.open_by_key('1k-gbn43tX6AxE7-TqxlZa7-zWbSh4G_IYU8lgRo5ys4')  # подключаем таблицу по ID
worksheet = sh.sheet1  # получаем первый лист

url = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999'
link = requests.get(url)
page = BeautifulSoup(link.text, 'lxml')
tables = page.find('table', class_='confluenceTable')

headers = []
lst = []
num = []
desc = []
i = 0
k = 1

for name in tables.find_all('th'):
    header = name.text
    headers.append(header)
print(headers)

for name in tables.find_all('td'):
    status = name.text
    lst.append(status)
print(lst)

while i < int(len(lst)):
    num.append(lst[i])
    i += 2
print(num)

while k < int(len(lst)):
    desc.append(lst[k])
    k += 2
print(desc)

data = [num, desc]
export = zip_longest(*data, fillvalue='')
with open('Codes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(export)

content = open('Codes.csv', 'r').read()
gs.import_csv('1k-gbn43tX6AxE7-TqxlZa7-zWbSh4G_IYU8lgRo5ys4', content)

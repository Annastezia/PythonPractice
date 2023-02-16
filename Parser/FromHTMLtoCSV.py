import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

url = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999'
link = requests.get(url)
page = BeautifulSoup(link.text, 'lxml')
tables = page.find('table', class_='confluenceTable')

headers = []
for name in tables.find_all('th'):
    header = name.text
    headers.append(header)
print(headers)

lst = []
num = []
desc = []
i = 0
k = 1

for name in tables.find_all('td'):
    status = name.text
    lst.append(status)
print(lst)

while i < int(len(lst)):
    num.append(lst[i])
    i += 2
print(num)
#
while k < int(len(lst)):
    desc.append(lst[k])
    k += 2
print(desc)

data = [num, desc]
export = zip_longest(*data, fillvalue='')
with open('PythonPractice/Parser/Codes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(export)

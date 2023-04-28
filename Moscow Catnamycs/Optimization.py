#ОПТИМИЗАЦИЯ КОДА

import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segment = list(data['segment'])
robocats = list(data['robocats'])

means = []  # пустой список для сбора средних показателей

# считаем среднее для нулевого сегмента:
cats = 0  # общее число робокотов
counter = 0  # количество обращений
for index in range(len(data)):
    if segment[index] == 'Segment 0': 
        cats +=robocats[index] 
        counter += 1
means.append(cats / counter) # добавляем среднее в means

# то же самое для первого сегмента:
cats = 0
counter = 0
for index in range(len(data)):
    if segment[index] == 'Segment 1': 
        cats += robocats[index] 
        counter += 1
means.append(cats / counter)

# и для второго: 
cats = 0
counter = 0
for index in range(len(data)):
    if segment[index] == 'Segment 2': 
        cats += robocats[index] 
        counter += 1
means.append(cats / counter)

names = ['Segment 0', 'Segment 1', 'Segment 2']
seaborn.barplot(x=means, y=names) 

#В таком случае удобнее написать вложенный цикл. Вот как это может выглядеть:

# список сегментов, чтобы цикл мог пройти по ним
names = ['Segment 0', 'Segment 1', 'Segment 2']

# список, в который будем складывать средние значения
means = []

# внешний цикл по названиям сегментов
for name in names:
    # код внутри - почти то же, что было раньше
    cats = 0
    counter = 0
    # внутренний цикл
    for index in range(len(data)):
        # в этой строке заменили название сегмента на переменную цикла
        if segment[index] == name:
            cats += robocats[index] 
            counter += 1
    means.append(cats / counter)

# код достаточно написать один раз
# цикл повторит его столько раз, сколько нужно

seaborn.barplot(x=means, y=names) 
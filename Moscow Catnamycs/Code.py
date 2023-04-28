import pandas

data = pandas.read_csv('support_data.csv')

interval = list(data['interval'])# преобразуем столбец interval в список

interval_unique = [] #создаем пустой список для уникальных значений видов интервалов

for index in range(len(interval)): #проходим по списку через индексы, чтобы сопоставить значения с другим датасетом
    if interval[index] not in interval_unique: #проверяем наличие значения в списке уникальных
        interval_unique.append(interval[index])  
        
#Значения получили "До внедрения ботов" и "После внедрения ботов"
#Узнать, сколько строк приходится на каждый период — посчитать количество значений "До внедрения роботов" и "После внедрения роботов" в столбце interval. Для оценки распределения записей относительно интервалов

count_before = 0 #счетчик для значения "До..."
count_after = 0 #счетчик для значения "После..."

for index in range(len(interval)):
    if interval[index] == 'До внедрения роботов':
        count_before += 1
    elif interval[index] == 'После внедрения роботов':
        count_after += 1

#Проводим аналогичную проверку для столбца segment — выясняем, какие уникальные значения в нём встречаются

segment = list(data['segment']) # преобразуем столбец segment в список
segment_unique = []

for index in range(len(segment)):
    if segment[index] not in segment_unique:
        segment_unique.append(segment[index])

#Оценить соотношение значений в датасете по сегментам пользователей. Для этого посчитать число строк, относящихся к каждому сегменту — 'Segment 0', 'Segment 1', 'Segment 2'. 

segment_0 = 0 #счетчик для значения Сегмента 0
segment_1 = 0 #счетчик для значения Сегмента 1
segment_2 = 0 #счетчик для значения Сегмента 2
        
for index in range(len(segment)):
    if segment[index] == 'Segment 0':
        segment_0 += 1
    elif segment[index] == 'Segment 1':
        segment_1 += 1
    elif segment[index] == 'Segment 2':
        segment_2 += 1

#Получили сильный разброс значений численности сегментов - больше всего пользователей оказалось в Сегменте 0

#Чтобы проверить гипотезу «пользователи разделены на сегменты по количеству робокотов из столбца robocats», можно посчитать среднее количество робокотов для каждого сегмента.  Проблема здесь состоит в том, что один и тот же клиент может обращаться в поддержку множество раз и в перерыве между обращениями покупать робокотов. 

robocats = list(data['robocats'])

cats = 0
# перебор индексов строк таблицы
for index in range(len(data)):
    if segment[index] == 'Segment 0': 
        cats += robocats[index] 
print(cats)

cats = 0
# вычисление для Segment 1
for index in range(len(data)):
    if segment[index] == 'Segment 1': 
        cats += robocats[index] 
print(cats)

cats = 0
# вычисление для Segment 2
for index in range(len(data)):
    if segment[index] == 'Segment 2': 
        cats += robocats[index] 
print(cats)

#Результаты соответственно: 0, 2468, 3964

#Чтобы найти средние показатели, в каждом сегменте разделим количество робокотов на количество обращений. 

cats = 0
counter = 0
# код для Segment 0
for index in range(len(data)):
    if segment[index] == 'Segment 0': 
        cats += robocats[index] 
        counter += 1

print(cats / counter) 

cats = 0
counter = 0
# код для Segment 1
for index in range(len(data)):
    if segment[index] == 'Segment 1': 
        cats += robocats[index] 
        counter += 1

print(cats / counter) 

cats = 0
counter = 0
# код для Segment 2
for index in range(len(data)):
    if segment[index] == 'Segment 2': 
        cats += robocats[index] 
        counter += 1

print(cats / counter) 

#Получили значения соответственно: 0.0, 1.0, 9.93483709273183, Визуализируем на столбчайто диаграмме
#Собераем среднее количество робокотов по каждому сегменту в один список. В другом списке перечисляем названия сегментов через запятую: 'Segment 0', 'Segment 1', 'Segment 2'. Затем вызываем функцию barplot(), передав ей список со средними показателями как x и список с названиями сегментов как y.

import seaborn

cats_0 = 0
cats_1 = 0
cats_2 = 0

counter_0 = 0
counter_1 = 0
counter_2 = 0

for index in range(len(data)):
    if segment[index] == 'Segment 0': 
        cats_0 += robocats[index]
        counter_0 += 1
    elif segment[index] == 'Segment 1':
        cats_1 += robocats[index]
        counter_1 += 1
    elif segment[index] == 'Segment 2':
        cats_2 += robocats[index]
        counter_2 += 1

common_list = []
common_list.append(cats_0/counter_0)
common_list.append(cats_1/counter_1)
common_list.append(cats_2/counter_2)
print(common_list)  #Получили средние значения [0.0, 1.0, 9.93483709273183]
segment_list = ['Segment 0','Segment 1','Segment 2']

seaborn.barplot(x = common_list, y = segment_list)

#Подтвердилась гипотеза: пользователи действительно разделены на сегменты по количеству купленных ими робокотов. 


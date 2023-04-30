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

#Показатели работы поддержки из датасета — скорость и длительность ответов, выданные промокоды и удовлетворённость пользователей в разных сегментах — помогут понять, что изменилось в компании после внедрения роботов и как это могло повлиять на доходы.

# списки со старыми и новыми названиями сегментов, а также периодами
segments_old = ['Segment 0', 'Segment 1', 'Segment 2']
segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

# вымышленные значения для примера
mean_scores = [[1, 2],
               [3, 4],
               [5, 6]]

# настраиваем и строим хитмэп
seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn') 

#Построим хитмэп с такими же настройками, но уже по настоящим значениям — средним пользовательским оценкам в каждом из сегментов до и после внедрения роботов

# названия сегментов и интервалов
segments_old = ['Segment 0', 'Segment 1', 'Segment 2']
segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

intervals_column = list(data['interval'])
segments_column = list(data['segment'])
score_column = list(data['score'])

# здесь будут средние оценки
mean_scores = []

for segment in segments_old:
    score_before = 0
    counter_before = 0
    score_after = 0
    counter_after = 0
    for index in range(len(data)):
        if segments_column[index] == segment:
            if intervals_column[index] == 'До внедрения роботов':
                score_before += score_column[index]
                counter_before += 1
            else:
                score_after += score_column[index]
                counter_after += 1
    segment_scores = [score_before / counter_before, score_after / counter_after]
    mean_scores.append(segment_scores)

seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

#По итогам построения хитмэпа: худшие оценки после внедрения стали поступать от постоянных, премиальных клиентов. Возможная причина - неспособность роботов вести продолжительные беседы, в отличие от сотрудников-людей. Построим хитмэп для продолжительности беседы ботов с клиентами.

mean_duration = []

for segment in segments_old:
    duration_before = 0
    counter_before = 0
    duration_after = 0
    counter_after = 0
    for index in range(len(data)):
        if segments_column[index] == segment:
            if intervals_column[index] == 'До внедрения роботов':
                duration_before += duration_column[index]
                counter_before += 1
            else:
                duration_after += duration_column[index]
                counter_after += 1
    segment_duration = [duration_before / counter_before, duration_after / counter_after]
    mean_duration.append(segment_duration)

seaborn.heatmap(mean_duration, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

# Длительность ответа снизилась для двух сегментов — роботы отвечают быстрее людей. Это может объяснить снижение оценок среди VIP-клиентов, которые привыкли к более подробным ответам. Но рост оценок для потенциальных клиентов остаётся загадкой. Теперь строим тепловую карту по среднему количеству выданных промокодов.

promo_column = list(data['promo'])
mean_promo = []

for segment in segments_old:
    promo_before = 0
    counter_before = 0
    promo_after = 0
    counter_after = 0
    for index in range(len(data)):
        if segments_column[index] == segment:
            if intervals_column[index] == 'До внедрения роботов':
                promo_before += promo_column[index]
                counter_before += 1
            else:
                promo_after += promo_column[index]
                counter_after += 1
    promo_avg = [promo_before/counter_before, promo_after/counter_after]
    mean_promo.append(promo_avg)
    
seaborn.heatmap(mean_promo, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

#Промокодов для потенциальных клиентов стало значительно больше — роботы выдают их почти каждому. В сегменте VIP промокоды исчезли вовсе, хотя раньше их выдавали всем. Из-за этого могли возникнуть и проблемы с доходами: потенциальных клиентов намного больше, чем VIP-клиентов, и такой наплыв клиентов с промокодами на покупку робокотов ниже обычной цены мог быть не предусмотрен финансовой моделью компании.

#Строим столбчатую диаграмму, отображающую зависимость оценки от среднего количества выданных промокодов. 

score_column = list(data['score'])
intervals_column = list(data['interval'])
promo_column = list(data['promo'])

# список всех оценок
scores = list(range(11))

promo_chance = []

for score in scores:
    promo = 0
    counter = 0
    for index in range(len(data)):
        if intervals_column[index] == 'До внедрения роботов' and score_column[index] == score:
            promo += promo_column[index]
            counter += 1
    promo_chance.append(promo/counter)
        
seaborn.barplot(x=scores,y=promo_chance)

#Вывод:  до внедрения роботов пользователи часто ставили самые высокие оценки — 8, 9 и 10 — именно после получения промокода на скидку. Скорее всего, роботы заметили эту связь и стали выдавать промокоды чаще.

#ОБЩИЕ ВЫВОДЫ В СБОРКЕ:

# Роботы достигли роста удовлетворённости пользователей в основном за счёт выдачи множества промокодов потенциальным клиентам;

# С увеличением количества выданных промокодов может быть связано и снижение доходов компании — клиенты скупают робокотов по сниженной цене;

# Скорее всего, такое поведение роботов связано с тем, что роботы в процессе обучения поймали связь между выданным промокодом и высокой оценкой от пользователя;

# Роботы плохо работают с VIP-клиентами: их удовлетворённость заметно снизилась. Это может негативно сказаться на показателях компании, потому что VIP-клиенты с десятками робокотов — основа бизнеса.
min_required_area = 40 # минимальная требуемая площадь
max_affordable_price = 190000 # максимально допустимая арендная ставка
third_ring_radius = 6.7 # максимальное расстояние от центра

open_hours_number = 18 # количество рабочих часов в сутки
traffic2visitors_average_ratio = 1 / 225 # средняя доля посетителей от числа прохожих
traffic2visitors_pessimistic_ratio = 1 / 300 # минимальная доля посетителей от числа прохожих
visitors2purchases_average_ratio = 0.1 # средняя доля покупателей от числа посетителей
visitors2purchases_pessimistic_ratio = 0.05 # минимальная доля покупателей от числа посетителей
average_order_value = 21000 # средняя стоимость покупки
average_order_value_pessimistic = 20000 # минимальная стоимость покупки
trade_margin = 0.2 # наценка
days_in_months = 30 # количество рабочих дней в месяц

# множитель для расчёта прибыльности в среднем сценарии
income_multiplier_average = (open_hours_number * 
                             traffic2visitors_average_ratio *
                             visitors2purchases_average_ratio *
                             average_order_value *
                             trade_margin *
                             days_in_months)

# множитель для расчёта прибыльности в пессимистичном сценарии
income_multiplier_pessimistic = (open_hours_number * 
                                 traffic2visitors_pessimistic_ratio *
                                 visitors2purchases_pessimistic_ratio *
                                 average_order_value_pessimistic *
                                 trade_margin *
                                 days_in_months)

number_of_employees = 2 # количество продавцов
employee_salary = 50000 # зарплата продавца
tax_multiplier = 1.43 # множитель для расчёта зарплаты с налогами

# зарплатная часть расходов
addition_to_expenses = number_of_employees * employee_salary * tax_multiplier

# минимальная ожидаемая прибыль
min_expected_profits = 500000

import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []
filtered_objects_profits = []

for index in range(len(realty_df)):
    if (realty_df['floor'][index] == 1 and
        realty_df['area'][index] >= min_required_area and
        realty_df['price'][index] <= max_affordable_price and
        realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
        realty_df['distance'][index] <= third_ring_radius and
        realty_df['already_taken'][index] == 0 and
        realty_df['competitors'][index] <= 1):
        filtered_objects_area.append(realty_df['area'][index])
        filtered_objects_price.append(realty_df['price'][index])
        filtered_objects_traffic.append(realty_df['traffic'][index])
        filtered_objects_address.append(realty_df['address'][index])
        filtered_objects_profits.append(realty_df['traffic'][index] * 
        income_multiplier_average - (realty_df['price'][index] + 
        addition_to_expenses))

for index in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index] > min_expected_profits:
        print(filtered_objects_price[index])
        print(filtered_objects_traffic[index])
        print(filtered_objects_address[index])
        print(filtered_objects_profits[index])
        print(filtered_objects_traffic[index] * income_multiplier_pessimistic - 
        (filtered_objects_price[index] + addition_to_expenses))
        print('----------') 

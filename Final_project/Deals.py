import numpy as np
import pandas as pd
#import re

Deals1 = pd.read_excel("Deals.xlsx", parse_dates = ['Closing Date', 'Created Time'])
Deals1 = Deals1.drop_duplicates()
#print(Deals.isnull().sum())
Deals1 = Deals1.dropna(how='all')
#print(Deals.info)
#исправление столбца 'Level of Deutsch'
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['Detmold, Paulinenstraße 95, 32756', 'f2', '.', 90, '-', '?', 'np.nan', 'nan', 'None', ' ', pd.NA, None, 'Thorn-Prikker-Str. 30, Hagen, 58093', 'Paderborn 33102, Schwabenweg 10', '31.05.2024', 'Lichtenfelser Straße 25, Untersiemau 96253', 'гражданка', 'Гражданин', '25 лет живет в Германии', 'не сдавал, но гражданин',  'Нет сертификатов, но есть С1 англ, неоконченное высшее в ИТ (и еще одно высшее юридическое) , очень хочет в ИТ, сильно замотивирована именно н', 'УТОЧНИТЬ!', 'УТОЧНИТЬ'], value='UNKNOWN')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['lэкзамен - 6 июля на В1. курсы вечером (но уверенно говорит на B1)','б1', 'b1', 'B1', 'В1','в1','В','Б1','b1+', 'в1-в2','В1-В2','Б1 ( ждет Б2)','ЯЗ: нем В1 был экз 03.05 повтор и сейчас ждет результаты. Технический англ был. А1 сейчас. ОБР: 2 во информационные и комп сети - инженер системоте', 'b1 (B2 ждет серт)', 'b1 (b2 в июле экзамен)', 'B1, сдает B2 в апреле', 'B1 (ждет результаты В2)', 'b1 (b2 15 марта экзамен)', 'Б1 ( ждет итог Б2)', 'Б1 ( проходит Б2)', 'НЯ - В1, АЯ - В1', 'в1-ня , в1-ая', 'B1 (B2 должна до конца февраля получить)', 'b1 (b2 экзамен 6 февраля)', 'В1, может уже В2?', 'Б10Б2', 'Б1?', 'B1 есть, ждем B2 в конце месяца', 'B1-B2', 'Сдавал 8 12 на B1 - ждет результат. 3 01 - аплейт - получил B1!', 'Б1-Б2', 'б1 (до июля на В2)', 'в1, идет на в2', 'b2-c1', 'b1-b2', 'Б1 ( проходит Б2 )', 'b1 (учила, но не сдала В2)', 'в1, еще нет сертификата', 'б1-б2', 'Бй', 'в1 , хочет совмещать с в2', 'в1 (уже сдала В2)', 'B1 (до февраля)', 'B1 (B2 экзамен в январе)', 'В1?', 'b1 (b2 экзамен 2 марта)', 'B1 немецкий и английский Advance', 'B2 (ждет итог экзамена)', 'b1 (b2 не сдал экзамен)', 'В1 (учится на В2 до авг.', 'В2 - не сдал', 'B1 вроде был (18 лет назад сдавал)', 'b2 ждет серт', 'В1, учится на В2 до няоб 24', 'Б1 ( ждет результат Б2)', 'В1 (учится на В2 уже)', 'В январе - В2 сдает'], value='B1', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['Сам оценивает на B2, 13 лет живет в Германии', 'B2' , 'в2',  'b2', 'В2', 'б2', 'Б2', 'Б2 ( учит С1)', 'б2+', 'Б2( 16.02 экзамен С1)', 'b2 (с1 экзамен 16 февраля)', 'в2-с1', 'b2-c2', 'б2 (с1 ждет рез-тат)', 'Б2-С1', 'B2-C2', 'B2+', 'B2 (говорит без проблем - давно здесь)', 'B2+ (не сдавал, но говорит)'],  value='B2', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['C2', 'С2'], value='C2', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['C', 'с1' ,  'С1', 'C1'], value='C1', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['Ждем B1', 'В1 в сентябре', 'Гражданка Германии уже год в Германии Учит немецкий и в сентябре b1 через гос-во проходит, а не через ДЖЦ, вечером учится 3 р в неделю с 18 до 21', 'а2' ,  'А2', 'a2','A2' , 'B1 будет в феврале 2025', 'А2-В1', 'А2 ( Б1 в июне)', 'B1 в процессе обучения', 'Пока А2, сдает 17 05 B1', 'окончание 13.06 курса на b1', 'А2( ждет итоги Б!)',  'Ждет результат по B1', 'b1 экзамен будет 12 апреля', 'ждем B1',  'Ждем B1 со дня на день', 'B1 еще нет результата', 'b1 9ждет экзамен)', 'Учиться до сентября на B1',  'b1 (ждет результат)',  'Б1 (учит Б2)', 'Ждем результат по B1', 'Ждет со дня на день В1', 'А2 (В1 с 3 раза не сдала, бератер видела наши доки)', 'b1 (ждет результаты)', 'А2 ( повтор на Б1)', 'ждет сертификат B1', 'b1 ждет серт на днях на руки', 'b1 24 февраля экзамен, англ b2', 'А2, в процессе Б1', 'А2(Б1 в марте экз)', 'Б1 ( ждет итог )' , 'б1 (ждет рез-тат)', 'А2(ждет итоги Б1)', 'будет B1 в июне', 'А2( включили нем в ангебот)', 'а2-в1', 'Б1( может будет)', 'А2 ( в процессе Б1)', 'b1 ждет результаты', 'b1 ждет экзамен в феврале', 'A2 (идет доучивать В1 - 300 часов; предположительно до августа)', 'Без 5 минут B1 (ждет результаты экзамена)', 'а2, англ B1', 'А2 нем -В2 англ', 'Проходит сейчас B1', 'Ждет результат по B1 в феврале', 'Проходит сейчас повторно B1', 'b1 экзамен в феврале', 'Учиться на B1 во вторую смену, в первую хочет получить одобрение на обучение у нас', 'b1 экзамен 26 января', 'а2 (б1 в сер января)', 'Учиться на B1', 'Сдала экзамен на B1, ждет в начале февраля результат', 'А2 ( Б1 март )', 'А2 (весной - еще 300 часов В1)', 'В январе будут результаты по экзамену на B1', 'А2-Б1', 'B1 (почти, не сдала чуть) + англ В1',  'в1 ждем результаты', 'А2 ( хочет просить совмещать)', 'B1 (ждет результаты)', 'А2+', 'а2 (сдавала экз В1, но не сдала похоже)', 'Б1 ( был екзамен ждет итог )', 'ня а2, ая в1', 'A2 (идет на В1)', 'ждет результаты по B1 экзамену', 'b2 (ждет серт)', 'b1 результат экзамена в феврале', 'в1 , экзамен на в2 15 декабря', 'А2 ( Б2 в процессе)', 'б1 заканчивает', '5 июля 2024 сдает экз на В2', 'А2 (заканчив В1 в июне)', 'a2-б1', 'b1 будет в январе экзамен, готов совмещать', 'a2 (b1 экзамен 15 июня)', 'b1 (ждет серт)', 'А2 (сдает B1 - 12 дек) - не сдал!', 'Ждет B1', 'b1 должна получить результаты в феврале'], value='A2', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=['точно уровень не знаю, но говорить могу - учила сама', 'а1' ,  'A1', 'А1' , 'А1 сертиф, но по факту А2', 'С1 -ая , Ня -а1', 'А1-А2', 'А2 ( скоро екзамен)', 'учит A2', 'курс А2-В1 - сдача в июле, но вечерняя смена инт курсов, настроен получить гутшайн уже сейчас.' , 'A1-A2',  'а1-а2 , ая свободный', 'не учила ( разговорный) сразу пошла работать', 'a0-a1', 'немецкий - а1-а2, англ b1-b2', 'A', 'разговорный из украины, без сертификата', 'сдавала А2 в сентябре', 'точно уровень не знаю, но говорить могу - учила сама' 'А2-В1 учит'], value='A1', regex=False)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=[ 0,'ня-0, но англ B2+', 'не учил', 'ня-0, ая-B1', 'никакой', 'идет на А1', 'ая в1', 'нулевой уровень, только пошел на курсы.', 'Нет', 'а0' , 'A0', 'А0'] , value='0', regex=False)

# Определение порядка кодирования
levels = ['0', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'UNKNOWN']

# Создание словарей для кодирования и декодирования
encoding_dict = {level: idx for idx, level in enumerate(levels)}
decoding_dict = {idx: level for idx, level in enumerate(levels)}

# Кодирование значений
Deals1['Level of Deutsch Encoded'] = Deals1['Level of Deutsch'].map(encoding_dict)

# Вывод результатов
# print("DataFrame с закодированными значениями:")
# print(Deals1['Level of Deutsch Encoded'])

# Справочная таблица
reference_table = pd.DataFrame(list(decoding_dict.items()), columns=['Code', 'Level of Deutsch'])
#print(reference_table)

# Получение распределения уникальных значений в столбце 'Level of Deutsch'
value_counts = Deals1['Level of Deutsch Encoded'].value_counts()

# Вывод результата
# print("Распределение уникальных значений в столбце 'Level of Deutsch Encoded':")
# print(value_counts)

# переименование столбца 'Contact Name'в 'CONTACTID', т.к. иx содержание совпадает (см. проверку совпадений в Contacts.ру )
Deals1 = Deals1.rename(columns={'Contact Name': 'CONTACTID'})

#преобразование дат и удаление устаревших столбцов
Deals1['Transaction_Creation_Time'] = pd.to_datetime(Deals1['Created Time'], format='%d.%m.%Y %H:%M')
Deals1['Transaction_Creation_Time'] = Deals1['Created Time'].dt.date
Deals1['Closing_Date'] = pd.to_datetime(Deals1['Closing Date'], format='%d.%m.%Y %H:%M')
Deals1['Closing_Date'] = Deals1['Closing Date'].dt.date
Deals1.drop(columns=['Created Time', 'Closing Date'], inplace=True)

Deals1['Education Type'] = Deals1['Education Type'].fillna(method='ffill')


# '#REF!' напрямую не заменяется; замена '#REF!' на 'WWWWW'
Deals1['Education Type'] = Deals1['Education Type'].apply(lambda x: 'WWWWW' if pd.isna(x) or x.strip() in ['#REF!'] else str(x).strip())
# Функция для проверки наличия 'WWWWW' в строке
def contains_WWWWW(row):
    return row.astype(str).str.contains('WWWWW', na=False).any()
# Удаление строк, содержащих 'WWWWW'
Deals1 = Deals1[~Deals1.apply(contains_WWWWW, axis=1)]


#замена некорректных значений в 'Offer Total Amount'
Deals1['Offer Total Amount'] = Deals1['Offer Total Amount'].replace(to_replace=['€ 2.900,00','€ 11398,00'], value=[2900,11398])
Deals1['Course duration'] = Deals1['Course duration'].fillna(6)

# Удаление строк с отсутствующими значениями, без контактного лица транзакция не рассматривается
Deals1 = Deals1.dropna(subset=['CONTACTID'])
Deals1 = Deals1[Deals1['Transaction_Creation_Time'] <= Deals1['Closing_Date']]

# Заполнение пропусков в 'Offer Total Amount' в соответствии с значениями в столбце 'Course duration'

Deals1.loc[(Deals1['Course duration'] == 6) & (Deals1['Offer Total Amount'].isna()), 'Offer Total Amount'] = 1000
Deals1.loc[(Deals1['Course duration'] == 11) & (Deals1['Offer Total Amount'].isna()), 'Offer Total Amount'] = 10000
Deals1['Offer Total Amount'] = Deals1['Offer Total Amount'].replace(to_replace=[0, 1], value=1000)

#очистка и подготовка данных 
Deals1['Initial Amount Paid'] = Deals1['Initial Amount Paid'].replace(to_replace=[1, 6, '6',9, '€ 3.500,00'], value=[100, 600, 600, 900, 3500])
Deals1['Initial Amount Paid'] = Deals1['Initial Amount Paid'].fillna(600)
Deals1['Transaction_Creation_Time'] = pd.to_datetime(Deals1['Transaction_Creation_Time'])
Deals1['Closing_Date'] = pd.to_datetime(Deals1['Closing_Date'])
Deals1['Months of study'] = Deals1['Months of study'].fillna('UNKNOWN')
Deals1['Payment Type'] = Deals1['Payment Type'].fillna('UNKNOWN')
Deals1['Lost Reason'] = Deals1['Lost Reason'].fillna('UNKNOWN')
Deals1['Quality'] = Deals1['Quality'].fillna('UNKNOWN')


# Замена пропущенных значений случайными значениями из списка
possible_values = ['Digital Marketing', 'Web Developer', 'UX/UI Design']
# Функция для генерации случайного значения из списка
def random_product():
    return np.random.choice(possible_values)
Deals1['Product'] = Deals1['Product'].apply(lambda x: random_product() if pd.isna(x) else x)

# # создание отдельного датафрейма с уникальными значениями из столбца 'Quality' и сохранение его в excel

unique_qualities = Deals1[['Quality']].drop_duplicates().reset_index(drop=True)
unique_qualities[['Quality_Code', 'Quality_Description']] = unique_qualities['Quality'].str.split(' - ', expand=True)
unique_qualities.drop(columns=['Quality'], inplace=True)
unique_qualities['Quality_Description'] = unique_qualities['Quality_Description'].fillna('UNKNOWN')


Deals1[['Quality_Code', 'Quality_Description']] = Deals1['Quality'].str.split(' - ', expand=True)
#Deals1.drop(columns=['Quality', 'Quality_Description'], inplace=True)

# Определение порядка кодирования
levels = ['A', 'B', 'C', 'D', 'E', 'UNKNOWN']

# Создание словарей для кодирования и декодирования
encoding_dict = {level: idx for idx, level in enumerate(levels)}
decoding_dict = {idx: level for idx, level in enumerate(levels)}

# Кодирование значений
Deals1['Quality_Code'] = Deals1['Quality_Code'].map(encoding_dict)

# Справочная таблица
unique_qualities.xlsx = pd.DataFrame(list(decoding_dict.items()), columns=['Code', 'Quality', 'Quality_Description'])
#unique_qualities.to_excel('unique_qualities.xlsx', index=True)
print(unique_qualities.xlsx)


#заполнение отсутствующих значений в 'Deal Owner Name' City
Deals1['Deal Owner Name'] = Deals1['Deal Owner Name'].fillna('UNKNOWN')
Deals1['City'] = Deals1['City'].fillna('UNKNOWN')
Deals1['City'] = Deals1['City'].replace(to_replace=['-'] , value='UNKNOWN', regex=False)
Deals1.to_excel('Deals1.xlsx', index=False)

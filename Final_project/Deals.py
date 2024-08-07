import pandas as pd

Deals1 = pd.read_excel("Deals.xlsx")
Deals1 = Deals1.drop_duplicates()
#print(Deals.isnull().sum())
Deals1 = Deals1.dropna(how='all')
#print(Deals.info)
#print(Deals.isnull().sum())
#Deals1.to_excel('Deals1.xlsx', index=False)


Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].fillna('unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='-', value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace=90, value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='.', value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='?', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='25 лет живет в Германии', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='31.05.2024', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='5 июля 2024 сдает экз на В2', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='a2 (b1 экзамен 15 июня)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='A2 (идет доучивать В1 - 300 часов; предположительно до августа)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='A2 (идет на В1)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 15 марта экзамен)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 в июле экзамен)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (B2 должна до конца февраля получить)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (B2 ждет серт)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 не сдал экзамен)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 экзамен 2 марта))', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 экзамен 6 февраля)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (B2 экзамен в январе)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (до февраля)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (b1 (ждет результат)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (ждет результаты В2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (ждет результаты)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (ждет результаты)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (ждет серт)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 (почти, не сдала чуть) + англ В1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (учила, но не сдала В2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 24 февраля экзамен, англ b2', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 9ждет экзамен)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 будет в феврале 2025', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 будет в январе экзамен, готов совмещать', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 в процессе обучения', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 вроде был (18 лет назад сдавал)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 должна получить результаты в феврале', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 есть, ждем B2 в конце месяца', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 еще нет результата', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 ждет результаты', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 ждет серт на днях на руки', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 ждет экзамен в феврале', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1 немецкий и английский Advance', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 результат экзамена в феврале', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 экзамен 26 января', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 экзамен будет 12 апреля', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 экзамен в феврале', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B1, сдает B2 в апреле', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B2 (говорит без проблем - давно здесь)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B2 (ждет итог экзамена)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b2 (ждет серт)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b2 (с1 экзамен 16 февраля)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b2 ждет серт', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='B2+ (не сдавал, но говорит)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Detmold, Paulinenstraße 95, 32756', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='f2', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Lichtenfelser Straße 25, Untersiemau 96253', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='lэкзамен - 6 июля на В1. курсы вечером (но уверенно говорит на B1)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Paderborn 33102, Schwabenweg 10', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Thorn-Prikker-Str. 30, Hagen, 58093', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А1 сертиф, но по факту А2', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='а1-а2 , ая свободный', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( Б1 в июне)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( Б1 март )', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( Б2 в процессе)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( в процессе Б1)', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( повтор на Б1)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( скоро екзамен)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 ( хочет просить совмещать)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='а2 (б1 в сер января)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 (В1 с 3 раза не сдала, бератер видела наши доки)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 (весной - еще 300 часов В1)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 (заканчив В1 в июне)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='а2 (сдавала экз В1, но не сдала похоже)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 (сдает B1 - 12 дек) - не сдал!', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2 нем -В2 англ', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2( включили нем в ангебот)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2( ждет итоги Б!)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2(Б1 в марте экз))', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2(ждет итоги Б1)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='а2, англ B1)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2, в процессе Б1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2-В1 учит', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ая в1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( был екзамен ждет итог )', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( ждет Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( ждет итог )', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( ждет итог Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( ждет результат Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( проходит Б2 )', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 ( проходит Б2)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1 (учит Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б1 заканчивает', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1( может будет)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1?', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б10Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б1-Б2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б1-б2', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б2 ( учит С1)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б2 (с1 ждет рез-тат)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б2( 16.02 экзамен С1)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б2+', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б2-С1)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Без 5 минут B1 (ждет результаты экзамена)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Бй', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='будет B1 в июне', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В январе - В2 сдает', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В январе будут результаты по экзамену на B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1 (уже сдала В2)', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1 (учится на В2 до авг.', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1 (учится на В2 уже)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1 , хочет совмещать с в2', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1 , экзамен на в2 15 декабря)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1 в сентябре', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1 ждем результаты', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1, еще нет сертификата', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1, идет на в2', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1, может уже В2?', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1, учится на В2 до няоб 24', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В1?', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1-ня , в1-ая)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='В2 - не сдал', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Гражданин', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='гражданка', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Гражданка Германии уже год в Германии Учит немецкий и в сентябре b1 через гос-во проходит, а не через ДЖЦ, вечером учится 3 р в неделю с 18 до 21', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждем B1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ждем B1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждем B1 со дня на день', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждет B1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждет результат по B1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждет результат по B1 в феврале', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ждет результаты по B1 экзамену', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ждет сертификат B1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждет со дня на день В1', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='идет на А1', value='A0')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='курс А2-В1 - сдача в июле, но вечерняя смена инт курсов, настроен получить гутшайн уже сейчас.', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='не сдавал, но гражданин', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='не учил', value='A0')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='не учила ( разговорный) сразу пошла работать', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='немецкий - а1-а2, англ b1-b2', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Нет', value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Нет сертификатов, но есть С1 англ, неоконченное высшее в ИТ (и еще одно высшее юридическое) , очень хочет в ИТ, сильно замотивирована именно н', value='0')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='никакой', value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='нулевой уровень, только пошел на курсы.', value=0)
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='НЯ - В1, АЯ - В1', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ня а2, ая в1', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ня-0, ая-B1', value='A0')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ня-0, но англ B2+', value='A0')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='окончание 13.06 курса на b1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Пока А2, сдает 17 05 B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Проходит сейчас B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Проходит сейчас повторно B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='разговорный из украины, без сертификата', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='С1 -ая , Ня -а1', value='C1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Сам оценивает на B2, 13 лет живет в Германии', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Сдавал 8 12 на B1 - ждет результат. 3 01 - аплейт - получил B1!', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='сдавала А2 в сентябре', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Сдала экзамен на B1, ждет в начале февраля результат', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='точно уровень не знаю, но говорить могу - учила сама', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='УТОЧНИТЬ', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='УТОЧНИТЬ!', value='unknown')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='учит A2', value='A1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учится до сентября на B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учится на B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учится на B1 во вторую смену, в первую хочет получить одобрение на обучение у нас', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='ЯЗ: нем В1 был экз 03.05 повтор и сейчас ждет результаты. Технический англ был. А1 сейчас. ОБР: 2 во информационные и комп сети - инженер системоте', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 ждет серт)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (b2 экзамен 2 марта)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='b1 (ждет результат)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2(Б1 в марте экз)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='а2, англ B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б1 (до июля на В2)', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б1 (ждет рез-тат)', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б10Б2', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1 , экзамен на в2 15 декабря', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='в1-ня , в1-ая', value='B1')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Ждем результат по B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учиться до сентября на B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учиться на B1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Учиться на B1 во вторую смену, в первую хочет получить одобрение на обучение у нас', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='б2', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='Б2', value='B2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].replace(to_replace='А2-Б1', value='A2')
Deals1['Level of Deutsch'] = Deals1['Level of Deutsch'].str.upper()


print(Deals1.isnull().sum())


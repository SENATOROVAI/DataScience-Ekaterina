# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

"""Introduction to Data Science."""

# 1. Введение в Data Science.
#
# Data Science - это научная дисциплина, которая включает в себя извлечение
# информации из огромных объемов данных с использованием различных научных
# методов, алгоритмов и процессов. Эта наука помогает обнаруживать в необрабо-
# танных данных скрытые закономерности, при этом она не касается какой-
# то конкретной предметной области, а являет собой сочетание различных дисцип-
# лин, связанных с анализом данных и выдаче «умных» результатов и решений,
# основанных на этих данных.

# ![image.png](attachment:image.png)

# 1.1. Зачем нам Data Science?
#
# 1. задавать правильные вопросы;
# 2. находить основную причину проблемы;
# 3. находить закономерности среди, на первый взгляд, хаотичных необработанных
# данных;
# 4. создавать модели для предиктивного анализа;
# 5. визуализировать и отображать результаты с помощью графиков, информацион-
# ных панелей и т. д.;
# 6. наделять машины интеллектом;
# 7. определять лояльность клиентов с помощью анализа настроений;
# 8. принимать более качественные и быстрые решения;
# 9. рекомендовать правильный продукт нужному клиенту для развития нашего биз-
# неса.
#
# 1.2. История Data Science
#
# Самый ранний способ хранения и анализа данных человеком датируется 18ООО г.
# до н. э. Кость Ишанго, обнаруженная в 1 960 г. на территории современной
# Уганды, считается одним из самых ранних доисторических свидетельств хранения
# данных. Палеолитические племена делали зарубки на палках или костях, чтобы
# вести торговую деятельность или подсчитывать припасы. Они сравнивали палки и
# насечки, выполняя тем самым элементарные расчеты, что позволяло
# предугадывать,
# например, на сколько хватит их запасов еды.
# Около 2400 r. до н. э.
# Счеты - первое устройство, сконструированное специально для выполнения вы-
# числений, впервые стали использоваться в Вавилоне. Примерно в это же время
# появились первые библиотеки - ранние попытки массового хранения данных.
# 1.2.2. Появление статистики
# 1663 год
# В Лондоне ученый Джон Граунт проводит первый зарегистрированный экспери
# мент по статистическому анализу данных. Он предположил, что с помощью имею
# щихся данных о смертности ему удастся разработать систему раннего предупре-
# ждения о бубонной чуме, опустошающей Европу.
# 1865 год
# Ричард Миллар Девенс в своей «Энциклопедии коммерческих и деловых анекдо-
# тов» вводит термин бизнес-аналитика, описывая им то, как банкир Генри Фернезе
# добился преимущества перед конкурентами, собирая, анализируя и структурируя
# информацию, связанную с его коммерческой деятельностью. Этот труд считается
# первым исследованием, в котором анализ данных стал использоваться бизнесом
# в коммерческих целях.
# 1880 год
# У Бюро переписи населения США возникла проблема: по его оценкам, на обработку
# всех данных, собранных в ходе переписи 1 880 г., потребуется 8 лет, а также
# бьло спрогнозировано, что обработка данных переписи 1 890 г. займет более 10
# лет, т.е. эти данные даже не успеют обработать до следующей переписи 1 900
# г. В 1881 г. молодой инженер по имени Герман Холлерит, нанятый Бюро, создает
# нечто, что позже будут называть Табулирующей машиной Холлерита. С помощью
# перфокарт он сократил 1О лет обработки данных до трех месяцев и занял свое
# место в истории как отец-основатель современных автоматизированных
# вычислений. Основанная им компания впоследствии станет называться IВМ.
#
# 1.2.3. Зарождение современного хранения данных
#
# 1926 год
# В интервью журналу Colliers изобретатель Никола Тесла заявляет, что при пра-
# вильном применении беспроводных технологий «всю планету можно превратить
# в огромный мозг, которым она, собственно, и является, ибо всё на ней является
# частицами настоящего и ритмичного целого, а приборы, с помощью которых это
# можно будет сделать, будут удивительно просты по сравнению с нашими ныне-
# шними телефонами. Этот прибор будет умещаться в кармане жилета».
# 1928 год
# Фриц Пфлеумер, немецко-австрийский инженер, изобретает метод магнитного хра-
# нения информации на ленте. Принципы, которые он разработал, используются до
# сих пор, и почти все цифровые данные хранятся на жестких магнитных дисках
# компьютеров.
#
# 1.2.4. Появление больших центров обработки данных
# 1965 год
# Правительство США планирует создать первый в мире центр обработки данных,
# в котором будут храниться 742 миллиона налоговых деклараций и 175 миллионов
# комплектов отпечатков пальцев на магнитной ленте.
# 1.2.5. Появление Интернета
# 1991 год
# Ученый-компьютерщик Тим Бернерс-Ли объявил о рождении того, что позже ста
# нет называться Интернетом, каким мы знаем его сегодня.
# 1997 год
# Появился сервис Google Search, и в течение следующих 20 лет название сервиса
# стало нарицательным, означающим поиск данных в Интернете.
# В том же году запускается журнал «Data Mining and Кnowledge Discovery»,
# причем
# такой порядок этих двух терминов в его названии отражает то, что термин Data
# Mining (сбор данных) стал более популярен, чем Knowledge Discovery
# (извлечение
# информации из больших баз данных).
# 2000 год
# 16 октября 2000 г. бьш выпущен язык Python 2.0 с множеством новых функций,
# включая сборщик мусора с обнаружением циклических ссылок и поддержку
# Unicode.
# 2010 год
# Эрик Шмидт, главный исполнительный директор Google, отметил на конференции,
# что сегодня каждые 2 дня создается столько же данных, сколько было создано
# человечеством с начала цивилизации до 2003 г.
# 2011 год
# В отчете McKinsey говорится, что к 2018 г. США столкнется с нехваткой от 140
# ООО до 190 ООО профессиональных специалистов по обработке данных, а такие
# проблемы, как конфиденциальность, безопасность и интеллектуальная
# собственность, должны быть решены до того, как большие данные раскроют весь
# свой потенциал.
# 2012 год
# В сентябре 2012 г. Том Дэвенпорт и Д. Дж. Патил публикуют статью «Data
# Scientist: The Sexiest Job of the 21st Century» («Специалист по обработке
# данных: самая сексуальная работа XXI века») в журнале Harvard Business
# Review.
# 2014 год
# Наблюдается рост мобильных устройств - для доступа к цифровым данным мо-
# бильные устройства используются чаще, чем офисные и домашние компьютеры.
# 88 % руководителей предприятий, опрошенных GE совместно с Accenture, считают,
# что аналитика больших данных является основным приоритетом для их бизнеса.
#
# 1.3. Настоящее и будущее Data Science
# Сегодня развитие Data Science не закончилось и идет по нескольким
# направлениям:
#
# ♦ Искусственный интеллект (ИИ) - это сфера, в которой основное внимание уде-
# ляется созданию интеллектуальных машин, способных работать и принимать
# решения как человек. Исследования в области ИИ начались около 1936 г., когда
# Алан Тьюринг создал первые машины на базе ИИ. Несмотря на довольно дол-
# гую историю, сегодняшний ИИ в большинстве областей все еще не способен
# полностью заменить человека. Соревнование ИИ с людьми в шахматах и шифро-
# вание данных - это две стороны одной медали.
#
# ♦ Машинное обучение - это инструмент для извлечения знаний из данных.
# В машинном обучении модели могут обучаться на данных самостоятельно или
# поэтапно: обучение с учителем, т.е. на данных, подготовленных человеком, или
# обучение без учителя, в котором работа ведется над хаотичными и неорганизо
# ванными данными.
#
# ♦ Глубокое обучение - это создание многослойных нейронных сетей в областях,
# где требуется более продвинутый или быстрый анализ, а традиционное машин-
# ное обучение не справляется. Под глубиной понимается наличие более одного
# скрытого слоя нейронов в сети, которые проводят математические вычисления.
#
# ♦ Большие данные - это работа с огромными объемами часто неструктуриро-
# ванных данных. Специфика этой сферы - инструменты и системы, способные
# выдерживать высокие нагрузки.
#
# 1.4. Чем занимается специалист по Data Science?
#
# Специалист по анализу данных решает бизнес задачи с помощью следующих шагов:
# 1. Задает правильные вопросы, чтобы понять проблему;
# 2. Собирает данные из нескольких источников - корпоративные данные, общедо-
# ступные данные и т. д.;
# 3. Обрабатывает сырые данные и преобразует их в формат, подходящий для ана-
# лиза;
# 4. Загружает данные в аналитическую систему - алгоритм машинного обучения
# или статистическая модель;
# 5. Подготавливает результаты и идеи, которые можно изложить заинтересованным
# сторонам.
#
# Всё это позволяет решить немало проблем, некоторые из них приведены далее:
# 1. Обнаружение мошенничества и выявление аномалий, например изменений схе-
# мы снятия или расходования средств с кредитной карты клиента;
# 2. Целевой и персонализированный маркетинг - персональные рассылки по эле-
# ктронной почте, системы рекомендаций на сайтах магазинов;
# 3. Метрические прогнозы - показатели эффективности, качества рекламных кам-
# паний и других мероприятий;
# 4. Оценка принятия решений - обработка больших объемов данных и помощь
# в принятии решения, например о выдаче кредита на основе кредитных оценок;
# 5. Прогнозирующее моделирование - прогнозирование столкновения метеорита
# с землей на основе астрономических данных.
# Это лишь малая часть тем, которыми занимается специалист по данным.
#
# 1.5. Что необходимо изучить будущему Data Scientist?
# 1. Программирование
# Для успешного выполнения проекта по Data Science требуются определенные
# навыки программирования. Наиболее распространенными языками программи
# рования являются Python и R.
# 2. Статистика
# Статистика лежит в основе Data Science. Правильная обработка статистики
# может помочь вам извлечь больше информации и получить более значимые
# результаты.
# 3. Базы данных
# Будучи специалистом по данным, вам необходимо понимать, как работают базы
# данных, как ими управлять и как извлекать из них данные.
# 4. Моделирование
# Математические модели позволяют выполнять вычисления и прогнозы на осно-
# ве того, что вы уже знаете о данных. Моделирование также относится к машин-
# ному обучению и включает определение того, какой алгоритм больше подходит
# для решения данной проблемы и как обучать эти модели.
#
# 1.6. Профессии в области Data Science:
# Наиболее известные профессии в Data Science следующие:
#
# 1. Специалист по данным
# Роль: специалист по данным - это профессионал, который манипулирует
# огромными объемами данных для создания серьезных бизнес-концепций, ис-
# пользуя различные инструменты, методы, методологии, алгоритмы и т. д.
# Языки: R, SAS, Python, SQL, Hive, МАТLАВ, Pig, Spark.
# 2. Дата-инженер
# Роль: его роль заключается в работе с большими объемами данных. Он разраба-
# тывает, конструирует, тестирует и поддерживает крупномасштабные системы
# обработки и базы данных.
# Языки: SQL, Hive, R, SAS, МАTLAB, Python, Java, Ruby, С++ и Perl.
# 3. Аналитик данных
# Роль: аналитик данных отвечает за сбор огромных объемов данных. Этот спе-
# циалист будет искать в данных отношения, закономерности и тенденции. Позже
# он составляет убедительную отчетность и визуализацию для анализа данных,
# чтобы принять наиболее жизнеспособные бизнес-решения.
# Языки: R, Python, НТМL, JS, С, С++, SQL.
# 4. Статистик
# Роль: статистик собирает, анализирует и обрабатывает качественные и количе-
# ственные данные, используя статистические теории и методы.
# Языки: SQL, R, МАТLАВ, ТаЫеаu, Python, Perl, Spark и Hive
# 5. Администратор данных
# Роль: администратор данных должен обеспечить доступ к базе данных для всех
# пользователей. Он также следит за тем, чтобы программа работала правильно и
# была защищена от взлома.
# Языки : Ruby on Rails, SQL, Java, С'#' и Python.
# 6. Бизнес-аналитик
# Роль: этот специалист занимается улучшением бизнес-процессов. Он является
# связующим звеном между руководством и IТ-отделом.
# Языки: SQL, Таbleаu, Power BI и Python.
#
# 2.1. От Data Science к программированию
# Что такое программирование?
# Программирование - это идеи, преобразованные в пошаговые
# инструкции, понятные компьютеру. Такая пошаговая инструкция называется алго-
# ритмом. В компьютерных системах алгоритм - это пример логики, написанной
# разработчиками программного обеспечения для эффективного выполнения на
# целевом
# компьютере и для получения некоторых выходных данных по заданным входным дан-
# ным. Оптимальный алгоритм дает более быстрые результаты, чем неоптимальный
# алгоритм для решения той же задачи. Вот почему алгоритмы, как и компьютерное
# оборудование, считаются технологиями.
# В целом алгоритмы состоят из 3 видов операторов, которые могут
# присутствовать в
# различных комбинациях:
# 2.1. Последовательные операторы.
# 2.2. Условные операторы.
# 2.3. Циклы или итерации.
#
# 2.1. Последовательные операторы
# Эти операторы выполняются один за другим, последовательно.
# Пример. Как рассчитать возраст человека по году его рождения.
# Шаг 1 : Начало.
# Шаг 2: Возьмите год рождения человека и сохраните это число как YОВ.
# Шаг 3: Возьмите текущий год и сохраните его как СY.
# Шаг 4: Вычтите YОВ из СY и сохраните как Age.
# Шаг 5: Выведите значение Age.
# Шаг 6: Конец.
#
# 2.2. Условные операторы
# В таких программах некоторая часть программы выполняется в зависимости от
# определенного условия. Если условие верное, компьютер выполняет одну часть
# программы, а если условие неверное, то выполняется другая часть программы.
# Пример. Напишите алгоритм, который проверяет, заболел ли человек. Считаем,
# что человек заболел, если температура его тела выше 37 °С.
# Шаг 1 : Начало.
# Шаг 2: Измерьте температуру и сохраните ее в ТЕМР.
# Шаг 3: Проверьте значение ТЕМР. Если оно превышает 37 градусов, переходите к
# шагу 4,
# в противном случае переходите к шагу 5.
# Шаг 4: Выведите «Пациент болеет» и переходите к шагу 6.
# Шаг 5: Выведите «Пациент здоров».
# Шаг 6: Конец.
#
# 2.З. Цикл или итерации
# В некоторых программах определенный набор действий нужно выполнять снова и
# снова в зависимости от некоторого условия. Эти повторяющиеся действия называ
# ются итерациями. Итерация выполняется с использованием одного или нескольких
# операторов цикла, поэтому программы такого типа называются циклическими или
# повторяющимися.
# Пример. Вывести на экран все числа от 1 до 1О.
# Шаг 1 : Начало.
# Шаг 2: Сохраните значение 1 в i.
# Шаг 3: Проверьте, выполняется ли условие i <= 10. Если да, то переходите к
# шагу 4. Если нет,
# переходите к шагу 7.
# Шаг 4: Выведите значение i на экран.
# Шаг 5: Увеличьте значение i на 1 .
# Шаг 6: Переходите к шагу 3.
# Шаг 7: Конец.
# В этом примере шаги с 3-ro по 5-й повторяются до тех пор, пока условие шага 3
# выполняется. Как только условие станет неверным, цикл завершится.
#
# 2.5. Блок-схемы
# Алгоритмы можно изображать в графической форме с использованием определенных
# обозначений. Полученное изображение называется блок-схемой.
# Вот некоторые виды блоков в блок-схеме алгоритма:
# 1. Функциональный (операторный) блок — указывает действие (шаг) алгоритма.
# 2. Альтернативный блок — указывает наличие выбора среди одного из двух
#  вероятных действий.
# 3. Блок начала/конца — применяется в начале и конце блок-схемы алгоритма.
# 4. Блок ввода-вывода — организует ввод исходных данных и вывод результирующих
# данных.
# 5. Блок цикла — служит для организации циклического процесса с каким-нибудь
# параметром.
# 6. Блок подпрограммы — указывает обращение к отдельным модулям, библиотечным
# подпрограммам, вспомогательным алгоритмам.
# 7. Элемент печати — обозначает вывод результатов на печать.

# ![image.png](attachment:image.png)

# 2.6. Что такое язык программирования?
# Если мы хотим дать компьютеру какие-то указания, нужен язык программирования.
# Разных языков программирования существует очень много. Как и у разговорных
# языков, у всех языков программирования есть свои правила (синтаксис)
# и значения (семантика).
#
# Программа «Hello World!» на С++
# #include <iostream>
# int main ( )
# std : : cout << "Hello World ! " ;
# return О ;
#
# Программа «Hello World!» на Java
# class HelloWorld
# puЫic static void main (String [ ] args )
# System. out . println ( "Hello World ! " ) ;
#
# Программа «Hello World !» на Python
# print ( "Hello World ! " )
# Это простейшая из возможных программ на многих языках, которая обычно ис-
# пользуется для демонстрации. Каковы различия в синтаксисе между языками?
# Во-первых, взглянем на язык программирования С++. Здесь синтаксис состоит из
# двойных кавычек вокруг текста "Hello World! ", точки с запятой в конце
# операторов и ключевого слова return перед закрывающей фигурной скобкой. Всё
# это является частью синтаксиса или правил языка программирования С++.
# Второй пример написан на языке программирования Java. На сегодняшний день это
# один из самых популярных языков, используемых в мобильных приложениях и
# программах в целом. Теперь посмотрим на тот же «Hello World!» на языке
# программирования Python. Это один из самых популярных языков в сфере Data
# Science и машинном обучении. Обратите внимание, что здесь синтаксис
# совершенно
# У всех языков программирования есть свои сильные и слабые стороны. Некоторые
# из них идеально подходят для создания веб-сайтов, другие - для мобильных при-
# ложений, а третьи предназначены для выполнения сложных математических рас-
# четов. Однако, компьютер понимает только машинный язык. Но нам было бы сложно
# писать программ ы напрямую на машинном языке, потому что он очень сложен и
# состоит в основном из последовательностей чисел. Именно поэтому приведенные
# выше языки программирования называются языками высокого уровня.
#
# Исходный код - это то, что пишуг программисты на всех языках программирова
# ния.
# Пример:
# print('Hello world')
#
# Существуют три основных способа перевода исходного кода в машинный код:
# 1. компиляция;
# 2. интерпретация;
# 3. сочетание этих двух способов.

# ![image.png](attachment:image.png)

# Компилятор - это программа, преобразующая исходный код в машинный.
# Языки, относящиеся к компилируемым: С, С++ и Objective С
# Компилятор генерирует автономную программу, написанную на машинном коде,
# далее её исходный код для запуска больше не требуется, работает быстрее.
#
# Интерпретатор - это компьютерная программа, которая непосредственно выполняет
# инструкции, написанные на языке программирования, без предварительной
# компиляции в программу на машинном языке. Интерпритаторы построчно обраба-
# тывают исходный код при каждом запуске, а у пользователя на компьютере должен
# быть установлен необходимый интерпретатор.
# Языки, относящиеся к интерпритируемым: РНР, JavaScript и т. д.
#
# Также существуют языки программирования, в которых используется комбинация
# обоих методов, например Python, Java, С'#'.
#
# 1.5. Что такое интегрированная среда разработки (IDE)?
# Для написания компьютерных программ существуют интегрированные среды
# разработки или IDE (lntegrated Development Environrnent). В этих программах
# есть специальные инструменты, необходимые для написания, отладки и компиляции
# кода.
# Spyder IDE (Scientific Python Development Environment) - это бесплатная
# научная
# среда разработки на Python, которая входит в состав дистрибутива Anaconda
# (пакетное программное обеспечение для Python). В этой TDE есть функции
# pедактирования, проверки, отладки и интерактивного тестирования.
#
# 3. РЕЗЮМЕ:
# 1. Знакомство с Data Science;
# 2. Статистика - это основа принятия всех решений, связанных с данными.
# 3. Знакомство с задачами специалиста по данным, чем она похожа и чем
# 4. Знакомство с программированием
# 5. Python - это единственный язык, который часто используется во всех
# областях, связанных с Data Science.
#

# Ответьте на вопросы:
# 1. Какие предметные области входят в Data Science? Что между ними общего и
# в чем различие?
# Ответ:
# Data Science (DS) — это междисциплинарная область на стыке статистики,
# математики,
# системного анализа и машинного обучения, которая охватывает все этапы работы
# с данными.
#  Везде работа с данными, язык программирования Python.
# 2. Как вы понимаете термин «алгоритм»? Как алгоритмы связаны с блок-схемами?
# Ответ:
# Алгоритм - это строго определнноя последовательность действий. Блок-схемы -
# это способ графического обозначения алгоритма
# 3. Какую программу можно назвать хорошей? Запишите все характеристики, какие
# удастся придумать.
# Ответ:
# есть функции:
# - редактирования;
# - проверки;
# - отладки;
# - интерактивного тестирования
# 4. Какой язык понимает компьютер?
# Ответ:
# Машинный язык.
# 5 . Чем языки программирования отличаются от языков, на которых мы говорим?
# Ответ:
# Язык программирования - это набор команд. Компьютер воспринимает программу,
# преобразованную
# в машинный код, только как руководство к действию.
# Естественные языки несравнимо сложнее любых языков программирования.
# Человеческие языки,
# помимо передачи информации, служат еще и для выражения эмоций, кроме того
# контекст может
# менять смысл. Язык программирования всегда однозначен и неясности толкования
# не терпит.
#

# 1.5.2. Правда или ложь.
# 1. Правда
# 2. Ложь
# 3. Ложь
# 4. Правда
# 5. Ложь
# 6. Ложь
# 7. Правда
# 8. Ложь
# 9. Правда
# 10.Ложь

# 1.5.3. Практические задания
# 1. Напишите алгоритм для расчета простых процентов от некоторой суммы.
# Шаг 1: Начало.
# Шаг 2: Запросить у пользователя сумму, одновременно присвоить данные
# переменной summ.
# Шаг 3: Запросить у пользователя размер процентов, одновременно присвоить
# данные
# переменной perc.
# Шаг 4: Переменной res присвоить формулу summ разделить на 100 и умножить на
# perc.
# Шаг 5: Вывести на экран значение res.
# Шаг 6: Конец.
#
# 2. Напишите алгоритм для вычисления площади прямоугольника.
# Шаг 1: Начало.
# Шаг 2: Запросить у пользователя значение длины, одновременно присвоить
# данные переменной a.
# Шаг 3: Запросить у пользователя значение ширины, одновременно присвоить
# данные переменной b.
# Шаг 4: Переменной res присвоить формулу a умножить на b.
# Шаг 5: Вывести на экран значение res.
# Шаг 6: Конец.
#
# 3 . Напишите алгоритм вычисления периметра круга.
# Шаг 1: Начало.
# Шаг 2: Запросить у пользователя значение радиуса окружности, одновременно
# присвоить
# данные переменной r.
# Шаг 3: Переменной res присвоить формулу 2 умножить на 3.14 и умножить на r.
# Шаг 5: Вывести на экран значение res.
# Шаг 6: Конец.
#
# 4. Напишите алгоритм, который находит все простые числа меньше 100.
# Шаг 1: Начало.
# Шаг 2: Перебрать все элементы в заданом диапазоне = от 2 до 101.
# Шаг 3: Проверить для каждого числа, есть ли у него какой-либо множитель
# между 1 и самим собой.
# Шаг 4: Если да, то число не простое, и оно перейдет к следующему числу.
# Шаг 5: Если нет, то это простое число, и программа автоматически выведет его
# на экран.
# Шаг 6: Цикл автоматически прервется, когда будет достигнуто верхнее значение.

for item in range(2, 101):
    if item > 1:
        for jey in range(2, item):
            if item % jey == 0:
                break
        else:
            print(item)

# 5. Напишите алгоритм превращения предложения, написанного в верхнем регистре,
# в обычный для
# предложений регистр.
# Шаг 1: Начало.
# Шаг 2: Присваиваем переменной с строку.
# Шаг 3: Путем среза присваиваем первую букву (под нулевым индексом)
# переменной first_letter.
# Шаг 5: Путем среза убираем из строки первую букву, используем метод lower.
# Шаг 6: Присваиваем переменной res зачение конкатинации переменных
# first_letter и с.
# Шаг 7: Выводим на печать переменную res.
# Шаг 8: Конец.

word = "Я ПОШЛА ГУЛЯТЬ"
first_letter = word[:1]
word = word[1:].lower()
res = first_letter + word
print(res)
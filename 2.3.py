'''
Задани2.3 Реализовать приложение, моделирующее очереди в
следующих условиях. В офисе имеется принтер, очередь печати которого
необходимо организовать по следующим правилам:
• Документы на печать имеют атрибуты: отправитель и ожидаемое время
печати.
• Отправители имеют приоритет по захвату принтера в следующем
порядке: директор, менеджер по продажам, бухгалтер, секретарь,
системный администратор.
• Также при выборе задания на печать имеет значение ожидаемое время
печати: чем больше это время, тем ниже приоритет.
Вход: текстовый файл с строками <отправитель> <ожидаемое время
печати>, терминал с теми же парами на добавление сообщений.
Выход: терминал с очередью.
'''

import re
import sys

# функция получения ключа по значению
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# открытие и считывание файла
file_queue = open('queue.txt', 'r', encoding="utf-8")
read_file = file_queue.read().splitlines()
if len(read_file) == 0:
	print('Файл пуст!')
	sys.exit()
file_queue.close()

# определение должностей и ожидаемого времени на печать
# и сортировка по должностям (в словаре read_queue должности выстроены по убыванию)
read_queue = {'директор':'', 'менеджер по продажам':'', 'бухгалтер':'', 'секретарь':'', 'системный администратор':''}
for i in range(len(read_file)):
	re_queue = re.search(r'\w+?[ -]?\w+?[ -]?\w+\s[-]\s', read_file[i])
	re_time = re.search(r'\d+?[ ]?[ч]?[ ]?\d{,2}[ ][м][и][н]', read_file[i])
	time_split = re_time[0].split()
	if len(time_split) == 4:
		ready_time = int(time_split[0]) * 60 + int(time_split[2])
	elif len(time_split) == 2:
		ready_time = int(time_split[0])
	read_queue[re_queue[0][:-3].lower()] = ready_time

mas_time = list(read_queue.values())
# удаление пустых значений
for i in range(len(mas_time)-1):
	if mas_time[i] == "":
		mas_time.pop(i)

# сортировка по требуемому времени на печать
# если разница времени на печать (у директора и менеджера по продажам больше 10 минут, то меняем их местами, между директором и бухгалтером 15 мин и т.д.)
diff = [0, 10, 15, 20, 25]
schet = 0
for i in range(len(mas_time)):
	for j in range(i, len(mas_time)):
		if int(mas_time[i]) - mas_time[j] > diff[j]:
			mas_time.insert(schet, mas_time.pop(j))
			schet += 1
			break

# определение должности по сортированному времени
edit_queue = []
for i in mas_time:
	edit_queue.append(get_key(read_queue, i))
	a = read_queue.pop(get_key(read_queue, i))

# вывод итоговой очереди
for i in edit_queue:
	print(i)
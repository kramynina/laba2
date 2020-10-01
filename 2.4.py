'''
Задание 2.4. Напишите программу, которая моделирует карточную игру и определяет, кто
выигрывает.
• В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со
значением 0 побеждает карту 9.
• Карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья
карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без
карт – проигрывает.
• Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта
побеждает самую старшую карту ("шестерка берет туза").
• Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого игрока, затем карту
второго игрока (то есть карта второго игрока оказывается внизу колоды).
• Входные данные. Программа получает на вход две строки: первая строка содержит 5 чисел,
разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт второго
игрока. Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая
будет открыта первой.
• Выходные данные. Программа должна определить, кто выигрывает при данной раздаче, и
вывести слово first или second, после чего вывести количество ходов, сделанных до выигрыша.
Если на протяжении 10^6 ходов игра не заканчивается, программа должна вывести сообщение too
long.
'''

import sys
import random
import re


def check_kards(player_kards, player_str, koloda):
	mas_player = re.findall(r'\d', player_str)
	if len(mas_player) != 5:
		print('Ошибка! У игрока должно быть 5 карт! (Проверьте правильность введенных цифр)')
		sys.exit()
	for i in mas_player:
		if int(i) not in koloda:
			print('Ошибка! Не все введенные карты есть в колоде!')
			sys.exit()
		else:
			player_kards.insert(0, koloda.pop(koloda.index(int(i))))

	return player_kards, koloda


def rules(first, second):
	win = True
	if (first == 0 and second == 9) or (second == 0 and first == 9):
		if first == 0 and second == 9:
			win = True
		if second == 0 and first == 9:
			win = False
	else:
		if first > second:
			win = True
		else:
			win = False

	return win, first, second


def edit_koloda(player, first, second):
	player.insert(0, first)
	player.insert(0, second)

	return player

koloda = [0,1,2,3,4,5,6,7,8,9]
player_1 = []
player_2 = []

first_player = input('Введите 5 карт первого игрока через пробел : ')
player_1, koloda = check_kards(player_1, first_player, koloda)

second_player = input('Введите 5 карт второго игрока через пробел : ')
player_2, koloda = check_kards(player_2, second_player, koloda)
#print('Исходная колода первого игрока : ', player_1)
#print('Исходная колода второго игрока : ', player_2)

schet = 0
while not (len(player_1) == 0 or len(player_2) == 0):
	round_, first, second = rules(player_1.pop(len(player_1)-1), player_2.pop(len(player_2)-1))

	if round_:
		player_1 = edit_koloda(player_1, first, second)
		#print('шаг : ', schet+1)
		#print('1: ', player_1)
		#print('2: ', player_2)
	else:
		player_2 = edit_koloda(player_2, first, second)
		#print('шаг : ', schet+1)
		#print('1: ', player_1)
		#print('2: ', player_2)
	schet += 1

	if schet == 10**6:
		print('too long')
		sys.exit()

if len(player_1) == 0:
	print('second')
	print('количество ходов : ', schet)
elif len(player_2) == 0:
	print('first')
	print('количество ходов : ', schet)
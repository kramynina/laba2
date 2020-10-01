'''
Задание 2.2. Реализовать программу, содержащую описание дека и моделирующую работу дека, работающую по заданным правилам.
• Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды выводится протокол с результатами работы по заданным правилами.
'''

import random
import sys


# ввод размера дека (<=100)
def input_size_deq():
    size_deq = input('Введите желаемый размер дека (<=100): ')
    try:
        size_deq = int(size_deq)
        if size_deq > 100:
            print('Размер дека превышает 100 элементов!')
            sys.exit()
    except ValueError:
        print('Размер дека должен быть целым числом!')
        sys.exit()

    return size_deq


# генерация дека от 0 до 99 по заданному размеру
def generate_deq(size):
    st = []
    for i in range(size):
        st.append(random.randint(0, 99))

    return st


# Добавление элемента в начало дека
def command_push_front(deq, number):
    if len(deq) == 100:
        print('Выполнение команды невозможно! В деке 100 элементов!')
    else:
        deq.insert(0, number)
        print('ok')
    get_commands(deq)


# Добавление элемента в конец дека
def command_push_back(deq, number):
    if len(deq) == 100:
        print('Выполнение команды невозможно! В деке 100 элементов!')
    else:
        deq.append(number)
        print('ok')
    get_commands(deq)


# Удаление первого элемента дека
def command_pop_front(deq):
    if len(deq) == 0:
        print('error')
    else:
        print(deq.pop(0))
    get_commands(deq)


# Удаление последнего элемента дека
def command_pop_back(deq):
    if len(deq) == 0:
        print('error')
    else:
        print(deq.pop())
    get_commands(deq)


# Вывод первого элемента дека
def command_front(deq):
    if len(deq) == 0:
        print('error')
    else:
        print(deq[0])
    get_commands(deq)


# Вывод последнего элемента дека
def command_back(deq):
    if len(deq) == 0:
        print('error')
    else:
        print(deq[len(deq) - 1])
    get_commands(deq)


# Вывод размера дека
def command_size(deq):
    print(len(deq))
    get_commands(deq)


# Очистка дека
def command_clear(deq):
    deq.clear()
    print('ok')
    get_commands(deq)


# Выход из программы
def command_exit():
    print('bye')
    sys.exit()


def error_input(deq):
    print('Недопустимая команда!')
    get_commands(deq)


def get_commands(deq):
    valid_commands = ['push_front', 'push_back', 'pop_front', 'pop_back', 'front', 'back', 'size', 'clear', 'exit']
    # print(deq)
    print('\nВведите команду: ')
    commands = input()
    commands = commands.lower()
    command = commands.split(' ')
    if command[0] in valid_commands:
        if len(command) == 2:
            if command[0] == 'push_front':
                try:
                    num = int(command[1])
                    command_push_front(deq, num)
                except ValueError:
                    print('После команды "push_front" должно быть целое число!')
                    get_commands(deq)
            elif command[0] == 'push_back':
                try:
                    num = int(command[1])
                    command_push_back(deq, num)
                except ValueError:
                    print('После команды "push_back" должно быть целое число!')
                    get_commands(deq)
            else:
                error_input(deq)

        elif len(command) == 1:
            if command[0] == 'pop_front':
                command_pop_front(deq)
            elif command[0] == 'pop_back':
                command_pop_back(deq)
            elif command[0] == 'front':
                command_front(deq)
            elif command[0] == 'back':
                command_back(deq)
            elif command[0] == 'size':
                command_size(deq)
            elif command[0] == 'clear':
                command_clear(deq)
            elif command[0] == 'exit':
                command_exit()
            elif command[0] == 'push_front' or command[0] == 'push_back':
                print(f'После команды {command[0]} через пробел должно идти целое число')
                get_commands(deq)
            else:
                error_input(deq)
        else:
            error_input(deq)
    else:
        error_input(deq)


def start():
    size = input_size_deq()
    deq = generate_deq(size)
    if len(deq) == 0:
        print('Дек пуст.')
    else:
        print(deq)
    get_commands(deq)


start()
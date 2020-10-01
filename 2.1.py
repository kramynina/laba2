'''
Задание 2.1. Реализовать программу, содержащую описание
стека и моделирующую работу стека со следующими функциями.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
После выполнения каждой команды выводится протокол с результатами работы по заданным правилами.
'''

import random
import sys


# ввод размера стека (<=100)
def input_size_stack():
    size_stack = input('Введите желаемый размер стека (<=100): ')
    try:
        size_stack = int(size_stack)
        if size_stack > 100:
            print('Размер стека превышает 100 элементов!')
            sys.exit()
    except ValueError:
        print('Размер стека должен быть целым числом!')
        sys.exit()

    return size_stack


# генерация стека от 0 до 99 по заданному размеру
def generate_stack(size):
    st = []
    for i in range(size):
        st.append(random.randint(0, 99))

    return st


# Добавление элемента в конец стека
def command_push(stack, number):
    if len(stack) == 100:
        print('Выполнение команды невозможно! В стеке 100 элементов!')
    else:
        stack.append(number)
        print('ok')
    get_commands(stack)


# Удаление последнего элемента стека
def command_pop(stack):
    if len(stack) == 0:
        print('Выполнение команды невозможно! Стек пуст!')
    else:
        print(stack.pop())
    get_commands(stack)


# Вывод последнего элемента стека
def command_back(stack):
    if len(stack) == 0:
        print('Выполнение команды невозможно! Стек пуст!')
    else:
        print(stack[len(stack) - 1])
    get_commands(stack)


# Вывод размера стека
def command_size(stack):
    print(len(stack))
    get_commands(stack)


# Очистка стека
def command_clear(stack):
    stack.clear()
    print('ok')
    get_commands(stack)


# Выход из программы
def command_exit():
    print('bye')
    sys.exit()


def error_input(stack):
    print('Недопустимая команда!')
    get_commands(stack)


def get_commands(stack):
    valid_commands = ['push', 'pop', 'back', 'size', 'clear', 'exit']
    # print(stack)
    print('\nВведите команду: ')
    commands = input()
    commands = commands.lower()
    command = commands.split(' ')
    if command[0] in valid_commands:
        if len(command) == 2:
            if command[0] == 'push':
                try:
                    num = int(command[1])
                    command_push(stack, num)
                except ValueError:
                    print('После команды "push" должно быть целое число!')
                    get_commands(stack)
            else:
                error_input(stack)
        if len(command) == 1:
            if command[0] == 'pop':
                command_pop(stack)
            elif command[0] == 'back':
                command_back(stack)
            elif command[0] == 'size':
                command_size(stack)
            elif command[0] == 'clear':
                command_clear(stack)
            elif command[0] == 'exit':
                command_exit()
            else:
                error_input(stack)
        else:
            error_input(stack)
    else:
        error_input(stack)


def start():
    size = input_size_stack()
    stack = generate_stack(size)
    if len(stack) == 0:
        print('Стек пуст.')
    else:
        print(stack)
    get_commands(stack)


start()
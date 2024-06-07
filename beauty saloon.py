from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm
from rich import print
from rich.table import Table

console = Console()

name_ = []
items = []
time_ = []
date_ = []
cost_ = []


def info():
    procedure = input('На какую процедуру хотели бы записаться?'
                      '(маникюр/педикюр/СПА/стрижка: ')
    day = input('На какой день записываетесь? ')
    start_time = input('В какое время Вам удобно подойти? ')
    client = input('Уточните Ваше имя: ')
    cost = int(input('Уточните цену процедуры: '))
    items.append(procedure)
    date_.append(day)
    time_.append(start_time)
    name_.append(client)
    cost_.append(cost)


def check_price():
    console.print(Panel(
        Text(
            f'''
        Маникюр - 1300 ₽
        Педикюр - 1500 ₽
        СПА - 2000 ₽
        Стрижка - 800 ₽
            '''
        ),
        title='Price',
        width=34
    ))


def check_params():
    global items
    global name_
    global time_
    global date_
    global cost_
    table = Table(title="Ваша запись")

    table.add_column("Название процедуры")
    table.add_column("Дата записи")
    table.add_column("Время записи")
    table.add_column('Стоимость услуги')
    table.add_column("Ваше имя")

    table.add_row(f'{items}', f'{date_}', f'{time_}', f'{cost_}', f'{name_}')
    console.print(table)


def cancel_appointment():
    name_.clear()
    items.clear()
    time_.clear()
    date_.clear()
    console.print('Ваша запись отменена! ')


def create_check():
    total_price = sum([int(i) for i in cost_])
    salon_name = 'Stilnyashka'
    console.print(Panel(
        Text(
            f'''
           Запись успешно завершена!
               Будем Вас ждать!
           ___________________________
           Клиент: {name_[0]}
           Процедура: {items[0]}
           Дата записи: {date_[0]}
           Время записи: {time_[0]}
           Общая цена: {total_price[0]} ₽
           Название салона: {salon_name[0]}

                   ''',
        ),
        title='Чек',
        width=50
    ))


def run():
    console.print(Panel(Text(
        '''  Добро пожаловать в салон 
        Stilnyashka! 
    1. Записаться на процедуру
    2. Посмотреть прайс
    3. Проверить запись
    4. Отменить запись
    5. Создать чек
    6. Завершить работу '''),
        title='Beauty saloon',
        width=34
    ))
    while True:
        print()
        oper = console.input('Что хочешь сделать? (1-6) ')
        if oper == '1':
            info()
        elif oper == '2':
            check_price()
        elif oper == '3':
            check_params()
        elif oper == '4':
            cancel_appointment()
        elif oper == '5':
            create_check()
        elif oper == '6':
            if Confirm.ask('Вы действительно хотите выйти? '):
                break
        else:
            console.print('Что-то не то!')


run()

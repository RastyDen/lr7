#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

import sys
import json

if __name__ == '__main__':
    # Список магазинов.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            product = input("Название товара? ")
            shop = input("Название магазина? ")
            price = float(input("Стоимость товара в руб.? "))

            # Создать словарь.
            markets = {
                'product': product,
                'shop': shop,
                'price': price,
            }

            # Добавить словарь в список.
            market.append(markets)
            # Отсортировать список в случае необходимости.
            if len(market) > 1:
                market.sort(key=lambda item: item.get('product', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Товар",
                    "Магазин",
                    "Стоимость в руб."
                )
            )
            print(line)

            # Вывести данные о всех товарах.
            for idx, markets in enumerate(market, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        markets.get('product', ''),
                        markets.get('shop', ''),
                        markets.get('price', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=2)
            period = str(parts[1])

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения товара из списка.
            for markets in market:
                if markets.get('product') >= period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('product', ''))
                    )
                    print('Название магазина:', markets.get('shop', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то товары не найдены.
            if count == 0:
                print("Продукт не найден.")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                market = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(market, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n"
                  "add - добавить продукт\n"
                  "list - вывести список продуктов\n"
                  "select <товар> - информация о товаре\n"
                  "help - отобразить справку\n"
                  "exit - завершить работу с программой\n"
                  "load <имя файла> - загрузить данные из файла\n"
                  "save <имя файла> - сохранить данные в файл")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

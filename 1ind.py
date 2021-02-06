#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, начинающиеся с тире, перед которым могут находиться только пробельные
# символы.

from typing import List
import sys

if __name__ == '__main__':
    with open('ind1.txt', 'r', encoding="utf8") as f:
        text = f.read()

    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    # Разбить текст на предложения.
    sentences = text.split('.')

    # Удаление пробельных символов.
    sentences = [i.strip() for i in sentences]

    # Вывод предложений начинающихся с тире.
    for sentence in sentences:
        if '-' in sentence[:1]:  # или if sentence.startswith('-')
            print(sentence)


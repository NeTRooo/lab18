#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        dictionary = {line.strip().lower() for line in f}
    return dictionary

def spell_check(input_file, dictionary):
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            words = line.strip().split()
            for word in words:
                if word.lower() not in dictionary:
                    print(f"Ошибка в строке {line_number}: '{word}'")
                    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python ind2.py <имя_файла>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        dictionary = load_dictionary("dictionary.txt")
    except FileNotFoundError:
        print("Ошибка: Файл словаря не найден.")
        sys.exit(1)

    try:
        spell_check(input_file, dictionary)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        sys.exit(1)

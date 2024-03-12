#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def capitalize_vowels(text):
    words = text.split()
    for i in range(len(words)):
        if words[i][0].isalpha() and is_vowel(words[i][0]):
            words[i] = words[i][0].lower() + words[i][1:]
    return ' '.join(words)

def main():
    file_name = input("Введите имя файла: ")
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            capitalized_text = capitalize_vowels(text)
            print("Текст с заменёнными гласными буквами:")
            print(capitalized_text)
    except FileNotFoundError:
        print("Файл не найден.")

if __name__ == "__main__":
    main()

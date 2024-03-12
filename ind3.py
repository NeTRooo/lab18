#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def count_files_by_extension(directory, extension):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.' + extension):
            count += 1
    return count

if __name__ == "__main__":
    extension = 'txt'
    file_count = count_files_by_extension(os.getcwd(), extension)
    print(f"Количество файлов с расширением .{extension} в директории {os.getcwd()}: {file_count}")
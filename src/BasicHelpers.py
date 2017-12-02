# -*- coding: utf-8 -*-

import os
import sys
import codecs
import time
import shutil


def load_lines_from_file(filename, encoding = "utf-8", strip = False):
    with codecs.open(filename, 'r', encoding) as in_file:
        return [ line.strip() for line in in_file.readlines() ] if strip else in_file.readlines()


def convert_encoding(filename, src_encoding, dst_encoding):
    with codecs.open(filename, 'r', src_encoding) as src_file: data = src_file.read()
    with codecs.open(filename, 'w', dst_encoding) as dst_file: dst_file.write(data)


def dump_list_to_file(input_list, output_filename, line_breaker = '', encode = 'utf-8'):
    if len(input_list) > 0:
        with codecs.open(output_filename, 'w', encode) as output_file:
            output_file.write(line_breaker.join(input_list))


def replace_extension(filename, src_extension, dst_extension):
    portion = os.path.splitext(filename)
    return (portion[0] + dst_extension) if (portion[1] == src_extension) else filename


def get_all_files(root_dir, extension):
    ret_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                ret_files.append(os.path.join(root, file))
    return ret_files


def clear_dir(input_dir):
    if os.path.isdir(input_dir):
        shutil.rmtree(input_dir)
    time.sleep(1)
    os.mkdir(input_dir)


def string_start_with(judge_string, pattern):
    return judge_string.strip().find(pattern) == 0


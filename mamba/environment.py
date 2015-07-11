import os
from timeit import default_timer
import mamba
import mamba.ast as ast
import mamba.symbol_table
import math
import random
import sys


def substr(s: str, start: int, length: int):
    return s[start:start + length]


def str_pos(sub: str, string: str):
    return string.index(sub)


def str_format(string, *args):
    return string % tuple(args)


def array_push(arr: list, value):
    arr.append(value)


def array_pop(arr: list):
    return arr.pop()


def array_insert(arr: list, i: int, x):
    arr.insert(i, x)


def array_remove(arr: list, i: int):
    return arr.pop(i)


def array_reverse(arr: list):
    arr.reverse()


def array_sort(arr: list):
    arr.sort()

def file_close(f):
    f.close()

def file_write(f, data):
    f.write(data)

def file_read(f, size = None):
    return f.read(size)

def file_seek(f, offset):
    return f.seek(offset)

def file_pos(f):
    return f.tell()

def file_exists(f):
    return os.path.isfile(f)


def declare_env(s: mamba.symbol_table.SymbolTable):
    f = ast.BuiltInFunction

    # "constants"
    s.set_sym('pi', math.pi)
    s.set_sym('e', math.e)

    # globals
    s.set_sym('argv', sys.argv)

    # Built in functions

    # math
    s.set_func('int', f(int))
    s.set_func('float', f(float))
    s.set_func('round', f(round))
    s.set_func('abs', f(abs))
    s.set_func('log', f(math.log))
    s.set_func('log2', f(math.log))
    s.set_func('rand', f(random.random))
    s.set_func('randrange', f(random.randrange))

    s.set_func('sin', f(math.sin))
    s.set_func('cos', f(math.cos))
    s.set_func('tan', f(math.tan))
    s.set_func('atan', f(math.atan))

    # string
    s.set_func('substr', f(substr))
    s.set_func('len', f(len))
    s.set_func('pos', f(str_pos))
    s.set_func('upper', f(str.upper))
    s.set_func('lower', f(str.lower))
    s.set_func('replace', f(str.replace))
    s.set_func('format', f(str_format))
    s.set_func('str', f(str))

    # misc
    s.set_func('chr', f(chr))
    s.set_func('ord', f(ord))
    s.set_func('time', f(default_timer))

    # arrays
    s.set_func('array_insert', f(array_insert))
    s.set_func('array_pop', f(array_pop))
    s.set_func('array_push', f(array_push))
    s.set_func('array_remove', f(array_remove))
    s.set_func('array_reverse', f(array_reverse))
    s.set_func('array_sort', f(array_sort))

    # file
    s.set_func('file', f(open))
    s.set_func('file_close', f(file_close))
    s.set_func('file_write', f(file_write))
    s.set_func('file_read', f(file_read))
    s.set_func('file_seek', f(file_seek))
    s.set_func('file_pos', f(file_pos))
    s.set_func('file_exists', f(file_exists))

    # input
    s.set_func('ask', f(input))
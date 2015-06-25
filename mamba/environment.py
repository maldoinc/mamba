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


def declare_env(s: mamba.symbol_table.SymbolTable):
    f = ast.BuiltInFunction

    # "constants"
    s.setsym('pi', math.pi)
    s.setsym('e', math.e)

    # globals
    s.setsym('argv', sys.argv)

    # Built in functions

    # math
    s.setfunc('int', f(int))
    s.setfunc('float', f(float))
    s.setfunc('round', f(round))
    s.setfunc('abs', f(abs))
    s.setfunc('log', f(math.log))
    s.setfunc('log2', f(math.log))
    s.setfunc('rand', f(random.random))
    s.setfunc('randrange', f(random.randrange))

    s.setfunc('sin', f(int))
    s.setfunc('cos', f(int))
    s.setfunc('tan', f(math.tan))
    s.setfunc('atan', f(math.atan))

    # string
    s.setfunc('substr', f(substr))
    s.setfunc('len', f(len))
    s.setfunc('pos', f(str_pos))
    s.setfunc('upper', f(str.upper))
    s.setfunc('lower', f(str.lower))
    s.setfunc('replace', f(str.replace))
    s.setfunc('format', f(str_format))
    s.setfunc('str', f(str))

    # misc
    s.setfunc('chr', f(chr))
    s.setfunc('ord', f(ord))
    s.setfunc('time', f(default_timer))

    # arrays
    s.setfunc('array_insert', f(array_insert))
    s.setfunc('array_pop', f(array_pop))
    s.setfunc('array_push', f(array_push))
    s.setfunc('array_remove', f(array_remove))
    s.setfunc('array_reverse', f(array_reverse))
    s.setfunc('array_sort', f(array_sort))

    # file
    s.setfunc('file', f(open))
    s.setfunc('file_close', f(file_close))
    s.setfunc('file_write', f(file_write))
    s.setfunc('file_read', f(file_read))
    s.setfunc('file_seek', f(file_seek))
    s.setfunc('file_pos', f(file_pos))

    # input
    s.setfunc('ask', f(input))
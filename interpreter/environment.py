import interpreter.ast as ast
import math
import time


def substr(s: str, start: int, length: int):
    return s[start:start + length]


def str_pos(sub: str, string: str):
    return string.index(sub)


def str_format(string, *args):
    return string % tuple(args)


def declare_env(s: ast.SymbolTable):
    f = ast.BuiltInFunction

    # "constants"
    s.setsym('pi', math.pi)
    s.setsym('e', math.e)

    # Built in functions

    # math
    s.setfunc('int', f(int))
    s.setfunc('float', f(float))
    s.setfunc('round', f(round))
    s.setfunc('abs', f(abs))
    s.setfunc('log', f(math.log))
    s.setfunc('log2', f(math.log))

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
    s.setfunc('time', f(time.time))
import math


class Environment(object):
    symtable = {}
    runtime = {
        'methods': {
            'abs': abs,
            'sin': math.sin,
            'log': math.log
        },

        'const': {
            'e': math.e,
            'pi': math.pi
        }
    }

    def resolve(self, sym):
        return self.get_sym(sym) if self.has_sym(sym) else sym

    def has_sym(self, sym):
        return self.is_var(sym) or self.is_const(sym)

    def is_var(self, sym):
        return self.symtable.get(sym, None) is not None

    def define(self, sym, val):
        self.symtable[sym] = val

    def undef(self, sym):
        self.symtable[sym] = None

    def is_const(self, sym):
        return sym in self.runtime['const'].keys()

    def get_sym(self, sym):
        return self.runtime['const'][sym] if self.is_const(sym) else self.symtable[sym]

    def get_method(self, sym):
        return self.runtime['methods'][sym]
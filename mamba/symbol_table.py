from mamba.exceptions import *


class SymbolTable:
    __func = 'functions'
    __sym = 'symbols'
    __local = 'local'

    __table = {
        __func: {},
        __sym: {},
        __local: []
    }

    def __is_local(self):
        '''
        Returns true if symbol table is being called from inside
        a function rather than the global scope

        :return: bool
        '''
        return len(self.__table[self.__local]) > 0

    def table(self):
        return self.__table

    def get_local_table(self):
        '''
        Returns the active local symbol table (the last one on the stack)
        '''

        t = self.__table[self.__local]

        return t[len(t) - 1]

    def set_local(self, flag):
        if flag:
            self.__table[self.__local].append({})
        else:
            self.__table[self.__local].pop()

    def get_sym(self, sym):
        if self.__is_local():
            # Check all the local symbol tables starting from the current one
            for tab in reversed(self.__table[self.__local]):
                if sym in tab:
                    return tab[sym]

        # if not found check the global scope
        if sym in self.__table[self.__sym]:
            return self.__table[self.__sym][sym]

        # nope... sorry :(
        raise SymbolNotFound("Undefined variable '%s'" % sym)

    def set_sym(self, sym, val):
        if self.__is_local():
            self.get_local_table()[sym] = val
        else:
            self.__table[self.__sym][sym] = val

    def get_func(self, name):
        if name in self.__table[self.__func]:
            return self.__table[self.__func][name]

        raise SymbolNotFound("Undefined function '%s'" % name)

    def set_func(self, name, val):
        if name in self.__table[self.__func]:
            raise DuplicateSymbol("Cannot redeclare function '%s'" % name)

        self.__table[self.__func][name] = val

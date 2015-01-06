class SymbolTable:
    __table = {}

    def getsym(self, sym: str, scope: str='global'):
        return self.__table[scope][sym]

    def setsym(self, sym: str, val, scope: str='global'):
        self.__table[scope][sym] = val

symbols = SymbolTable()


class BaseExpression:
    def eval(self, scope):
        raise NotImplementedError()


class Identifier(BaseExpression):
    def __init__(self, name: str):
        self.name = name

    def assign(self, val, scope):
        symbols.setsym(self.name, val, scope)

    def eval(self, scope):
        pass


class Assignment(BaseExpression):
    def __init__(self, identifier: Identifier, val: BaseExpression):
        self.identifier = identifier
        self.val = val

    def eval(self, scope):
        self.identifier.assign(self.val.eval(scope), scope)

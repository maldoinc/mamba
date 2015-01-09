class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def eval(self):
        for n in self.children:
            res = n.eval()

            if res is not None:
                return res


class SymbolTable:
    __table = {}

    def getsym(self, sym, scope='global'):
        return self.__table[scope][sym]

    def setsym(self, sym, val, scope='global'):
        self.__table[scope][sym] = val


symbols = SymbolTable()


class BaseExpression:
    def eval(self, scope):
        raise NotImplementedError()


class Numeric(BaseExpression):
    def __init__(self, value):
        self.value = value

    def eval(self, scope):
        return self.value


class Identifier(BaseExpression):
    def __init__(self, name):
        self.name = name

    def assign(self, val, scope):
        symbols.setsym(self.name, val, scope)

    def eval(self, scope):
        pass


class Assignment(BaseExpression):
    def __init__(self, identifier, val):
        self.identifier = identifier
        self.val = val

    def eval(self, scope):
        self.identifier.assign(self.val.eval(scope), scope)

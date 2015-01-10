import operator

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

    def table(self):
        return self.__table

    def getsym(self, sym, scope):
        return self.__table[sym]

    def setsym(self, sym, val, scope):
        self.__table[sym] = val


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

class BinaryOperation(BaseExpression):
    __operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '**': operator.pow,
        '/': operator.truediv
    }

    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def eval(self, scope):
        return self.__operations[self.op](self.left.eval(scope), self.right.eval(scope))

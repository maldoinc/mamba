import operator


class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __repr__(self):
        return '<Instruction list: {0}>'.format(self.children)

    def eval(self):
        for n in self.children:
            res = n.eval()

            if res is not None:
                return res


class SymbolTable:
    __table = {}

    def table(self):
        return self.__table

    def getsym(self, sym):
        return self.__table[sym]

    def setsym(self, sym, val):
        self.__table[sym] = val


symbols = SymbolTable()


class BaseExpression:
    def eval(self):
        raise NotImplementedError()


class Primitive(BaseExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Primitive: "{0}"({1})>'.format(self.value, self.value.__class__)

    def eval(self):
        return self.value


class Identifier(BaseExpression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Identifier: {0}>'.format(self.name)

    def assign(self, val):
        symbols.setsym(self.name, val)

    def eval(self):
        return symbols.getsym(self.name)


class Assignment(BaseExpression):
    def __init__(self, identifier, val):
        self.identifier = identifier
        self.val = val

    def __repr__(self):
        return '<Assignment: sym = {0}; val = {1}>'.format(self.identifier, self.val)

    def eval(self):
        self.identifier.assign(self.val.eval())


class BinaryOperation(BaseExpression):
    __operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '**': operator.pow,
        '/': operator.truediv,

        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,

        'and': operator.and_,
        'or': operator.or_,
    }

    def __repr__(self):
        return '<Binary operation: left = {0}; right = {1}>'.format(self.left, self.right)

    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        return self.__operations[self.op](self.left.eval(), self.right.eval())


class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart

    def __repr__(self):
        return '<If condition={0}; then={1}>'.format(self.condition, self.truepart)

    def eval(self):
        if self.condition.eval():
            self.truepart.eval()
        elif self.elsepart is not None:
            if isinstance(self.elsepart, BaseExpression):
                self.elsepart.eval()
            else:
                self.elsepart.eval()

class PrintStatement(BaseExpression):
    def __init__(self, expr: BaseExpression):
        self.expr = expr

    def eval(self):
        print(self.expr.eval())

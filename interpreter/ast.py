import operator


class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __repr__(self):
        return '<Instruction list: {0}>'.format(self.children)

    def eval(self):
        ret = []
        for n in self.children:
            if isinstance(n, ExitStatement):
                return n

            res = n.eval()

            if isinstance(res, ExitStatement):
                return res
            elif res is not None:
                ret.append(res)

        return ret


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
        '%': operator.mod,

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


class UnaryOperation(BaseExpression):
    __operations = {
        '+': operator.pos,
        '-': operator.neg,
        'not': operator.not_
    }

    def __repr__(self):
        return '<Unary operation: operation={0} expr={1}>'.format(self.operation, self.expr)

    def __init__(self, operation, expr: BaseExpression):
        self.operation = operation
        self.expr = expr

    def eval(self):
        return self.__operations[self.operation](self.expr.eval())


class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart

    def __repr__(self):
        return '<If condition={0}; then={1}>'.format(self.condition, self.truepart)

    def eval(self):
        if self.condition.eval():
            return self.truepart.eval()
        elif self.elsepart is not None:
            if isinstance(self.elsepart, BaseExpression):
                return self.elsepart.eval()
            else:
                return self.elsepart.eval()


class For(BaseExpression):
    def __init__(self, variable: Identifier, start: Primitive, end: Primitive, asc: bool, body: InstructionList):
        self.variable = variable
        self.start = start
        self.end = end
        self.asc = asc
        self.body = body

    def __repr__(self):
        return '<For {0} {1} {2} >'.format(self.start, '->' if self.asc else '<-', self.end)

    def eval(self):
        for i in range(self.start.eval(), 1 + self.end.eval(), 1 if self.asc else -1):
            self.variable.assign(i)
            if isinstance(self.body.eval(), ExitStatement):
                break


class While(BaseExpression):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self):
        while self.condition.eval():
            if isinstance(self.body.eval(), ExitStatement):
                break


class ExitStatement(BaseExpression):
    def __iter__(self):
        return []

    def eval(self):
        pass


class PrintStatement(BaseExpression):
    def __init__(self, items: InstructionList):
        self.items = items

    def __repr__(self):
        return '<Print: {0}>'.format(self.items)

    def eval(self):
        print(*self.items.eval(), end='', sep='')

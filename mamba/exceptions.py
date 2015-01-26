class InterpreterException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SymbolNotFound(InterpreterException):
    pass


class UnexpectedCharacter(InterpreterException):
    pass


class ParserSyntaxError(InterpreterException):
    pass


class DuplicateSymbol(InterpreterException):
    pass


class InterpreterRuntimeError(InterpreterException):
    pass


class InvalidParamCount(InterpreterRuntimeError):
    pass
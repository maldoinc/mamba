import ply.lex as lex

reserved = {
    'if': 'IF',
    'fn': 'FUNCTION',
    'ret': 'RETURN',
    'say': 'PRINT'
}

tokens = [
    'KEYWORD',
    'STMT_END',
    'EQUALS',
    'IDENTIFIER',
    'NUM_INT',
    'NUM_FLOAT',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'COMMA',
    'STRING',

    'PLUS',
    'EXP',
    'MINUS',
    'MUL',
    'DIV',

] + list(reserved.values())


t_COMMA = ','
t_PLUS = R'\+'
t_EXP = R'\*\*'
t_MINUS = '-'
t_MUL = R'\*'
t_DIV = R'/'
t_STMT_END = ';'
t_EQUALS = '='
t_NUM_FLOAT = R'\d*\.\d+'
t_ignore_WS = R'\s+'
t_LPAREN = '\('
t_RPAREN = '\)'
t_LBRACK = '{'
t_RBRACK = '}'


def t_IDENTIFIER(t):
    r'[\$_a-zA-Z]\w*'

    t.type = reserved.get(t.value, t.type)

    return t


def t_NUM_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"(?:\\"|.)*?"'

    # hiqen thonjezat dhe karakteret e escape
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")

    return t


def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


lexer = lex.lex()
import sys

import ply.yacc as yacc
import interpreter.ast as ast
from interpreter.lexer import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP')
)


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_assignee(p):
    '''
    assignee : identifier
    '''
    p[0] = p[1]


def p_assign(p):
    '''
    assign : assignee EQUALS NUMBER
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()
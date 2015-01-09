import sys

import ply.yacc as yacc
import interpreter.ast as ast
from interpreter.lexer import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP')
)


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement : identifier
    '''
    p[0] = p[1]


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_number(p):
    '''
    number : NUM_INT
           | NUM_FLOAT
    '''
    p[0] = ast.Numeric(p[1])


def p_assign(p):
    '''
    statement : identifier EQUALS number STMT_END
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_print(p):
    '''
    statement : PRINT identifier STMT_END
    '''
    print(p[2])


def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()
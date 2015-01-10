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
              | expression
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
           | STRING
           | boolean
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])


def p_boolean_operators(p):
    '''
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = p[1]


def p_assignable(p):
    '''
    assignable : number
               | expression
    '''
    p[0] = p[1]


def p_assign(p):
    '''
    expression : identifier EQUALS expression STMT_END
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_arithmetic_op(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression MUL expression
               | expression DIV expression
               | expression EXP expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])


def p_expression(p):
    '''
    expression : number
               | STRING
               | identifier
    '''
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()
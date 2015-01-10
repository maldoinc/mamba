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
              | if_statement
    '''
    p[0] = p[1]


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_primitive(p):
    '''
    primitive : NUM_INT
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


def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2] if isinstance(p[2], ast.BaseExpression) else ast.Primitive(p[2])


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = ast.Primitive(p[1])


def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]


def p_assign(p):
    '''
    expression : identifier EQUALS assignable STMT_END
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_ifstatement(p):
    '''
    if_statement : IF boolean LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[4])


def p_ifstatement_else(p):
    '''
    if_statement : IF boolean LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
    '''
    p[0] = ast.If(p[2], p[4], p[8])


def p_ifstatement_else_if(p):
    '''
    if_statement : IF boolean LBRACK statement_list RBRACK ELSE if_statement
    '''
    p[0] = ast.If(p[2], p[4], p[7])


def p_print_statement(p):
    '''
    statement : PRINT expression STMT_END
    '''
    p[0] = ast.PrintStatement(p[2])


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
    expression : primitive
               | STRING
               | identifier
    '''
    p[0] = p[1]


def p_for_loop(p):
    '''
    statement : FOR identifier IN NUM_INT ARROW_LTR NUM_INT LBRACK statement_list RBRACK
    statement : FOR identifier IN NUM_INT ARROW_RTL NUM_INT LBRACK statement_list RBRACK
    '''
    p[0] = ast.For(p[2], ast.Primitive(p[4]), ast.Primitive(p[6]), p[5] == '->', p[8])


def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()
import interpreter.parser as p
import interpreter.ast

script = '''
    a = 5;
    b = 6;

    c= 2 - 2 * 3;

    d = "wello" + " " + "world";

    a = true;

    a = 1 == 2;
'''

ast = p.parser.parse(script)

for node in ast.children:
    node.eval('dummy')

print(ast.children)
print(interpreter.ast.symbols.table())
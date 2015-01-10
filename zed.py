import interpreter.parser as p
import interpreter.ast
import pprint

script = '''
    a = 5;
    b = 6;

    c= 2 - 2 * 3 + 2 - 2 * 3 + 2 - 2 * 3 + 2 - 2 * 3;

    d = "wello" + " " + "world";

    a = true;

    a = 1 == 2;
    a = true or false;

    b = b + 1;
'''

ast = p.parser.parse(script)

for node in ast.children:
    node.eval('dummy')

pp = pprint.PrettyPrinter()
pp.pprint(ast.children)
pp.pprint(interpreter.ast.symbols.table())
import interpreter.parser as p
import interpreter.ast
import pprint

with open("scripts/second.sc") as f:
    script = f.read()

ast = p.parser.parse(script)

for node in ast.children:
    node.eval()

print("\n\n" + '=' * 80)
pp = pprint.PrettyPrinter()
pp.pprint(ast.children)
pp.pprint(interpreter.ast.symbols.table())
import interpreter.parser as p
import interpreter.ast
import interpreter.environment
import pprint

with open("scripts/second.sc") as f:
    script = f.read()

res = p.parser.parse(script)

interpreter.environment.declare_env(interpreter.ast.symbols)

for node in res.children:
    node.eval()

print("\n\n" + '=' * 80)
pp = pprint.PrettyPrinter()
pp.pprint(res.children)
pp.pprint(interpreter.ast.symbols.table())
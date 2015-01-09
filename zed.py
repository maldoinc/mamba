import interpreter.parser as p

script = '''
    a = 5;
    b = 6;
'''

ast = p.parser.parse(script)

for node in ast.children:
    node.eval()
    print(node)
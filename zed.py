import interpreter.parser as p
import sys

if len(sys.argv) == 1:
    with open("scripts/second.sc") as f:
        p.parser.parse(f.read())
else:
    with open(sys.argv[1]) as f:
        p.parser.parse(f.read())
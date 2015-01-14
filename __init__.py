import interpreter

with open("scripts/second.sc") as f:
    interpreter.execute(f.read(), disable_warnings=True)
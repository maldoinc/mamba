import mamba

with open("scripts/second.sc") as f:
    mamba.execute(f.read())
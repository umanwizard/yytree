from sys import stdin
import re

ID = r"[a-zA-Z_][a-zA-Z_0-9]*"
shift_re = re.compile(r"[^()]*reading[^(]*\(([a-zA-Z_][a-zA-Z_0-9]*)\)")
reduce_re = re.compile(r"[^()]*reducing[^(]*\(([^)]*)\)")
symbols = []
for line in stdin:
    match = shift_re.match(line)
    if match:
        symbols.append((match.groups()[0], []))
    else:
        match = reduce_re.match(line)
        if match:
            parts = match.groups()[0].split()
            children = symbols[-(len(parts)-2):]
            symbols = symbols[:-(len(parts)-2)]
            symbols.append((parts[0], children))

print symbols

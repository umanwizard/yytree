from sys import stdin
import re

chars = ['|', '=', 'T', ':']

def psymbol(depth, symbol):
    print ' ' * depth + chars[depth % len(chars)] + ('+' if len(symbol[1]) else '-')  + '-' + symbol[0]
    for child in symbol[1]:
        psymbol(depth + 1, child)

ID = r"[a-zA-Z_][a-zA-Z_0-9]*"
shift_re = re.compile(r"[^()]*reading[^(]*\(([a-zA-Z_][a-zA-Z_0-9]*)\)")
reduce_re = re.compile(r"[^()]*reducing[^(]*\(([^)]*)\)")
shifting_re = re.compile(".*shifting to.*")
shift_queue = []
symbols = []
for line in stdin:
    match = shift_re.match(line)
    if match:
        shift_queue.append((match.groups()[0], []))
    elif shifting_re.match(line):
        symbols.append(shift_queue.pop(0))
    else:
        match = reduce_re.match(line)
        if match:
            parts = match.groups()[0].split()
            if (len(parts) != 2):
                children = symbols[-(len(parts)-2):]
                symbols = symbols[:-(len(parts)-2)]
                symbols.append((parts[0], children))
            else:
                symbols.append((parts[0], []))

for symbol in symbols:
    psymbol(0, symbol)

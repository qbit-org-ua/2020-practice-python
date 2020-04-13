"""
while True:
    try:
        s = input()
    except EOFError:
        break
    print("New line:", s)

print("Bye")
"""

import sys

for line in sys.stdin:
    print("New line1: ", repr(line))
    line = line.strip()
    print("New line2: ", repr(line))
print("Bye")

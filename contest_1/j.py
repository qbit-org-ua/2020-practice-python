# Авторы похожих решений:
# * Кошевой Алексей

import sys

direction = x = y = 0
for line in sys.stdin:
    action = line.strip()
    if action == "L":
        direction = (direction - 1) % 4
    elif action == "R":
        direction = (direction + 1) % 4
    else:
        x += (2 - direction) * (direction % 2)
        y += (1 - direction) * ((direction + 1) % 2)

print(x, y)

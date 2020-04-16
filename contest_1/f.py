# Все решения схожи. Приз за находчивость (math.hypot) получают:
# * Отусіле Еммануїл
# * Куприянова Катя

import math

x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]
a = math.hypot(x2 - x1, y2 - y1)
b = math.hypot(x3 - x1, y3 - y1)
c = math.hypot(x3 - x2, y3 - y2)
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)

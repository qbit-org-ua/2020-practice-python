import itertools
import math

points = []
for _ in range(3):
    points.append([int(x) for x in input().split()])

coefficients = []
for p1, p2 in itertools.combinations(points, 2):
    coefficients.append(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))

S = p = sum(coefficients) / 2
for coefficient in coefficients:
    S *= p - coefficient
S = math.sqrt(S)

print(S)

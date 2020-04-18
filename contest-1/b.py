# Авторы похожих решений:
# * Шевченко Тимур

a, b = [int(x) for x in input().split()]

print(f"{abs(b - a) + 1} very important numbers:")

step = 1 if a < b else -1
for i in range(a, b + step, step):
    print(i)

# print(*range(a, b + step, step), sep="\n")

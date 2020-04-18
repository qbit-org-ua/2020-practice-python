# Авторы похожих решений:
# * Носенко Микита
# * Тесля Юля
# * Момот Олег

line = input().strip()
digits = sorted(line)
for index, digit in enumerate(digits):
    if digit != "0":
        digits[0], digits[index] = digits[index], digits[0]
        break
print("".join(digits))


# Решение со звёздочкой от Александра:

# num = "".join(sorted(str(int(input())))).lstrip("0")
# print(num[0] + ("0000" + num[1:])[-3:])

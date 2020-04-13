string_value = "Привет мир!"
print(string_value[::-1])

string_value = "   текст  с пробелами   \n"
print(repr(string_value.strip()))
print(repr(string_value.lstrip()))
print(repr(string_value.rstrip()))

my_list = ["one", "two", "three"]
print(my_list)
print(my_list[::-1])
print("one" in my_list)
print("Vlad" in my_list)

for my_item in my_list:
    print(my_item)

a, b = [1, 2]
print(a, b)

# Множества (set)

my_set = {"one", "one", "two", "one", "three"}
print(my_set)

is_in_set = "one" in my_set
print(is_in_set)

print("Vlad" in my_set)

"""
import sys

names = set()
for line in sys.stdin:
    name = line.strip()
    names.add(name)
print("There are", len(names), "unique names:", names)
"""

my_list_of_names = ["Vlad", "Stas", "Nikolay", "Vlad", "Oleg"]
unique_names = set(my_list_of_names)
print("There are", len(unique_names), "unique names:", unique_names)


# Ассоциативные массивы (hashmap, словарь, dictionary, dict())

my_dict = {
    "Vlad": 2,
    "Oleg": 1,
    "Nikolay": 1,
}
print(my_dict)
print(my_dict["Vlad"])
my_dict["Vlad"] += 1
print(my_dict["Vlad"])
my_dict["Alex"] = 10
print(my_dict["Alex"])
print(my_dict)
del my_dict["Vlad"]
print(my_dict)
print(len(my_dict))


my_list_of_names = ["Vlad", "Stas", "Nikolay", "Vlad", "Oleg", "Oleg", "Oleg", "Oleg"]
my_dict_of_names = {}
# my_dict_of_names = dict()

# X in list() - O(N)
# X in set() / dict() - O(1)

# if "Vlad" in my_list_of_names:
#    ...

# my_set_of_names = set(my_list_of_names)
# if "Vlad" in my_set_of_names:
#    ...

for name in my_list_of_names:
    if name in my_dict_of_names:
        my_dict_of_names[name] += 1
    else:
        my_dict_of_names[name] = 1
print(my_dict_of_names)

import collections

my_dict_of_names = collections.Counter(my_list_of_names)
print(my_dict_of_names)


# Списковые выражение (list comprehentions)

my_list_of_names = ["Vlad", "Stas", "Nikolay", "Vlad", "Oleg", "Oleg", "Oleg", "Oleg"]
"""
my_list_of_len_names = [
    len(my_list_of_names[0]),
    len(my_list_of_names[1]),
    len(my_list_of_names[2]),
    len(my_list_of_names[3]),
    len(my_list_of_names[4]),
    len(my_list_of_names[5]),
    len(my_list_of_names[6]),
]
"""

my_list_of_len_names = []
for name in my_list_of_names:
    my_list_of_len_names.append(len(name))

# for i in range(len(my_list_of_names)):
#    my_list_of_len_names.append(len(my_list_of_len_names[i]))

print(my_list_of_len_names)

my_list_of_len_names = [len(name) for name in my_list_of_names]
print(my_list_of_len_names)

my_dict_of_len_names = {name: len(name) for name in my_list_of_names}
print(my_dict_of_len_names)

"""
for VAR_NAME in LIST:
    pass
    if i > 10:
        break
    if i % 2 == 0:
        continue

while CONDITION:
    pass
    if i > 10:
        break
    if i % 2 == 0:
        continue

if CONDITION:
    pass
elif CONDITION:
    pass
else:
    pass

try:
    #
except EOFError:
    print("Случился конец файла")

def FUNCTION_NAME(param1, param2):
    pass
"""

# Функции


def add(a, b):
    return a + b


print("Сложение:", add(2, 2))


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


for i in range(1, 10):
    print("Число fib #", i, "=", fib(i))
    x = f"Число fib({i}) = {fib(i)}"
    print(x)


def sub(a, b):
    c = b - a
    return c


print("Вычитание:", sub(2, 2))


# Модули

import sys
import math
import collections
import itertools
import functools
import heapq

print(math.factorial(1000))


print("Я Python. Приятно познакомиться!")

# name = "Vlad"
# print(name + str(33))
# name = 10
# print(name / 3)

# your_name = input()
# print("Your name is " + your_name)

# a_str = input()
# a = int(a_str)

# b_str = input()
# b = int(b_str)
# print(a + b)

# b_str = str(b)

# if b > 10 \
#     and a < 10:
#     print("qq")
#     print("qq")
#     print("qq")
#     print("qq")
# else:
#     print("ww")

# line = input()
# numbers_str = line.split()

# a = int(numbers_str[0])
# b = int(numbers_str[1])
# print(a + b)

arr = [1, 2, 3, 'asd', True]
print(arr[::-1])

for item in arr:
    print("Item: ", item)

# Pascal: for i := 1 to 9 begin
# C: for (int i = 1; i < 10; ++i)

for i in range(9, 0, -1):
    print(i)

arr = [1, 2, 3, 'asd', True]
s = 0
for i, item in enumerate(arr):
    print(i, item)
    s += i
print(s)

a = 1
while a < 10:
    a += a
print("A: ", a)



# ['Vlad', 'Petya', 'Oleg'] => [[0, 'Vlad'], [1, 'Petya'], [2, 'Oleg']]

for (index, name) in [[0, 'Vlad'], [1, 'Petya'], [2, 'Oleg']]:
    print(index, name)

a = 10
b = 20
a, b = 10, 20
a, b = b, a

index, name = [0, 'Vlad']
index, name = [0, 'Vlad']

arr = [1, 2, 3]
arr.append(10)
print("Arr:", arr)

print("Arr:", arr + [30, 40])

def qq(param1):
    print("Parameter #1", param1)
    return param1 + 1

x = qq(123)
print(x)

a = [1, 2, 3]
b = a.copy()
a.append(4)
print(b)

s = 0
s += 10
s += 33

s = []
s = ""

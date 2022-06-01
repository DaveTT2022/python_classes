#1
for i in range(1, 10):
    print("*"*i)


#2

num = input("Send number:")
sum = 0

for i in num:
    if int(i) % 2 == 0:
        sum += 1
print(sum)

#3


for i in range(1, 9):
    print(f"{i} x {i + 1} = {i * (i + 1)}")

#4

text= input("Send your text: ")

for i in range(0,len(text), 2):
    print(text[i], end = "")
print()

#5

num = int(input("Send your number: "))

for i in range(1, int(num ** 0.5)):
    if not num % i:
        print(num // i, i)

#6 Write a Python program to add two positive integers without using the '+' operator. 

first_num = int(input("First number: "))
second_num = int(input("Second number: "))

while True:
    x_or = first_num ^ second_num
    second_num = (first_num & second_num) << 1
    if x_or == first_num:
        break
    first_num = x_or
print(first_num)

#7 Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

text = input("Send a text: ")
letters = []
letters[:] = text
print(letters)
values = []
o = [0 for x in range(len(letters))]
k = [0 for x in range(len(letters))]
i = -1

def func_lists():
    global letters, values, o, k, i
    i += 1
    for o[i], k[i] in enumerate(letters):
        letters.pop(o[i])
        values.append(k[i])
        first_value = o[i]
        second_value = k[i]
        if len(letters) == 1:
            print("".join(values) + letters[0])
            i = 0
        else:
            func_lists()
        letters.insert(first_value, second_value)
        values.pop()

func_lists()
#1

num = int(input("Send your number: "))
sum = 1
for i in range(1, num + 1):
    sum *= i
print(sum)

#2

count = 0

for i in range(1, 10):
    if i > 5:
        count += 2
    print((i - count) * '*')

#3

num_1 = 0
num_2 = 1

while True:
    if num_2 > 50:
        break
    print(num_1, num_2, "", end = "")
    num_1 = num_2 + num_1
    num_2 = num_2 + num_1
print()

#4

import random

num = int(input("Lets play Rock-Paper-Scissors, 1 is rock, 2 is paper 3 is scissors \n"))

random_num = random.randint(1, 3)
print("Computer choosed " + ("rock" * bool(not bool(random_num - 1))) + ("paper" * bool(not bool(random_num - 2)) + ("scissors" * bool(not bool(random_num - 3)))))

if num - random_num == 1 or random_num - num == 2:
    print("You won")
elif num == random_num:
    print("Draw")
elif random_num - num == 1 or num - random_num == 2:
    print("You lost")
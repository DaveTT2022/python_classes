#1

num = int(input("give a number 0-6: "))
if num == 0:
    print("Monday")
elif num == 1:
    print("Tuesday")
elif num == 2:
    print("Wednesday")
elif num == 3:
    print("Thursday")
elif num == 4:
    print("Friday")
elif num == 5:
    print("Saturday")
elif num == 6:
    print("Sunday")

#2

text = input("Send your text: ")
if " " in text:
    print("your text has space")
else:
    print("your text doesn't have space")

3

word = input("Send a word:")
if len(word) < 3:
    print("your word must have at least 3 character")
else:
    if word.endswith("ing"):
        print(word + "ly")
    else:
        print(word + "ing")

#4

num = int(input("Enter year number: "))
if not num%4:
    if not num%400 or num%100:
        print("Its leap year")
    else:
        print("Not leap year")
else:
    print("not leap year")
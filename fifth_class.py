#1
number = int(input("Send your number: "))
if not number % 5 and not number % 11:
    print(f"{number} number is divisble by both 5 and 11")
elif not number % 5 or not number % 11:
    print(f"{number} number is divisble by {(5 if number % 11 else 11)}")
else:
    print(f"{number} number is not divisble by 5 nor by 11")

#2

number = int(input("Send your number: "))

if not number % 5 and not number % 3:
    print("FizzBuzz")
elif not number % 5 or not number % 3:
    print("Buzz" if number % 3 else "Fizz")
else:
    print(number)

#3

text = input("send your text: ")

if text.find("not") < text.find("poor") and text.find("not") != -1:
    print(text[:text.find("not")] + "good")
else:
    print(text)

#4

text = input("send your text: ")

first_letter = text[0]

changed_string = text.replace(first_letter, "$")
print(first_letter + changed_string[1:])
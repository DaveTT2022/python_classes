#1

nums = input("Send your numbers by seperating them with ','\n")

x = nums.find(",")
num_1 = int(nums[:x])
y = nums.find(",", x + 1)
num_2 = int(nums[x + 1 : y])
num_3 = int(nums[y + 1 : ])

def area_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise Exception("Impossible triangle")
    half_perimiter = (a + b + c) / 2
    area = (half_perimiter * (half_perimiter - a) * (half_perimiter - b) * (half_perimiter - c)) ** 0.5
    return area

print("Area of you triangle is:", round(area_triangle(num_1, num_2, num_3), 2))

#2

text = input("Send your text: ")

def reverse_text(text):
    return text[::-1]
print(reverse_text(text))

#3

text = input("Sent your text: ")

def text_check(text) -> int:
    upper, lower = 0, 0
    for i in text:
        if i.isalpha() and ord("a") <= ord(i):
            lower += 1
        elif i.isalpha():
            upper += 1
    return f"Upper letters: {upper} \nLower letters: {lower}"

print(text_check(text))

#4

text = input("Send your palindrome text: ")

def is_palin(text):
    clear_text = ""
    for i in text:
        if i.isalpha():
            clear_text += i
    if clear_text.lower() == clear_text[::-1].lower():
        return "Text is palindrome"
    else:
        return "Text is not palindrome"

print(is_palin(text))

#5

num = int(input("Send your number: "))

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            break
    else:
        return "The number is prime"
    return "The number is not prime"
print(is_prime(num))

# # extra (currency convertor)

# import requests
# import re
# from prettytable import PrettyTable


# currency_1 = input("Enter 3 letters (e.g USD, EUR, RUB) from your main currency: ")
# currency_2 = input("Enter 3 letters currency to which you want to convert: ")

# x = PrettyTable()
# x.field_names = [currency_1.upper(), currency_2.upper()]
# x.padding_width = 5
# x.align = "r"

# data = requests.get(f'https://www.xe.com/currencyconverter/convert/?Amount=1&From={currency_1.upper()}&To={currency_2.upper()}')
# html = data.text


# first_row = re.findall(r'qMFSh">.*?<!-- -->', html)
# second_row = re.findall(r'<td>[0-9]+[,]?[0-9]*[.][0-9]+<!-- -->', html)

# if first_row == []:
#     raise ValueError("Mentioned currency was not found, make sure to use 3 letters of currency")

# price_1 = []
# price_2 = []

# for i in range(len(first_row)//2):
#     price_1.append(first_row[i][7:-8])
#     price_2.append(second_row[i][4:-8])
#     x.add_row([price_1[i], price_2[i]])

# print(x)
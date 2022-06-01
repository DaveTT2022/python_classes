#First assignment

tempC = 34
tempF = 1.8*tempC + 32
print("1.", tempF)

#Second assignment

a, b, c = 5, 6, 7
print("2.")
print("  a)", (a + b + c)/3) # a point
print("  b)", (a+b)**c) # b point
print("  c)", int(str(a) + str(b) + str(c)) + a*b*c) # c point

#Third assignemnt (calculations of 2 numbers)

print("Enter your first number: ", end = "")
num1 = int(input())
print("Enter your second number: ", end = "")
num2 = int(input())

print("Sum of numbers: ", num1 + num2)
print("Diference of numbers: ", num1 - num2)
print("Ratio of numbers: ", num1 / num2)
print("Product of numbers: ", num1 * num2)

#Extra

# #4. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# numbersInput = input()
# numberList = numbersInput.split(", ")
# numberTuple = tuple(numberList)
# print("List:", numberList)
# print("Tuple:", numberTuple)

# # 5 Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# color_final = set()
# for i in color_list_1:
#     if i not in color_list_2:
#         color_final.add(i)
# print(color_final)

# # 6 Write a Python program to convert seconds to day, hour, minutes and seconds

# sec = int(input("Input seconds:"))
# days = sec // (3600 * 24)
# hours = (sec - days * 3600 * 24) // 3600
# minutes = (sec - days * 3600 * 24 - hours * 3600) // 60
# seconds = sec - days * 3600 * 24 - hours * 3600 - minutes * 60
# print(f"{days}d {hours}h {minutes}m {seconds}s")

# # 7 Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

# num = int(input("Positive int: "))
# def sumCube(number):
#     return (number**3 + sumCube(number-1)) if number > 1 else + 1
# print(sumCube(num))
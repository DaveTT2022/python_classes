# while True:
#     has_letter = False
#     has_digit = False
#     has_symbol = False
#     password = input("Send your password: ")
#     try:
#         if len(password) < 8:
#             raise ValueError("short password")
#         for i in password:
#             if password.isalpha():
#                 has_letter = True
#                 continue
#             elif password.isdigit():
#                 has_digit = True
#                 continue
#             else:
#                 has_symbol = True
#                 continue 
#     except Exception as error:
#         print(error)

dict_1 = {"abc" : 5, 666 : "a", (1,1,12,3) : [3,3,3,3]}
dict_2 = {"66" : 59, 646 : "abb", (1,1,3) : [3,3,3,3]}

for i, j in enumerate(dict_1):
    dict_2[i] = j
print(hash("abc"))
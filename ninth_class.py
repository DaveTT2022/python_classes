#1

def tuple_check(first_tuple: tuple, second_tuple: tuple) -> str:
    if first_tuple == second_tuple:
        return f"{first_tuple} and {second_tuple} are the same tuple"
    else:
        return f"{first_tuple} and {second_tuple} are not the same tuple"

tuple_1 = (5,6,7,"8")
tuple_2 = (5,6,7,"8")

print(tuple_check(tuple_1, tuple_2))

tuple_1 = (5,6,7,"9")
tuple_2 = (5,6,7,"8")

print(tuple_check(tuple_1, tuple_2))

#2

def tuple_test(first_tuple: tuple, second_tuple: tuple) -> bool:
    if tuple_letter_counter(first_tuple) == tuple_letter_counter(second_tuple):
        return True 
    return False

def tuple_letter_counter(tuple_: tuple) -> int:
    sum_ = 0
    for element in tuple_:
        if type(element) == str:
            for i in element:
                sum_ += 1 if i.isalpha() else 0
    return sum_

tuple_1 = ("Abc", "d", False, "gh")
tuple_2 = ("a", "and", "gh", 5)

print(tuple_test(tuple_1, tuple_2))

tuple_1 = ("Abc", "d", False, "gha")
tuple_2 = ("a", "and", "gh", 5)

print(tuple_test(tuple_1, tuple_2))

#3

def common_values(tuple_1: tuple, tuple_2: tuple) -> tuple:
    common_tuple = ()
    for i in tuple_1:
        common_tuple += (i,) if i in tuple_2 else ()
    return common_tuple
print(common_values((25,65,55,"a",66,78, "abc", "b"), (25,32,"a",62, "abcdefg")))

#4

def tuple_opt(*args) -> tuple:
    tuple_ = ()
    for elem in args:
        tuple_ += (elem,) if elem not in tuple_ else ()
    return tuple_
print(tuple_opt(4,5,6,5,5,5,"a","a", "abc"))
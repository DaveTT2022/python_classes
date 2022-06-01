#1

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}
dict4 = {6:50,7:60}

def sum_dict(*args):
    dict_ = {}
    for elems in args:
        dict_.update(elems)
    return dict_

print(sum_dict(dict1, dict2, dict3, dict4))

#2

num = int(input("Send your number \n"))

def dict_maker(number : int) -> dict:
    return {i : i * i for i in range(1, number + 1)}

print(dict_maker(num))

#3

dict_ = {'c1': 'Red', 'c2': 'Green', 'c3': None}

def clear_dict(dictionary: dict) -> dict:
    return {x : y for x , y in dictionary.items() if dictionary[x] != None}

print(clear_dict(dict_))
#1

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_3 = []

for i in list_2:
    if i in list_1 and i not in list_3:
        list_3.append(i)
print(list_3)

2

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40], [33]]

for elems in sample_list:
    inx = sample_list.index(elems) + 1

    if elems in sample_list[inx : ]:
        sample_list.pop(sample_list.index(elems, inx))

print(sample_list)

3

sample_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

for elems in sample_list:
    if type(elems) == list:
        for elems_2 in elems[::-1]:
            sample_list.insert(sample_list.index(elems) + 1, elems_2)
        sample_list.pop(sample_list.index(elems))

print(sample_list)

4

text = input("Your text: ")
text = text.split(" ")
text.reverse()
print(text)
#1

set_1 = {"abc", 36, True, 25, "O", 44, "abc"}

def set_copy(set_ : set) -> set:
    return set_1.copy()

set_2 = set_copy(set_1)
print(set_2)

#2

sample_set = {484,864,64,761,761,6776,94,97498,465,1}

def max_min_set(set_ : set) -> dict:
    ls = sorted(list(set_))
    return {"min" : ls[0], "max" : ls[len(ls) - 1]}

print(max_min_set(sample_set))

#3

set_1 = {"abc", 36, True, 25, "O", 44, "abc"}
set_2 = {"O", 25, False, 66, "bca"}

def difference_set(fst_set : set, snd_set : set) -> set:
    dif_set = fst_set.copy()
    dif_set.difference_update(snd_set)
    return dif_set

print(difference_set(set_1, set_2))

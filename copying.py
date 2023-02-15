# how to copy mutable items with the built-in copy module
# difference between shallow and deep copies
# make custom copies of actual objects

org = 5
cpy = org
# this did not make a "real" copy, instead it simply made a new variable with the same refernce

cpy = 6
# this assignment again creates a new variable

print(cpy)
print(org)
# we can see they are different

# it is different with a list, we have to be more careful
org_list = [0, 1, 2, 3, 5]
cpy_list = org_list
# so we copied it now if we want to make a change
cpy_list[0] = 69

print(cpy_list)
print(org_list)
# thus when we print we can see that BOTH were changed.
# thus we want to be able to make a new, independent copy

# shallow copy: 1 level deep
# deep copy: full and independent copy

import copy
org_list2 = [6, 66, 69, 13, 26]

# shallow copy
cpy_list2 = copy.copy(org_list2)




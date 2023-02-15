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
cpy_list2[0] = 10101

print(cpy_list2)
print(org_list2)
# thus we can see here original list did not change

# now imagine we have a nested list
nest_list = [[3, 6, 9], [4, 8, 12], [5, 10, 15]] 

# first assume we just make a shallow copy
nest_cpy = copy.copy(nest_list)
nest_cpy[0][1] = 13

print(nest_cpy)
print(nest_list)
# we can see that again it changed both - not what we wanted
# so for 2 or more dimensions we need to use deep copy

nest_lis2 = [[10, 20, 30], [11, 22, 33], [12, 21, 121]] 
nest_cpy2 = copy.deepcopy(nest_lis2)
nest_cpy2[0][1] = 1000

print(nest_cpy2)
print(nest_lis2)
# now we can see it only changed original and copy was unaffected 
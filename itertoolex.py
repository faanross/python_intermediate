# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# iterators are data types that can be used in a for loop, most common example is list but here are more specific use cases

# product
from itertools import product
a = [13, 26]
b = [6, 9]
# we can see in results this is similar (if not the exact same) as matrix multiplication
prod = product(a, b)
print(prod)
print(list(prod))

prodb = product(a, b, repeat=2)
print(list(prodb))
print()

# permutation return all possible orderings of an input
from itertools import permutations
c = ['lama', 'liger', 'lawfanwduh']
perma = permutations(c)
print(list(perma))

permab = permutations(c, 2)
print(list(permab))

# combinations makes all combinations of a specified length
from itertools import combinations
boob = [12, 11, 8, 6]
bbcomb = combinations(boob, 2)
print(list(bbcomb))


# accumulate
from itertools import accumulate
poop = [6, 9, 16, 19]
accu = accumulate(poop)
print(accu)
print(list(accu))

# by default it will take the sum, but we can also multiply
import operator
accub = accumulate(poop, func=operator.mul)
print(list(accub))

dog = [13, 5, 6, 16, 18, 11, 50]
accuc = accumulate(dog, func=max)
print(list(accuc))

# groupby is an iterator that returns keys and groups from an iterable
from itertools import groupby

def smaller_than_four(x):
   return x < 4

xx = [1, 2, 3, 4, 5, 6, 10, 13]
legrup = groupby(xx,key=smaller_than_four)

for key, value in legrup:
    print(key, list(value))

print()
# do the same but using the lambda function

xx = [1, 2, 3, 4, 5, 6, 10, 13]
legrupb = groupby(xx,key=lambda x:x<4)

for key, value in legrupb:
    print(key, list(value))

from itertools import count, cycle, repeat

# starts counting from 5 in increments of 2 until it reaches 13
for i in count(5, 2):
    print(i)
    if i == 13:
        break
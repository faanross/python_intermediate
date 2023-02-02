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

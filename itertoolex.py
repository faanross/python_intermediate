# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# iterators are data types that can be used in a for loop, most common example is list but here are more specific use cases

# product
from itertools import product
a = [13, 26]
b = [6, 9]
prod = product(a, b)
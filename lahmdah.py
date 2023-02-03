# lambda arguments: expression
# small, one-line, anonymous function 
# creates a function with some arguments, evaluates, and returns

add10 = lambda x: x + 10 # we are creating a function, it receives x, it returns x + 10
print(add10(5))
print(add10(add10(5)))

# practically same as a normal function
def addsten(x):
    return x + 10

print(addsten(5))

# lambda is just used for convenience whenever there is a function with 1 line only = use lambda

power_of =  lambda a, b: a**b
print(power_of(2, 8))

# we also often use lambda when we need to use multiple functions

# let's look at sorted() function
list_a = [13, 44, 4, 3, 1, 55, 67, 23]
print(sorted(list_a))

# now imagine we have 2D - list of tuples
list_b = [(3, 4), (1, 6), (11, 1), (12, 9), (1, 7)]

# if we simply use sorted() then by default it will use x (first entry in each tuple)
print(sorted(list_b))

# if we want to change this, let's say sort by 2nd element, we can use lambda here
print(sorted(list_b, key = lambda x: x[1]))

# let's sort them according to sum of each
print(sorted(list_b, key = lambda x: x[0] +  x[1]))

# map(function, sequence)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * x, a)
print(list(b))

# another way we can do this with list comprehension
c = [x*x for x in a]
print(c)
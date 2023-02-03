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
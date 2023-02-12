# functions that return an object that can be iterated over
# defined exactly like a normal function but instead of return keyword we use yield

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)
# different use cases of *

# multiplication and power
print(5*7)
print(2**8)

# creat lists, tuples, or strings with repeated elements
zeros = [0] * 10
letuple = (6, 9) * 5
doityeah = "ABC" * 6

print(zeros)
print(letuple)
print(doityeah)

# *args and **kwargs

def foo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, "poop", "tweak")
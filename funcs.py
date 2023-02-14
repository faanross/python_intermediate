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
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, "poop", "tweak")

def bar(a, b, c):
    print(a, b, c)

my_list = [6, 8, 9]
bar(*my_list)

number = [1, 2, 3, 4, 5, 6]
beginning, *middle, last = number
print(beginning)
print(middle)
print(last)

tuple1 = (1, 2, 3)
list1 = [4, 5, 6]

new_list = [*tuple1, *list1]
print(new_list)
# functions that return an object that can be iterated over
# defined exactly like a normal function but instead of return keyword we use yield

def mygenerator():
    yield 1
    yield 2
    yield 3

def mygenerator2():
    yield 11
    yield 2
    yield 6
    yield 23

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1



g = mygenerator()
print(g)

# for i in g:
#     print(i)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# now if we were to use next() again it would yield an error

h = mygenerator()
print(sum(h))

k = mygenerator2()
print(sorted(k))

cd = countdown(10)
for i in cd:
    print(i)

# generators save a lot of memory when we work with large data sets
# to illustrate this look at this regular function, it will generate data set and store in list nums

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

mylist = firstn(10)
print(mylist)
print(sum(mylist))

# here we will create the same functional outcome, but with generator
def firstn_generator(n):
    num2 = 0
    while num2 < n:
        yield num2
        num2 += 1

mylist2 = firstn_generator(10)
mylist3 = firstn_generator(10)
print(sum(mylist2))
print(list(mylist3))



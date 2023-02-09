import random

# produces random float
a = random.uniform(1, 50)
print(a)

# produces integer
b = random.randint(10, 100)
print(b)

# variate using mu (mean) and sigma (std.deviation)
c = random.normalvariate(0, 1)
print(c)

#randomly draw from a list
mylist = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
print(mylist)

d = random.choice(mylist)
print(d)

# choose mulitple from list - unique
e = random.sample(mylist, 5)
print(e)

# choose mulitple from list - can reuse same element multiple times
f = random.choices(mylist, k=5)
print(f)
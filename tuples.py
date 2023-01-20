# Tuples are:
# Ordered (same as lists)
# Immutable (vs lists which are mutable)
# Also allows duplicates (same as lists)
# Thus major diff vs lists is that they are immutable
# Use them in programs when you want to ensure variable value remains constant

first_tuple = ("Kip", 32, "Cage Fighter")
print(first_tuple)

first_tuple = ("Kip")
print(type(first_tuple))

first_tuple = ("Kip",)
print(type(first_tuple))

# Remember you can nest: for ex lists in a tuple
# Here we will be able to change the individual values in the lists, but cannot add or remove lists or change order

first_tuple = (["Kip", 32, "Cage Fighter"], ["Rico", 44, "Pro Athlete"])
print(first_tuple)

# Accessing specific values

print(first_tuple[0])
print(first_tuple[1])

print(first_tuple[0][2])
print(first_tuple[1][0])

# this works because we are changing LIST. If we tried to change first_tuple[0], it would not work: MUTABILITY
first_tuple[0][0] = "Pedro"
print(first_tuple)

first_tuple = (["Kip", 32, "Cage Fighter"], ["Rico", 44, "Pro Athlete"])

# nested for loop to print all the values
for i in first_tuple:
    for j in i:
        print(j)

# check to see if values are present

query1 = "rico"
query2 = "lyle"

if query1 in (first_tuple[0] or first_tuple[1]):
    print(query1,"is in the tuple.")
else:
    print(query1,"is not in the tuple.")

if query2 in (first_tuple[0] or first_tuple[1]):
    print(query2,"is in the tuple.")
else:
    print(query2,"is not in the tuple.")

chicken = ('t', 'a', 'l', 'o', 'n', 's')
print(len(chicken))

print(chicken.count('t'))
print(chicken.count('x'))

print(chicken.index('o'))

# convert a tuple to a list
chicken_list = list(chicken)
print(type(chicken_list))

# convert a list to a tuple
new_chicken = tuple(chicken_list)
print(type(new_chicken))
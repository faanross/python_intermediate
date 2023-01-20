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
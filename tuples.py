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
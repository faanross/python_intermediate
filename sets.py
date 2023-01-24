# a collection type that is: unordered, mutable, does NOT allow duplicates (disting. charac.)
# same curly braces as dict, but does not contain key:values just single entries

myset = {1, 6, 9, 13, 26, 69, 420, 666}
print(myset)

# if we have copies of an item in a list, only one will be interpreted as beign in set
myset = {1, 6, 9, 13, 26, 69, 420, 666, 6, 9, 13, 26, 69}
print(myset)

# we can use function to turn a word into a set, each UNIQUE letter will be processed as a single entry in set, and reorders ARBITRARILY
newset1 = set("rexkwondo")
print(newset1)
# output: {'d', 'o', 'n', 'w', 'k', 'r', 'e', 'x'}

if 'x' in newset1: print("Present")
else: print("Not present")
# strings: ordered, immutable, text representation
first_string = "Bring me my chapstick"
print(first_string)

char1 = first_string[3]
print(char1)

for i in range(len(first_string)):
    print(first_string[i], end="")
print()

substring = first_string[12:]
print(substring)

for i in range(len(first_string)):
    j = len(first_string)-(i+1)
    #print(j)
    print(first_string[j], end="")
print()

name = "Rico"
food = "steak"
occupation = "pro footballer"
sentence = name+" is a "+occupation+" who loves "+food
print(sentence)

if 'Rico' in sentence:
    print("YES")
else:
    print("NO")

lotsofspace = "                    numchuck skills           "
print(lotsofspace)
print(lotsofspace.strip())
print(lotsofspace.strip().upper())
print(lotsofspace.strip().capitalize())
print(lotsofspace.strip().endswith("skills"))
print(lotsofspace.strip().endswith("dunes"))
print(lotsofspace.strip().find('chuck'))
print(lotsofspace.strip().count('s'))
print(lotsofspace.strip().replace('numchuck', 'computer hacking'))
#
pickup = "I see you're drinking 1%."
# default delimiter is space
picksplit = pickup.split()
# we can specify delimiter - here for ex on i
picksplitb = pickup.split("i")

print(picksplit)
print(picksplitb)
print(picksplit[3])

# convert list back into string
new_string = '--'.join(picksplit)
print(new_string)

# %, fomart(), f-Strings
hair = "sandy"
hair1 = "her hair is %s" %hair
print(hair1)
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
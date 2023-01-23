# Dictionaries: Key:Value pairs, Unordered, Mutable, nesting provides many poss.

first_dict = {"name": "Napoleon", "school": "Preston", "age": 17, "food": "quesadilla"}
print(first_dict)

#using dict function to caste dictionary
second_dict = dict(name="Rico", school="Preston", age=46, food="minute steak")
print(second_dict)

# accessing value: name[key]
printme = second_dict["food"]
print(printme)

# append a pair
first_dict["power animal"] = "liger"
print(first_dict)
print(first_dict["power animal"])
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

# a few ways to delete items
del first_dict["age"]
print(first_dict)

first_dict.pop("school")
print(first_dict)

# this one simply removes last item
first_dict.popitem()
print(first_dict)

# check if to see a specific key is in dictionary - two methods
third_dict = {"name": "Pedro", "school": "Preston", "age": 18, "food": "chimmychangas"}
fourth_dict = {"name": "Deb", "school": "Preston", "age": 17, "food": "skim milk"}

if "food" in third_dict:
    print(third_dict["food"].capitalize()+" is Pedro's comida favorita.")
else:
    print("Pedro has no favorite food")

try:
    print(fourth_dict["power animal"])
except:
     print("Deb's power animal is unknown.")

for key in fourth_dict:
    print(str(key)+": "+str(fourth_dict[key]))

# copying a dictionary
mydict_cpy = third_dict
print(mydict_cpy)
# but this one is dangerous: if we modify copy, also modifies original

# So instead use copy function...
mydict_cpy = third_dict.copy()
print(mydict_cpy)

# merging dictionaries with update() method
fifth_dict = {"name": "Tina", "nickname": "Fat Lard", "age": 6, "food": "casserole"}
sixth_dict = {"name": "Randy", "school": "Preston", "age": 19, "food": "tots"}

fifth_dict.update(sixth_dict)
print(fifth_dict)

# nest: note we CAN nest a tuple as a key but we CANNOT nest a list as a key
the_tuple = (1, 6, 9)
the_dict = {the_tuple: 666}
print(the_dict)


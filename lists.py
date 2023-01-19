# just messing around with lists as a refresher for Python intermediate course by Patrick Loeber

my_list = ["napoleon", "kip", "pedro"]
print(my_list)

for i in my_list:
    print(i)

my_list2 = []

print(my_list2)

print(my_list[2])
print(my_list[-1])

test1 = "napoleon"
test2 = "rex kwon do"

if test1 in my_list:
    print(test1 + " is in the list")
else:
    print(test1 + " is not in the list")

if test2 in my_list:
    print(test2 + " is in the list")
else:
    print(test2 + " is not in the list")

amount = len(my_list)
print("There are", amount,"elements in the list.")

my_list.append("lawfawnduh")
print(my_list)

my_list.insert(0, "liger")
print(my_list)

removeme = my_list.pop()
print(removeme)
print(my_list)

removeme2 = my_list.remove("liger")
print(my_list)

my_list3 = []

for i in my_list:
    my_list3.append(i)

my_list.sort()

print(my_list)

my_list.reverse()

print(my_list)
print(my_list3)

new_list = ["tater tots"] * 3
print(new_list)

combined_list = new_list + my_list
print(combined_list)

sliced_list = combined_list[3:5]
print(sliced_list)
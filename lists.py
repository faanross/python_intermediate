# just messing around with lists as a refresher for Python intermediate course by Patrick Loeber

my_list = ["napoleon", "kip", "pedro", 69, False, 12.420]
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
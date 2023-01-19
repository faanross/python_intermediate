# just messing around with lists as a refresher for Python intermediate course by Patrick Loeber

my_list = ["napoleon", "kip", "pedro", 69, False, 12.420]
print(my_list)

for i in my_list:
    print(i)

my_list2 = []

print(my_list2)

print(my_list[2])
print(my_list[-1])

if "napoleon" in my_list:
    print("It is in the list")
else:
    print("It is not in the list")
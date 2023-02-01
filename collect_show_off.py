# Collections module:
# 1. Counter
# 2. namedtuple
# 3. OrderedDict
# 4. defaultdict
# 5. deque

# Counter is a container that stores elements as dictionary keys and their counts as dictionary values
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aabbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])

print(my_counter.most_common(2))
print(list(my_counter.elements()))

# named tuple continue is an easy to create and lightweight object type similar to a struct
# namedtuple - first argument is class name, second argument is another string that indicates all the fields we want seperated by a comma

Point = namedtuple('Point', 'x,y')
# This creates a class called Point with the fields x and y
pt = Point(1, -12)
print(pt)
print(pt.x)
print(pt.y)

# OrderedDict is a dictionary but where the ordered is remembered 
# Note however in Python 3.7 this is also the case for regular dicts, but for older ones you'll need to use this

ordered_dict = OrderedDict()

ordered_dict['a'] = 1 
ordered_dict['b'] = 2 
ordered_dict['c'] = 3 
ordered_dict['d'] = 4 
ordered_dict['e'] = 5

print(ordered_dict) # we can see there the order is the same, with old Python it will be random each time

# defaultdict: first we give it a default type, then we can fill it
# ensures only one type of data can be added to dict
d = defaultdict(int)
d['a'] = 1
d['b'] = 3
print(d)

# deque is a double-ended queue used to add or remove elements from both ends

deck = deque()

deck.append(420)
deck.append(69)
print(deck)

deck.appendleft(666)
print(deck)

# thus regular append adds value to right, appendleft adds it to the right

deck.pop()
print(deck)

deck.popleft()
print(deck)

deck.extend([4, 5, 6, 7])
print(deck)

deck.clear()
print(deck)

deck.extend([4, 5, 6, 7])
print(deck)
deck.rotate(1)
print(deck)
deck.rotate(2)
print(deck)
# Collections module:
# 1. Counter
# 2. namedtuple
# 3. OrderedDict
# 4. defaultdict
# 5. deque

# Counter is a container that stores elements as dictionary keys and their counts as dictionary values
from collections import Counter
a = "aabbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])

print(my_counter.most_common(2))
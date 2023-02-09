# We have a Python dictionary and want to convert it to JSON
# This is also known as serialization, or encoding

import json

napoleon = {
    "meal": "quesadilla",
    "numbers": 169,
    "sequence": [1, 2, 3],
    "girslike": {"skills": "computer_hacking"}
}

napoleonJSON = json.dumps(napoleon, indent=2)
print(napoleonJSON)

# now we can see it creates JSON output
with open('napoleon.json', 'w') as file:
    json.dump(napoleon, file, indent=4)

# now assume we want to do the inverse
# we want to convert json and assign to a new dictionaryd

new_example = json.loads(napoleonJSON)
print(new_example)

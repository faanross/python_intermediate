# Here we simply create 
with open('notes.txt', 'w') as file:
    user_text = input("What would you like to write? ")
    file.write(user_text)


file = open('notes.txt', 'w')
try:
    file.write('something else too...')
finally: 
    file.close()

# finally will execute with or without an exception vs try that is dependent

# Here we simply create 
with open('notes.txt', 'w') as file:
    user_text = input("What would you like to write? ")
    file.write(user_text)

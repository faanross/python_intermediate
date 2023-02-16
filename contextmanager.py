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

# example of using a lock (multi-threading)
from threading import Lock
lock = Lock()

lock.acquire()
#...We can do something safely - it is thread safe...#
#...And then we always have to call lock.release...#
lock.release()

# here is a more pythonic manner of achieving the same thing:
# with lock:
    #...Do something...#


################################################################
# How we might implement a context manager for our own classes #
################################################################

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()

            



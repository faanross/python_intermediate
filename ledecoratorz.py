# two different decorators: function decorators, and class decorators
# function, shown immediately below, is more common
# think of decorator as a function, that takes another function as an argument
# it can thus extend the functionality of a function, without modifying it

# in principle the dosummin() function is extended by adding the functionality of @mydecorator
# @mydecorator
# def dosummin():
#    pass

def start_end_decorator(func):
    def wrapper():
        

def print_name(x):
    print("Hello, "+x)

thename = input("What's your name? ")
print_name(thename)


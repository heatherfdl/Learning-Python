# Functions in python

# general form of python function is:
# def (define) function_name(arguments):
#   {lines telling function what to do to produce result}
#   return result (must use 'return')

# consider an example function that returns x^2 + y^2
def squared(x,y):  # need a colon and next line must be indented + funtion appears in light orange
    result = x**2 + y**2 #to put something to the power, put number fo * you wish to multiple by eg cubed = ***
    return result
# you can incorperate many more elements into this and it will just spit out the answer

print(squared(5,10)) # define x and y values so the function define above can run

# a new function
def born(country):
    return print("I am from " + country) # adding 2 strings together as a function

born("Canada") #define born function

#eg another example without any math
def age(number):
    return print("I am " + number + " years old.")

age("22")
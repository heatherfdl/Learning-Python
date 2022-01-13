# Python Types (booleans, strings, floats....)
print(type("Hello world")) # string (str)
print(type(13)) #integer
print(type(4.72)) # float (has a decimal)
print(type(True)) # bool

# moving to integers
print(4.72, int(4.72)) # will take input and product is as an integer (int)
print(4.05, int(4.05)) # Python will always round down to closest integer - can be manually overcome

#Rounding up
print(4.72, int(4.72), int(round(4.72)))
# should get result 4.72 (starting float), 4 (rounded down integer), and 5 (rounded up integer)
# round command works both ways up and down just like you would do in everyday life

#moving strings to integers
print("12345", int("12345")) # theyll look the same
print(type("12345")) # this is the string
print(type(int("12345"))) # this is the integer

#print("hello world")
#print(int("hello world")) # this will NOT work
# can only move strings to integers when they are NUMBERS - cannot do with words/characters

# Moving to floats
print(float(18)) # creates decimal - in this case 18.0
print(float("12345")) # should print "12345.0"

#Moving to strings
print(str(18))
print(str(19.5))
print(type(str(19.5))) # should result as a string (even though it looks like an integer - IT IS NOT!!)
# be careful not to mix up integers, floats, and strings. If you are doubting, check!

# logical operators
# there are 3 different logical operators: 'and', 'or', and 'not'
x = 6
print(x > 0 and x < 10) # should result as expression is True (x is greater than 0 AND less than 10)
# if you were to change to x < 5, would result in False

y = 24
print(y % 2 == 0 or y % 3 == 0) #whether y is divisible by 2 OR 3 (with remainder of 0) - can change the numbers
# will spit out True response even if just 1 of the statements is true (not necessarily both)
# if we put 'and', then both statements must hold. If one is false, the total output is false (and vice versa)






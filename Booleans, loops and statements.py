#Booleans used to store 2 values (true or false) - test whether result of expression is T or F
#True and False must be capatalized
print(True)
print("True")

print(type(True)) #this is a bool
print(type("True")) # this is a string

print(5 == 5) # should return true because statement is correct
print (6 == 5)# should return false because statement is incorrect

#Incorperating 'if' loop with boolean
x = 10
y = 5
if x % y == 0: #modular: if x divided by y results in remainder of 0 ...
    print(True)
else:
    print(False)

#'While' loop
number = 1  # our variable
while number < 4:
    print(number)
    if number == 4: # keep adding to 'number' until we reach 4 and then the while loop breaks
        break
    number = number + 1

#using else within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("Number is no longer less than 4")

# if loop with elif (basically 'or' argument)
number = 1
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")




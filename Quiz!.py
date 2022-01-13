

#Question 1 - Assigning Variables
x = 10
y = 20
# find addition, division, subtraction, and multiplcation
print(x + y)
print( x % y)
print(x - y)
print(x * y)

#Question 2 - Lists
#create lsit of all even numbers from 0 to 100
evennumbers = list(range(0, 100, 2)) #prints even numbers but only up until 98
evennumbers = list(range(0, 101, 2)) #prints only even numbers up to 100
print(evennumbers)
#print first 10 elements in list and find its length
print(evennumbers[0:11])
#append a value of your choice to the end of this list (can be any type)
evennumbers.append("woopsie")
print(evennumbers)

#Question 3 - Assign variables to integers
# Assign varaible to any integer you want and using if statement, find whether integer is divisible by 5
x = 100
if x % 5 == 0:
    print("x is divisible by 5.")
else:
    print("x is not divisible by 5.")
#get python to print if it is or isnt

#Question 4 - for loop
# using for loop, get python to print numbers 0 to 5
for i in range(6):
    print(i)

#Question 5
# draw a pentagon in turtle
import turtle
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.speed(0)
turtle.pensize(3)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.done()

#Question 6
# create a function that tests whether 3 numbers (a,b,c) are a Pythagorean triple
def pythag(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
print(pythag(3, 6, 9))
print(pythag(3, 9, 20))


# Question
# Tuples in Python

#tuples are a sequence of items of any type (BUT we want modify elements within them)
#tuples look like this
fruit = ("apples", 4, "bananas", 5, "oranges", 6)
print(type(fruit)) #prints that its a tuple
# in tuples vs lists, tuples use (), lists use []

fruitlist = ["apples",4, "bananas", 5, "oranges", 6]
print(type(fruitlist)) #this prints as a list

fruitlist[0] = "strawberries"
print(fruitlist) #substitutes apples with strawberries in the *list*
#we are able to modify elements within a list
#BUT we CANNOT modify elements within a tuple
#fruit[0] = "strawberries" #will generate an error because its a tuple

# we can perform similar operations on tuples like we can with lists
#Slicing tuples
print(fruit[0:3]) #creates a slice in the tuple
# Recalling elements in tuples
print(fruit[0])
# Concatenate tuples together
fruit = fruit[0:4] + ("cherries", 10)
print(fruit)

#tuples with 1 element
x = (5) #this is an integer, NOT a tuple
print(type(x))
# in tuples with 1 element, element must be seperated by ','
y = (5,) #this is a tuple
print(type(y))

#find length of a tuple (same command as list)
print(len(fruit))

#another way to create a tuple
anothertuple = tuple(("Hello", 18, True)) #can combine multiple types of elements
print(type(anothertuple))

# converting tuple to list, then back to tuple
fruit = list(fruit) #converts 'fruit' tuple into a list
print(type(fruit))
fruit.append("pears") #adds 'pears' onto end of list
print(fruit)
fruit = tuple(fruit) # turn the list back into a tuple with additional element

#Unpacking tuples
fruit = ("apples", "bananas", "pears", "oranges", "berries")
print(len(fruit))
(one, two, three, four, five) = fruit #creates another tuple with variables that assign according to position
print(one) #will print 'apples' because that is the variable we have 'assigned' it to
print(two) # this will print bananas
#another way
fruitlist
(one, *two) = fruitlist
print(one) #generates an error because we have 2 variables but 3 elements in our tuple
#use an '*' to work around the problem
print(one)
print(two) #when we place the '*', it assigns that variable to the rest of the tuple BUT as a list
# so we need to convert it back to tuple
print(tuple(two))
print(type(fruit))
# if you put '*' in the middle, it will assign variables from the front and back first until you reach the *,
#then it will use assign * to whatever elements remain in the middle

#Incorperating loops in tuples
for i in range(3):
    print(fruit[i]) # for i in range (), print the fruit of that element (eg range 3 will be apples, bananas, and pears)
#what about then we dont know how long a tuple is?
for a in range(len(fruit)):
    print(fruit[a]) #produces all of the elements within the tuple for its entire length



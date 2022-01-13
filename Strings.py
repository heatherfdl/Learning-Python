#Strings

#integers, floats, and booleans are considered 'simple' data types - cant be broken down
#lists and strings CAN be broken down

print("hello world") #this is a string
print(type("hello world"))

#operations on strings
#addition sign concatenation
greeting = "Hello "
name = "Heather"
print(greeting + name)

print("My shoe size is", 9, "and my age is", 22)

#* Operator
print(name * 3)
print(greeting + name*3) #prints greeting + name (x3) - use brackets to multiple whole statement
print ((greeting + name)*3)

#Index operator (slicing strings) - recall a specific element
name = "Ellie"
print(name[2]) #output is 3rd element in the list (ie the letter 'l')
print(name[0] + name[3]) #takes the 0th and 3rd element and concatenates (adds) them
print(name[0:2]) #dont forget that it always takes -1 from the end (so this should give elements in position 0 and 1)
print(name[0:6]) #prints the whole name

#Lowercase and Uppercase
myname = "Heather"
print(myname.upper()) #prints all uppercase
print(myname.lower()) #prints all lowercase

#Count how many times a character appears in a string
print(myname.count("e")) #counts how many times letter is is in "Heather"

#replace specific character with some other character
print(myname.replace("t", "d")) #replaces the character 't' in "Heather" with 'd'
#can also assign it as a new variable and recall it
newname = myname.replace("t", "d")
print(newname)

#Finding the length of a string
print(len(myname)) #'len' gives the length of inputed string (in this case Heather)

#Format strings
#yourname = input("Your name: ")
#hello = "Hello {}".format(yourname) #this is NOT concatenation, but rather joining strings in single phrase
#print(hello)

#Each letter in Python is assigned to a specific number
#means we can do math with strings
print("Orange" < "Strawberry") #gives TRUE output, but why?...
print(ord("o")) #the character 'o' is assigned to the number 111
print(chr(38)) #the character that corresponds to 38 is '&'
#Characters and NOT limited to letters - they can be anything on the keyboard
#Lowercase and uppercase have different values
#this allows us to perform math on strings

# in and not operators
fruit = "banana"
print("a" in fruit) #Print whether a is in variable fruit (it is so True)
print("s" not in fruit) #print whether there are no 's' in fruit (there are not so True)

#Incorperating things together
x = "hello"
y = ""
for character in x: #for each character in x, let y = (that character) in uppercase + y
    y = character.upper() + y
print(y)
#essentially prints it backwards (if you do y + character.upper(), it prints normally)



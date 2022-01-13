# allows multiple interations of something
#create a list
mylist = [5, 8, 10, 12]
#add 5 to each element in the list using the 'for' loop
for element in mylist:
    element = element * 5
    print(element)
# for every element in list, takes element and adds 5 to it - 'for' loop repeats the function for all the elements in the list
#print has to stay within 'for' loop (will loop anything within indented space)

#'if' loop
a = 15
if a % 2 == 0:
    print("a is divisible by 2")
else:   #if 'if' command not true, then will be run 'else' loop
    print("a is not divisible by 2")
#% is modulous sign - produces an integer ** dont forget colon, signifies begining of a loop **
# == means we are not assigning a new variable, but rather a true output (exact output)


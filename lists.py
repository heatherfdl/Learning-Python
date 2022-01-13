mylist = [1, 2, 3, 4, 5, 6]
#mylist2 = list(range(1, 7))
#print(mylist2)

print(mylist)

#operations on lists
print(mylist[2])
#returns 2nd element in list (starting from position 0)
print(mylist[-1])
#returns last element in a list (for example if you dont know how many elements are in a list)

#create a slice from the 2nd to the 4th element
print(mylist[1:4])

#get length of a list
print(len(mylist))

#max and min in a list
print(min(mylist))
print(max(mylist))

#add element into list (add a number on to the end of a list)
mylist.append(120)
print(mylist)

#reverse a lit
mylist.reverse()
print(mylist)

#what if we have another list - add two lists together (create 1 list out of 2 NOT ADDING)
mylist2 = [10, 11, 12, 13, 14, 15, 16]
print(mylist + mylist2)


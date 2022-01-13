#Random Password Generator Mini Project

# importing relevent modules
from random import randint

#all uppercase password
password = "" #start with empty string (because we will populate it with random characters)
for i in range(10): #how long we want our password
    i = chr(randint(65,90)) #lets i = random character between 65 and 90 (corresponds to capital letters)
    password = str(password) + i #set password as a string and add i (defined above) onto it, repeated 10 times
print(password) #produced random password that is 10 characters long

#Upper and lowercase password
password2 = ""
for a in range(5):
    a = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower
    password2 = str(password2) + a + j
print(password2)


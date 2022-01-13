#weighted exam score avarage

# entering how many exams you have done
numberofexams = int(input("Enter number of exams: "))

# entering how many credits exams cover
totalcredits = int(input("Enter how many credits these exams cover: "))

#'for' loop (need average to start at 0 because we add on percentages for each exam)
average = 0
for exam in range(numberofexams):
    score = int(input("Enter exam score: "))
    examcredits = int(input("Enter how many credits this exam covered: "))
    average = average + score*examcredits/totalcredits
print("Your average is ", average)
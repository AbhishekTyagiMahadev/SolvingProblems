maths = int(input("Enter marks of Maths : "))
check = maths<33

english = int(input("Enter marks of English : "))
check = english<33

hindi = int(input("Enter marks of Hindi : "))
check = hindi<33

science = int(input("Enter marks of Science : "))
check = science<33

computer = int(input("Enter marks of Computer : "))
check = computer<33

marks = maths + english + hindi + science + computer
percentage = marks/5

if 90 <= percentage <= 100:
    grade = "Ex"
elif 80 <= percentage < 90:
    grade = "A"
elif 70 <= percentage < 80:
    grade = "B"
elif 60 <= percentage < 70:
    grade = "C"
elif 50 <= percentage < 60:
    grade = "D"
elif percentage < 50:
    grade = "F"
else:
    grade = "Invalid marks"

print("Total Marks = ", marks,"\nPercentage = ", percentage, "%\nGrade:", grade)
if(check==True):
    print("Sorry you are failed!")
elif(percentage<40):
    print("Sorry you are failed!")
else:
    print("Passed")

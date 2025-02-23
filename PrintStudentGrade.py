#Get mark of student from user
mark = float(input("Enter mark of student: "))
#Check grade
if mark >= 90:
    print("Grade A")
elif mark >=80:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 35:
    print("Grade D")
else:
    print("Fail")
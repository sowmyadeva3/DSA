#Get first name from user
firstName = input("Enter first name: ")
#Get last name from user
lastName = input("Enter last name: ")
#Get n from user
numberOfTimes = int(input("Enter number of times to print: "))
#Initialize counter to 0
counter = 0
#Concatenate name
fullName = firstName + lastName
#Print fullName 'n' times
while counter < numberOfTimes:
    print(fullName)
    counter+=1


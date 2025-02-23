#Get value of x from user
x = int(input("Enter x: "))
#Initialize multiplier to 1
multiplier = 1
# Print multiples of x until 1000
while x*multiplier <= 1000:
    print(x*multiplier)
    multiplier+=1

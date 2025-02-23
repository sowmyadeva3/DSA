# Get the 3 angles
angle1 = float(input("Enter the 1st angle: "))
angle2 = float(input("Enter the 2nd angle: "))
angle3 = float(input("Enter the 3rd angle: "))
# check if sum of angles is 180
if angle1+angle2+angle3 == 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
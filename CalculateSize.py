#Get numerical value from user
value = float(input("Enter a numerical value: "))
#Print the size based on teh value
match value:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("XLarge")
    case _:
        print("Invalid")
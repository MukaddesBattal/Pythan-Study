User_Number = input("Please enter a positive integer number: ")
if User_Number.isdigit() and int(User_Number) > 0 :
    Number_Len = len(User_Number)
    Sum = 0
    for i in User_Number:
    Sum += int(i) ** Number_Len
    if Sum == int(User_Number):
        print(User_Number, "is An Armstron Number")
    else:
        print(User_Number, "is not An Armstron Number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

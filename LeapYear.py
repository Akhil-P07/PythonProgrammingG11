#Program checks whether if a inputted year is a leap or not
print("Note: To enter Year in BCE type it as a negative equivalent number", end='\n' "      Do not type BCE, CE, AD or BC at the end of year")
print(" ")
yr = int(input("Enter year: "))
a = yr % 4
b = yr % 10 + yr % 100
if ( b == 0):
    if (yr % 400 == 0):
        if (yr >= 0):
            print(yr, "CE is a leap year")
        else:
            print(-1 * yr, "BCE is a leap year")
    else:
        print(yr, "is not a leap year")
else:    
    if (a == 0):
        if (yr >= 0):
            print(yr, "CE is a leap year")
        else:
            print(-1 * yr, "BCE is a leap year")
    else:
        print(yr, "is not a leap year")

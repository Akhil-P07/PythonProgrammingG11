months = ["January", "Febuary", "March","April","May","June","July", "August", "September", "October", "November","December"]
a = int(input("Enter year(In AD or CE): "))
yr = dict()
x= a % 4
y = a % 10 + a % 100
feb_day = 28 #Non-Leap year no. of days
if ( y == 0):
    if (a % 400 == 0):
        feb_day = 29
else:    
    if (x == 0):
        feb_day = 29
for i in range(12):
    if (i == 1):
        yr[months[i]] = feb_day
    elif( i < 7):
        if (i%2 == 0):
            yr[months[i]] = 31
        elif(i%2 != 0):
            yr[months[i]] = 30
    else:
        if (i%2 == 0):
            yr[months[i]] = 30
        elif(i%2 != 0):
            yr[months[i]] = 31

print(yr)        

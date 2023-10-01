#Checks if whether number is even or odd 
num1 = int(input("Enter num: "))
num = num1 % 2
if(num == 0):
    print(num1, "is Even")
elif (num != 0):
    print(num1, "is Odd")
else:
    print("Error: Invalid number entered")
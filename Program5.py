#Takes 3 numbers and prints the largest of the 3 numbers.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if(num1 > num2 and num3):
    print(num1, "is the greatest")
elif(num2 > num1 and num3):
    print(num2, "is the greatest")
elif(num3 > num1 and num2):
    print(num3, "is the greatest")
else:
    print("No number is greater")

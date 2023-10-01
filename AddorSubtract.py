#Addition and subtraction only
num1 = int(input("Enter 1stNum: "))
num2 = int(input("Enter 2nd Num: "))
oper = input("Enter operation: ")
if (oper == "-" or "subtract"):
    print(num1 - num2)
elif(oper == "+" or "add"):
    print(num1 + num2)
else:
    print("error")

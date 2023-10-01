#Addition and subtraction only
print("Enter numbers to do operation then choose + or -\n")
num1 = int(input("Enter 1st Num: "))
num2 = int(input("Enter 2nd Num: "))
oper = input("Enter operation: ")
if (oper == "-"):
    print("result: ",num1 - num2)
elif(oper == "+"):
    print("result: ",num1 + num2)
else:
    print("error")

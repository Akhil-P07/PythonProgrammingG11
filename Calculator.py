a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
print("Note:\nTo add use: +\nTo Subtract use: -\nTo multiply use: * \nTo Divide use: /\n")
op = input("Enter operation: ")

if (op == "+"):
    print("Result:", a + b)

elif(op == "-"):
    print("Result:", a - b)

elif(op == "*"):
    print("Result:", a * b)

elif(op == "/"):
    print("Resullt:", a/b)

else:
    print("Error: Invalid Operation")
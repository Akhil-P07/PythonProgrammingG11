#Multi-Operation Calculator
a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
op = input("Enter operation: ")

if (op == "+"):
    print("Result:", a + b)
elif(op == "-"):
    print("Result:", a - b)
elif(op == "*"):
    print("Result:", a * b)
elif((op == "/") and (b != 0)):
    print("Result:", a/b)
else:
    print("Error: Invalid Operation")
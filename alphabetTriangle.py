alpha = ["A", "B", "C", "D", "E", "F"]
op = int (input("Choose 1 for '*' type triangle and 0 for Alphabet type triangle: "))
if (op == 0):
    for i in range(6):
        for j in alpha[:i + 1]:
            print(j,end="")
        print()
elif (op == 1):
    for i in range(6):
        for j in range(i + 1):
            print("*", end="")
        print()
else:
    print("Error: Invalid operation selected")
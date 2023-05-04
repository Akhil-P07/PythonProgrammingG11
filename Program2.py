print("Note: Only area of circle, square and rectangle operations are avaliable")
oper = input("Enter operation: ")
if (oper == "circle"):
    r = float(input("Enter radius of circle: "))
    print("Area is", 3.14 * r **2)
elif (oper == "square"):
    s = float(input("Enter side length: "))
    print("Area is", s ** 2)
elif (oper == "rectangle"):
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area is", l * b)
else:
    print("Error: Invalid operation or number.")

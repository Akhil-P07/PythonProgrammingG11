#Body-Mass-Index Calculator
h = float(input("Enter height(in meters): "))
w = float(input("Enter weight(in kg): "))
bMI = w/h**2
if bMI <= 18.4:
    print("Underweight")
elif bMI >= 18.5 and bMI <= 24.9:
    print("Normal")
elif bMI >= 25.0 and bMI <= 39.9:
    print("Overweight")
else:
    print("Obese")
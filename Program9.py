a = int(input("Enter for factorial: "))
b = 1
if a == 0:
    print(a, "factorial is", 1)
else: 
    for i in range(1, a + 1):
        b *= i
    print(a, "factorial is", b)
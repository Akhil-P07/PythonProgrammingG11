a = int(input("Enter for factorial: "))
b = 1
for i in range(1, a + 1):
    b *= i
print(a, "factorial is", b)
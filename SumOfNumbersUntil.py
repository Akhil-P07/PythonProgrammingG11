n = int(input("Enter highest natural num: "))
a = 0
for i  in range(0, n + 1):
    a += i
print("Sum of all natural numbers until",n, "is", a)
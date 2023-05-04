n = float(input("Enter num: "))
b = int(input("Enter largest divisor: "))
i = 0
while (i <= n):
    if (i == 0):
        continue
    else:
        print(n, "/", i, "=", n/i)
    i += 1
    if (n < 0):
        print("error")
        break
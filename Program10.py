num = int(input("Enter num for table: ")) #Finds multiplication table of this num
r = int(input("Enter largest multiple of given numm: "))
for i in range(1, r + 1):
    print(num, "X", i, "=", num * i)

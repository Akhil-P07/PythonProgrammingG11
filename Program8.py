#Prints fibonacci series of numbers set
n = int(input("Max number of elements in series: "))
a = 0
b = 1
c = 0
print(str(a) +", " + str(b), end = ", ")
for i in range(n - 2):
    c = a + b
    if (i == n - 3):
        print(c)
    else:
        print(c, end=", ")
    a = b
    b = c
print("Here is your fibonacci sequence of", n, "numbers :)")

    
    
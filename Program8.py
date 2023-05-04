#0,1,1,2,3,5,8,13,21,34
n = int(input("Max number of elements in series: "))
a = 0
b = 1
c = 0
print(a)
print(b)
for i in range(n - 2):
    c = a + b
    print(c)
    a = b
    b = c
print('')
print("Here is your fibonacci sequence of", n, "numbers :)")

    
    
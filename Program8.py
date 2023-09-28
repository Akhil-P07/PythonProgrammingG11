#Prints the fibonacci sequence until the last set number eg. 0,1,1,2,3,5,8,13
max = int(input("Enter the largest no. in the fibonacci sequence: "))
a = 0
b = 1
while (b < max):
    print(a,b,end=" ")
    a += b
    b += a


    
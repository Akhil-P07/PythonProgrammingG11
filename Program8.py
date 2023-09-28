#Prints the fibonacci sequence until the last set number eg. 0,1,1,2,3,5,8,13
max = int(input("Enter largest no. in sequence: ")) 
a = 0
b = 1
seq=list()
for i in range(max):
    seq.append(a)
    seq.append(b)
    if (a > max):
        max = a
        break
    elif (b > max):
        max = b
        break
    a += b
    b += a
loc = seq.index(max)
for i in seq[:loc]:
    print(i, end =" ")

    
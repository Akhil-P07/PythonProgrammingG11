lim = int(input("Enter largest number in triplet: "))
a,b,c = 0,0,0
trplt = list()
#Triplet program
for b in range(1,lim + 1):
    for a in range(1,b+1):
        c = (a**2) + (b**2)
        c = c**(1/2)
        if (c == int(c)):
            if c > lim:
                break
            trplt.extend([[a,b,int(c)]])
n = 1
#Ordering
for i in trplt:
    n += 1
no = 0
for i in str(n):
    no+= 1
n = 1
count = 1
for i in trplt:
    if (n % (10 ** count)  == 0):
        no -= 1
        count +=1
    elif(no == 0):
        no = 0
    print("%i." %(n), end ="")
    n +=1
    print(" "*no, end="")
    for j in i:
        print(j, end =" ")
    print()

                
                
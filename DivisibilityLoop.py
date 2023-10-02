x = int(input("Enter num: "))
a = list()
for i in range(1, x):
  if(x % i == 0):
    a.append(i)
print("The Following numbers divide %i: "%(x))

for j in a:
  print(j, end=", ")
print(x)
 
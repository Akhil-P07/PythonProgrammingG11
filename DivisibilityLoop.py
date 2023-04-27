x = int(input("Enter num: "))

a = range(1, 11)

print("Numbers divisible by ", x, " are the following: ")

for i in a:
  if (i % x == 0):
    print(i)
end = 1
reg = dict()
while (end == 1):
    name = input("Enter student name: ")
    rolln = int(input("Enter students roll number: "))
    reg[name] = rolln
    end = int(input("Press 1 to Continue and 0 to Exit: "))
print(reg)
   
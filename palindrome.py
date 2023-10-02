a = input("Enter text: ")
if (a == a[::-1]):
    print("%s is a Palindrome"%(a))
else:
    print("%s is not a Palindrome"%(a))
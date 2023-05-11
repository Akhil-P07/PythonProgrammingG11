#Guessing game Implementing the concept of jump statements
import random 
mxGuess = 10 #Set maximum number of guesses here
num = random.randint(1, 101)
check = 1
print("Welcome to @YourMamaGae2007's Guessing Game")
for i in range(mxGuess):
    guess = int(input("Enter guess: "))
    if(guess == num):
        print("Correct! the number was indeed", num)
        print("You took", i + 1, " turns")
        break
    elif(guess != num and i != mxGuess - 1):
        print("Incorrect! Try again")
        if(guess < num):
            print("Go higher")
        else:
            print("Go lower")
        continue
    print("Out of turns :(")


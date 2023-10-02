import random
print("Welcome to lottery simulator!")
turns = 3 #Set turns
spin_time = 2000 #Lottery timer Recommended: 2000 above
match = int(input("Press 1 to begin match or 0 to quit: "))
score = dict()
while(match == 1):
    name = input("Enter your Username: ")
    score[name] = {"Score":0, "Turns": turns}
    while ((score[name]["Turns"] <= turns) and (score[name]["Turns"] > 0) ):
        game = int(input("Press 1 to roll or 0 to quit: "))
        if(game == 1):
            for i in range(spin_time): 
                a = random.randint(1,6)
                b = random.randint(1,6)
                c = random.randint(1,6)
                print("| %i    %i    %i |"%(a,b,c))
            if((a == b) and (b==c) and (a == c)):
                print("JACKPOT! +300")
                score[name]["Score"] += 300
            elif((a==b) or (b==c) or (a==c)):
                print("SYMPATHY POINTS! +75")
                score[name]["Score"] += 75
            else:
                print("YOU LOST! -100")
                score[name]["Score"] -= 100 
            score[name]["Turns"] -= 1 
                 
        else:
            break
        print("You have %i turns left"%(score[name]["Turns"])) 
    print("Out of turns :(\n")
    match = int(input("Press 1 to begin match or 0 to quit: "))

#Prints scores of all players
print("===========SCOREBOARD===========")
for name in score:
    print(name,"---->",score[name]["Score"])
    

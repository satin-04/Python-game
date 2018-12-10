
import random
print("1-STONE\n2-PAPER\n3-SCIZZOR")
"""
1="STONE"
2="PAPER"
3="SCIZZOR"
"""
l=[1,2,3]
user_score=0
comp_score=0
while True:
    n=int(input("\nEnter a number: "))
    if(n>3 or n<0):
        print("Invalid Input")
    else:
        d=random.choice(l)
        if(n==1):
            if(d==2):
                print("USER: STONE    COMPUTER: PAPER")
                comp_score=comp_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==1):
                print("USER: STONE    COMPUTER: STONE")
                print("TIE")
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==3):
                print("USER: STONE    COMPUTER: SCIZZOR")
                user_score=user_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)

        if(n==2):
            if(d==3):
                print("USER: PAPER    COMPUTER: SCIZZOR")
                comp_score=comp_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==2):
                print("USER: PAPER    COMPUTER: PAPER")
                print("TIE")
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==1):
                print("USER: PAPER    COMPUTER: STONE")
                user_score=user_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)

        if(n==3):
            if(d==1):
                print("USER: SCIZZOR    COMPUTER: STONE")
                comp_score=comp_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==3):
                print("USER: SCIZZOR    COMPUTER: SCIZZOR")
                print("TIE")
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
            if(d==2):
                print("USER: SCIZZOR    COMPUTER: PAPER")
                user_score=user_score+1
                print("Computer score: ",comp_score)
                print("User score: ",user_score)
    
    if(user_score==5):
        print("User Won")
        break
    if(comp_score==5):
        print("Comp Won")
        break









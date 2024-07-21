import random
user_score=0
comp_score=0
count=3
while count>0:
    user=int(input("Enter your choice\n0 for SNACK\n1 for WATER\n2 for GUN\n= "))
    choices=["snack","water","gun"]
    comp=random.choice(choices)

    if user==0 and comp=="water" or user==1 and comp=="gun" or user==2 and comp=="snack":
         user_score+=1
         print("You win, computer lose the match, you got",user_score,"points")
         
    
    elif user==0 and comp=="gun" or user==1 and comp=="snack" or  user==2 and comp=="water":
        comp_score+=1
        print("You lose, computer win the match, computer got",comp_score,"points")
        
    
    elif user==1 and comp=="water" or user==2 and comp=="gun" or user==0 and comp=="snack":
        print("Draw match")
    
    count-=1
print("Final score:")
print("USER: ",user_score)
print("COMPUTER: ",comp_score)
if user_score>comp_score:
    print("You are the winner")
else:
    print("Computer is the winner")
        


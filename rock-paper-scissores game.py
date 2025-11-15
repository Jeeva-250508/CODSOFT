import random
options=["rock","paper","scissor"]
Try_again="y"
p_score=0
c_score=0
while Try_again.lower()=="y":
    computer=random.choice(options)
    player=None
    while player not in options:
        player=input("Enter a choice rock or paper or scissors:").lower()
    print("player=",player)
    print("computer=",computer)
    if player.lower()==computer:
        print("It's a tie")
        p_score+=1
        c_score+=1
    elif player.lower()=="rock"and computer=="scissor" :
        print("You win")
        p_score+=1
    elif player.lower()=="paper"and computer=="rock" :
        print("You win")
        p_score+=1
    elif player.lower()=="scissor"and computer=="paper" :
        print("You win")
        p_score+=1
    else:
         print("You lose")
         c_score+=1
    Try_again=input("Do you want to play again(y/n):")
print()    
if p_score > c_score:
    print("Player won with a score",p_score,"-",c_score)
elif p_score < c_score:
    print("Computer won with a score",c_score,"-",p_score)
else:
    print("It's a tie!",c_score,"-",p_score)    
           




        
            
    
    

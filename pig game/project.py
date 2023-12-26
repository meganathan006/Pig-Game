import random
def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll



while True:
    players=input("Enter no.of player (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print("player between (2-4) ")
    else:
        print("invalid,try again") 
 


max_score= 50
player_score=[0 for x in range(players)]
while max(player_score)< max_score:
    for player_idx in range(players):
        print("\n","player number",player_idx + 1,"turn has just started!")
        print("your total score is .........",player_score[player_idx],"\n") 
        current_score=0
        while True:

            should_roll=input("would you like to roll (y)? : ")
            if should_roll.lower()!="y":
               break
            value=roll()
            if value==1:
               print("you rolled a 1! Turn done.....")
               current_score=0
               break
            else:
                current_score=current_score+value
                print("you rolled a:",value)
            print("your score is :",current_score)        
        player_score[player_idx]+=current_score
        print("your total score is ",player_score[player_idx]) 

max_score=max(player_score)
winner=player_score.index(max_score)
print("player number",winner+1,"is the winner with score of",max_score)          
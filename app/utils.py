import random

d = [2,3,4,5,6,7,8,9,10,10,10,10,11]
dealer_showcard = (random.choice(d))

Dealer = print("The dealer's faceup card is a", dealer_showcard,".")

player_showcard1 = (random.choice(d))
player_showcard2 = (random.choice(d))

Player = print("The player's faceup cards are", player_showcard1, "and", player_showcard2,".")

Question = input("What would you do in this situation? Hit, stay, or split?")
 
if player_showcard1 == ("11") and player_showcard2 == ("10"):
    Print("You have blackjack! You win!")
elif player_showcard1 == ("10") and player_showcard2 == ("11"):
    Print("You have blackjack! You win!")
else:
    Question
            
    
        


from utils import dealer_showcard
from utils import Dealer
from utils import player_showcard1
from utils import player_showcard2
from utils import Player
from utils import Question
from utils import blackjack


Dealer
Player
Question

if Question == "Hit" or "Stay" or "Split":
    if player_showcard1 == player_showcard2 and player_showcard1 > dealer_showcard:
        print("The best decision here is to split.")
    elif player_showcard1 + player_showcard2 <= 11:
        print("The correct choice is to hit. You can hit with no worries of busting.")
    elif player_showcard1 + player_showcard2 >= 17:
        print("It is too risky to hit. You should just stay.")
    elif player_showcard1 + player_showcard2 >= 10 + dealer_showcard:
        print("You're in a good position. The best move is to stay.")
    elif player_showcard1 + player_showcard2 < 10 + dealer_showcard:
        print("The dealer has a good position. Most of the time you want to hit.")
 
else:
    print("That is not a valid choice. Try Again.")
    exit()             

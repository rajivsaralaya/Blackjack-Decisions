from random import choice
from app.utils import dealer_showcard
from app.utils import player_showcard1
from app.utils import player_showcard2
#who is ahead in the hand

def ahead(dealer_showcard,playershowcard1,playershowcard2):
    if player_showcard1 + player_showcard2 >= dealer_showcard + 10:
        assert("player is ahead in the hand")
    elif player_showcard1 + player_showcard2 < dealer_showcard + 10:
        assert("dealer is ahead in the hand")

def stay_hand(playershowcard1,playershowcard2):
    if playershowcard1 + playershowcard2>=17:
        assert("the player should stay no matter what")
    elif player_showcard1 + player_showcard2<=11:
        assert("the player should hit not matter what")
    else:
        assert("the player is in a tough spot and should stay if ahead in the hand and hit if behind in the hand")
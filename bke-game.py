import random
import matplotlib.pyplot as plt
 
from bke import EvaluationAgent, MLAgent, is_winner, opponent, RandomAgent, train_and_plot, start
from bke import HEADLESS
 
class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1,500)

class MyAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):        
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 5;
        if board[0] == my_symbol:
            getal = getal + 1;
        if board[2] == my_symbol:
            getal = getal + 1;
        if board[6] == my_symbol:
            getal = getal + 1;
        if board[8] == my_symbol:
            getal = getal + 1; 
        
        return getal



my_agent = MyAgent()
rand_agent = MyRandomAgent()


win = { "X":0,"O":0, "D" : 0}    
for x in range(100):
    w = start(player_o = rand_agent, player_x=my_agent, ui=HEADLESS)    
    if isinstance(w, str):
        win[w] += 1
    else:
        win["D"] += 1
        
print(win)





    
    

from ast import Continue
import random

class RockPaperScissors:
    def __init__(self, itemsDict, userScore, compScore):
        self.userScore = userScore
        self.compScore = compScore
        self.itemsDict = itemsDict

    def playRounds(self, rounds):
            print("\n****** ROUND "+ str(rounds) + " ******")
            print("*** Player's Turn ***")
            
            while True:
                userIn = input("Pick \t\"R\" for Rock, \t\"P\" for Paper, \tOr \t\"S\" for Scissors \n").upper()
                if userIn in self.itemsDict.keys():
                    break
                else:
                    print("\n*** WRONG INPUT ***")
                    continue

            print("******  **** ******")
            print("*** CPU's Turn ***")
            compIn = random.choice( list(self.itemsDict.keys()) )
            print(compIn)

            if (userIn == 'R') and (compIn == 'S') or \
                (userIn == 'S') and (compIn == 'P') or \
                    (userIn == 'P') and (compIn == 'R') :
                    self.userScore += 1
                    print("Player ("+ self.itemsDict[userIn] + ")", " : ", "CPU ("+ self.itemsDict[compIn] + ")")
                    print("**** Player Wins ****")

            elif (compIn == 'R') and (userIn == 'S') or \
                (compIn == 'S') and (userIn == 'P') or \
                    (compIn == 'P') and (userIn == 'R') :
                    self.compScore += 1
                    print("Player ("+ self.itemsDict[userIn] + ")", " : ", "CPU ("+ self.itemsDict[compIn] + ")")
                    print("**** CPU Wins ****")
                    
            elif (compIn == 'R') and (userIn == 'R') or \
                (compIn == 'S') and (userIn == 'S') or \
                    (compIn == 'P') and (userIn == 'P') :
                    print("Player ("+ self.itemsDict[userIn] + ")", " : ", "CPU ("+ self.itemsDict[compIn] + ")")
                    print("It's a Tie -- No Winner")
        
            return [self.userScore, self.compScore]

    def chkScores(self):
        if (self.userScore > self.compScore):
            print("\n*** WINNER --- PLAYER ***\n Congratulations\n")
        elif (self.compScore > self.userScore):
            print("\n*** WINNER --- CPU ***\n Player Losses... Better Luck Next Time\n")
        else:
            print("\nIt's a Draw -- No Winner")

#--------------**********************------Main Program Starts here--------*****************************
play = "Y"
while play == "Y":
    print("\n*** GAME INSTRUCTIONS *** \n Rock beats Scissors \n Paper beats Rock \n Scisors beats Paper")

    itemsDict = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}
    obj = RockPaperScissors(itemsDict, 0, 0)

    for x in range(1,4): 
        finScore = obj.playRounds(x)
        print("Player " + str(finScore[0]) + " vs. CPU " + str(finScore[1]))
    

    obj.chkScores()
    play = input("\nDo You Want To Play Again? \"(Y/N)\" \n").upper()
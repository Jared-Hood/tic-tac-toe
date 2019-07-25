add-GUI
import random

class AI():
    def __init__(self, difficulty=1, moves= [1,2,3,4,5,6,7,8,9]):
        self.diff = difficulty
        self.moves = moves

    def makeMove(self, difficulty, moves):
        self.diff = difficulty
        self.moves = moves

        if self.diff == 1:
            move = self.easy()

        elif self.diff==2:
            move = self.medium()

        elif self.diff==3:
            move = self.hard

        return move

    #randomly selects and open square
    def easy(self):
        move = self.moves[random.randrange(len(self.moves))]
        return move

    #Makes an obvious move to prevent player win or for itself to win
    def medium(self):

        pass


    #Makes perfect move everytime using minmax algorithm
    def hard(self):
        pass


#Use min-max algorithm for AI
#Recursive
 master

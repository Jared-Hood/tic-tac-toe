import random

class AI():
    def __init__(self, difficulty=1, moves= [1,2,3,4,5,6,7,8,9]):
        self.diff = difficulty
        self.moves = moves
        self.x_moves = []
        self.o_moves = []

    def makeMove(self, difficulty, moves, x, o):
        self.diff = difficulty
        self.moves = moves #open moves
        self.x_moves = x #moves made by player
        self.o_moves = o #moves made by computer

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

        #check for win
        wins = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

        for m in self.moves:
            copy_o_moves = self.o_moves.copy()
            copy_o_moves.append(m)
            for win in wins:
                if ( win[0] in copy_o_moves and win[1] in copy_o_moves and win[2] in copy_o_moves):
                    return m

        #prevent player win
        for m in self.moves:
            copy_x_moves = self.x_moves.copy()
            copy_x_moves.append(m)
            for win in wins:
                if ( win[0] in copy_x_moves and win[1] in copy_x_moves and win[2] in copy_x_moves):
                    return m

        #else make random move
        else:
            move = self.moves[random.randrange(len(self.moves))]
            return move

    #Makes perfect move everytime using minmax algorithm
    def hard(self):
        pass


#Use min-max algorithm for AI
#Recursive

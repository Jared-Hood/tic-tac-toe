import random

class AI():
    def __init__(self, difficulty=1, moves= [1,2,3,4,5,6,7,8,9]):
        self.diff = difficulty
        self.moves = moves
        self.wins = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
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
            state = [""] * 10
            for x in self.x_moves:
                state[x] = "X"
            for o in self.o_moves:
                state[o] = "O"
            state[0] = 0

            c_turn = True
            move = self.hard(c_turn, state, 0)

            for i in range(1,10):
                if move[i] != state[i]:
                    return i

        return move

    #randomly selects and open square
    def easy(self):
        move = self.moves[random.randrange(len(self.moves))]
        return move

    #Makes an obvious move to prevent player win or for itself to win
    def medium(self):

        #check for win
        for m in self.moves:
            copy_o_moves = self.o_moves.copy()
            copy_o_moves.append(m)
            for win in self.wins:
                if ( win[0] in copy_o_moves and win[1] in copy_o_moves and win[2] in copy_o_moves):
                    return m

        #prevent player win
        for m in self.moves:
            copy_x_moves = self.x_moves.copy()
            copy_x_moves.append(m)
            for win in self.wins:
                if ( win[0] in copy_x_moves and win[1] in copy_x_moves and win[2] in copy_x_moves):
                    return m

        #else make random move
        else:
            move = self.moves[random.randrange(len(self.moves))]
            return move


    #Makes perfect move every time using minimax algorithm
    #Computer is maximizer while simulated player is minimizer
    #Computer is always "O"
    def hard(self, c_turn, state, depth):
        branches = self.branches(state, c_turn)
        for branch in branches:
            branch[0] = self.branch_eval(branch, c_turn, depth)

        #find min or max value depending on whose turn it is
        if depth != 0:
            best_branch = branches[0]
            #maximize is c_turn
            if c_turn:
                for b in branches:
                    if int(b[0]) > int(best_branch[0]):
                        best_branch = b
            else:
                for b in branches:
                    if int(b[0]) < int(best_branch[0]):
                        best_branch = b

            return best_branch[0]

        if depth == 0:
            best_score = branches[0][0]
            for b in branches:
                if int(b[0]) > best_score:
                    best_score = b[0]


            best_branches = []
            for b in branches:
                if b[0] == best_score:
                    best_branches.append(b)

            random.shuffle(best_branches)

            return best_branches[0]

    def branch_eval(self, branch, c_turn, depth):

        result = self.checkwin(branch)
        if result != 0:
            return result

        # determine if tie
        count = 0
        for i in range(1, 10):
            if branch[i] == "":
                count += 1
        if count == 0:
            return 0

        return self.hard(not c_turn, branch, depth + 1)

    #return 0 for tie, 1 for win, -1 for loss
    def checkwin(self,state):
        for win in self.wins:
            if (state[win[0]] == "X" and state[win[1]]== "X" and state[win[2]] == "X"):
                return -1
            elif (state[win[0]] == "O" and state[win[1]]== "O" and state[win[2]] == "O"):
                return 1
        return 0

    #return all the possible branches for the current state
    def branches(self, state, c_turn):
        branches = []
        if c_turn:
            for i in range(1,10):
                if state[i] == "":
                    branch = state.copy()
                    branch[i] = "O"
                    branches.append(branch)
        else:
            for i in range(1,10):
                if state[i] == "":
                    branch = state.copy()
                    branch[i] = "X"
                    branches.append(branch)

        return branches
import random

class board:

    def __init__(self):
        self.matrix = [["-" for i in range(3)] for j in range(3)]
        self.playerTurn = True
        self.nextGamePlayerStart = False
        self.openMoves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        self.gameOver = False
        self.win = False
        self.winner = ""
        self.playerWins = 0
        self.computerWins = 0

    def print(self):
        for row in self.matrix:
            print('[%s]' % ' , '.join(map(str, row)))

    def move(self):

        self.findOpen()

        if len(self.openMoves) == 0:
            print("No more available moves")
            self.gameOver = True


        elif self.playerTurn:
            while True:

                    moveRaw = input("input your move coordinate starting in the top left as 0,0\n")
                    move = (int(moveRaw[0]), int(moveRaw[2]))

                    if move not in self.openMoves:
                        print("Illegal move")

                    else:
                        self.matrix[move[0]][move[1]] = "X"
                        self.playerTurn = False
                        break

        else:

            move = self.openMoves[random.randrange(len(self.openMoves))]
            print("Computer moves: ",end=' ')
            print(move)

            self.matrix[move[0]][move[1]] = "O"
            self.playerTurn = True

        if self.checkWin():
            print("Player: " + self.winner + " wins!")
            if self.winner == "X":
                self.playerWins += 1
            else:
                self.computerWins += 1

    #check rows, columns, then diagnals
    def checkWin(self):
        current_player = ""

        #rows
        for row in self.matrix:
            count = 0
            if row[0] != "-":
                current_player = row[0]
                for spot in row:
                    if spot == current_player:
                        count += 1

            if count == 3:
                self.winner = current_player
                self.win = True
                self.gameOver = True
                return True

        #columns
        for c in range(3):
            count = 0
            if self.matrix[0][c] != "-":
                current_player = self.matrix[0][c]
                for r in range(3):
                    if self.matrix[r][c]  == current_player:
                        count += 1

            if count == 3:
                self.winner = current_player
                self.win = True
                self.gameOver = True
                return True

        #diagnals

        current_player = self.matrix[0][0]
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != "-"):
            self.winner = current_player
            self.win = True
            self.gameOver = True
            return True

        current_player = self.matrix[0][2]
        if (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != "-"):
            self.winner = current_player
            self.win = True
            self.gameOver = True
            return True

    def findOpen(self):
        newOpen = []

        for r in range(3):
            for c in range(3):
                if self.matrix[r][c] ==  "-":
                    newOpen.append((r,c))

        self.openMoves = newOpen.copy()

    def reset(self):
        self.matrix = [["-" for i in range(3)] for j in range(3)]
        self.openMoves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.win = False
        self.winner = ""
        self.playerTurn = self.nextGamePlayerStart
        self.nextGamePlayerStart = not self.nextGamePlayerStart
        self.gameOver = False

        print("Player Wins: " + str(self.playerWins))
        print("Computer Wins: " + str(self.computerWins))


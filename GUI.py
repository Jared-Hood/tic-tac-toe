import tkinter as tk
from tkinter import messagebox
import AI
import time

class MainApplication(tk.Frame):
    def __init__(self,parent):
        self.parent = parent
        self.difficulty = tk.IntVar()
        self.win = False
        self.comp_wins = 0
        self.player_wins = 0
        self.p_turn = True
        self.last_p_turn = True #use to change who starts  first
        self.moves = [1,2,3,4,5,6,7,8,9] #Array of available moves in current game
        self.x_moves = []
        self.o_moves = []

        parent.title("Tic Tac Toe")
        self.difficulty.set(1)

        self.computer_AI = AI.AI()

        # Creating labels and adding to grid

        label_turn = tk.Label(parent, text="Turn", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        label_turn.grid(row=0, column=0)

        label_player = tk.Label(parent, text="Player", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        label_player.grid(row=0, column=1)

        label_score = tk.Label(parent, text="Score", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        label_score.grid(row=0, column=2)

        self.l_player_turn = tk.Label(parent, bg='green', height=1, width=1)
        self.l_player_turn.grid(row=1, column=0)

        self.l_comp_turn = tk.Label(parent, bg='white', height=1, width=1)
        self.l_comp_turn.grid(row=2, column=0)

        l_pname = tk.Label(parent, text="Player 1", font='Times 16', bg='white', fg='black', height=1, width=8)
        l_pname.grid(row=1, column=1)

        l_Cname = tk.Label(parent, text="Computer", font='Times 16', bg='white', fg='black', height=1, width=8)
        l_Cname.grid(row=2, column=1)

        self.l_Pscore = tk.Label(parent, text=str(self.player_wins), font='Times 16', bg='white', fg='black', height=1, width=8)
        self.l_Pscore.grid(row=1, column=2)

        self.l_Cscore = tk.Label(parent, text=str(self.comp_wins), font='Times 16', bg='white', fg='black', height=1, width=8)
        self.l_Cscore.grid(row=2, column=2)

        r_easy = tk.Radiobutton(parent, text="Easy", font='Times 16', bg='white', fg='green', height=1, width=10,
                             variable='difficulty', value=1, command=lambda: self.setDifficulty(r_easy))
        r_medium = tk.Radiobutton(parent, text="Medium  ", font='Times 16', bg='white', fg='orange', height=1, width=10,
                               variable='difficulty', value=2, command=lambda: self.setDifficulty(r_medium))
        r_hard = tk.Radiobutton(parent, text="Hard", font='Times 16', bg='white', fg='red', height=1, width=10,
                             variable='difficulty', value=3, command=lambda: self.setDifficulty(r_hard))
        r_easy.grid(row=0, column=3)
        r_medium.grid(row=1, column=3)
        r_hard.grid(row=2, column=3)

        self.button1 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button1))
        self.button2 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button2))
        self.button3 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button3))
        self.button4 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button4))
        self.button5 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button5))
        self.button6 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button6))
        self.button7 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button7))
        self.button8 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button8))
        self.button9 = tk.Button(parent, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command = lambda: self.buttonClick(self.button9))

        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.button4.grid(row=4, column=0)
        self.button5.grid(row=4, column=1)
        self.button6.grid(row=4, column=2)
        self.button7.grid(row=5, column=0)
        self.button8.grid(row=5, column=1)
        self.button9.grid(row=5, column=2)

    def setDifficulty(self,radio):
        self.difficulty.set(radio['value'])

    def buttonClick(self, button):
        button.config(state="disabled")

        if self.p_turn:
            button["text"] = "X"
        else:
            button["text"] = "O"

        if button == self.button1:
            self.moves.remove(1)
            if self.p_turn:
                self.x_moves.append(1)
            else:
                self.o_moves.append(1)
        elif button == self.button2:
            self.moves.remove(2)
            if self.p_turn:
                self.x_moves.append(2)
            else:
                self.o_moves.append(2)
        elif button == self.button3:
            self.moves.remove(3)
            if self.p_turn:
                self.x_moves.append(3)
            else:
                self.o_moves.append(3)
        elif button == self.button4:
            self.moves.remove(4)
            if self.p_turn:
                self.x_moves.append(4)
            else:
                self.o_moves.append(4)
        elif button == self.button5:
            self.moves.remove(5)
            if self.p_turn:
                self.x_moves.append(5)
            else:
                self.o_moves.append(5)
        elif button == self.button6:
            self.moves.remove(6)
            if self.p_turn:
                self.x_moves.append(6)
            else:
                self.o_moves.append(6)
        elif button == self.button7:
            self.moves.remove(7)
            if self.p_turn:
                self.x_moves.append(7)
            else:
                self.o_moves.append(7)
        elif button == self.button8:
            self.moves.remove(8)
            if self.p_turn:
                self.x_moves.append(8)
            else:
                self.o_moves.append(8)
        elif button == self.button9:
            self.moves.remove(9)
            if self.p_turn:
                self.x_moves.append(9)
            else:
                self.o_moves.append(9)

        self.p_turn = not self.p_turn
        self.configTurn()

        if self.checkWin():
            self.reset()

        if len(self.moves) == 0:
            self.comp_wins += 0.5
            self.player_wins +=  0.5
            self.reset()

        if not self.p_turn:
            self.computerMove()

    def checkWin(self):

        #check win for "X"
        if (
            #Rows
                self.button1["text"] == self.button2["text"] == self.button3["text"] == "X" or
                self.button4["text"] == self.button5["text"] == self.button6["text"] == "X" or
                self.button7["text"] == self.button8["text"] == self.button9["text"] == "X" or
            #Columns
                self.button1["text"] == self.button4["text"] == self.button7["text"] == "X" or
                self.button2["text"] == self.button5["text"] == self.button8["text"] == "X" or
                self.button3["text"] == self.button6["text"] == self.button9["text"] == "X" or
            #Diagnals
                self.button1["text"] == self.button5["text"] == self.button9["text"] == "X" or
                self.button3["text"] == self.button5["text"] == self.button7["text"] == "X"
        ):

            self.win = True
            self.player_wins += 1
            return True

        elif (
                self.button1["text"] == self.button2["text"] == self.button3["text"] == "O" or
                self.button4["text"] == self.button5["text"] == self.button6["text"] == "O" or
                self.button7["text"] == self.button8["text"] == self.button9["text"] == "O" or
            #Columns
                self.button1["text"] == self.button4["text"] == self.button7["text"] == "O" or
                self.button2["text"] == self.button5["text"] == self.button8["text"] == "O" or
                self.button3["text"] == self.button6["text"] == self.button9["text"] == "O" or
            #Diagnals
                self.button1["text"] == self.button5["text"] == self.button9["text"] == "O" or
                self.button3["text"] == self.button5["text"] == self.button7["text"] == "O"
        ):

            self.win = True
            self.comp_wins += 1
            return True

        else:
            return False

    def configTurn(self):
        if self.p_turn:
            self.l_player_turn.config(bg='green')
            self.l_comp_turn.config(bg='white')
        else:
            self.l_player_turn.config(bg='white')
            self.l_comp_turn.config(bg='green')

    def computerMove(self):
        dif = int(self.difficulty.get())
        comp_move = self.computer_AI.makeMove(dif,self.moves, self.x_moves, self.o_moves)
        self.buttonClick(eval("self.button" + str(comp_move)))

    def reset(self):
        self.button1.config(state = "normal", text=" ")
        self.button2.config(state = "normal", text=" ")
        self.button3.config(state = "normal", text=" ")
        self.button4.config(state = "normal", text=" ")
        self.button5.config(state = "normal", text=" ")
        self.button6.config(state = "normal", text=" ")
        self.button7.config(state = "normal", text=" ")
        self.button8.config(state = "normal", text=" ")
        self.button9.config(state = "normal", text=" ")

        self.l_Cscore.config(text=str(self.comp_wins))
        self.l_Pscore.config(text=str(self.player_wins))

        self.p_turn = not self.last_p_turn
        self.last_p_turn = not self.last_p_turn

        self.configTurn()
        self.moves = [1,2,3,4,5,6,7,8,9]
        self.x_moves = []
        self.o_moves = []
        self.win = False
import tkinter as root
from  tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")


difficulty = IntVar()
difficulty.set(1)

def setDifficulty(radio):
    difficulty.set(radio['value'])



#Creating labels and adding to grid

label_turn = Label( root, text="Turn", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label_turn.grid(row=0, column=0)

label_player = Label( root, text="Player", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label_player.grid(row=0, column=1)

label_score = Label( root, text="Score", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label_score.grid(row=0, column=2)

l_player_turn = Label(root, bg='green',height=1,width=1)
l_player_turn.grid(row=1,column=0)

l_comp_turn = Label(root,bg='white',height=1,width=1)
l_comp_turn.grid(row=2,column=0)

l_pname = Label(root,text="Player 1", font='Times 16', bg='white',fg='black',height=1,width=8)
l_pname.grid(row=1,column=1)

l_Cname = Label(root,text="Computer", font='Times 16', bg='white',fg='black',height=1,width=8)
l_Cname.grid(row=2,column=1)

l_Pscore = Label(root,text="0", font='Times 16', bg='white',fg='black',height=1,width=8)
l_Pscore.grid(row=1,column=2)

l_Cscore = Label(root,text="0", font ='Times 16', bg='white',fg='black',height=1,width=8)
l_Cscore.grid(row=2,column=2)

r_easy = Radiobutton(root, text="Easy", font='Times 16', bg='white',fg='green',height=1,width=10, variable='difficulty', value=1, command=lambda: setDifficulty(r_easy))
r_medium = Radiobutton(root, text="Medium  ", font='Times 16', bg='white',fg='orange',height=1,width=10, variable='difficulty',value=2,command=lambda: setDifficulty(r_medium))
r_hard = Radiobutton(root, text="Hard", font='Times 16', bg='white',fg='red',height=1,width=10, variable='difficulty', value=3,command= lambda: setDifficulty(r_hard))
r_easy.grid(row=0,column=3)
r_medium.grid(row=1,column=3)
r_hard.grid(row=2,column=3)

button1 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button2 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button3 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button4 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button5 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button6 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button7 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button8 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button9 = Button(root, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button7.grid(row=5,column=0)
button8.grid(row=5,column=1)
button9.grid(row=5,column=2)

root.mainloop()
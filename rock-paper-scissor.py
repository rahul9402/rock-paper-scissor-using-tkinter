
from tkinter import *
import tkinter.messagebox
import random

play = Tk()
play.geometry('700x500')
play.title('Rock-Paper-Scissor')
play.configure(bg='red')

global player_point, computer_point
choices = {1:'Rock',2:'Paper',3:'Scissor'}

def rock():
    global player_point, computer_point
    computer_choices = choices[random.randint(1,3)]

    l1.config(text='Rock')
    l2.config(text=computer_choices)

    if computer_choices == 'Rock':
        tkinter.messagebox.showinfo('Rock-Paper-Scissor','It\'s a Tie!..')
    elif computer_choices == 'Paper':
        computer_point += 1
        l4.config(text=computer_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Computer Wins!...')
    else:
        player_point += 1
        l3.config(text=player_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Player Wins!...')



def paper():
    global player_point, computer_point
    computer_choices = choices[random.randint(1, 3)]

    l1.config(text='Paper')
    l2.config(text=computer_choices)

    if computer_choices == 'Rock':
        player_point += 1
        l3.config(text=player_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Player Wins!...')
    elif computer_choices == 'Paper':
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'It\'s a Tie!..')
    else:
        computer_point += 1
        l4.config(text=computer_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Computer Wins!...')

def scissor():
    global player_point, computer_point
    computer_choices = choices[random.randint(1, 3)]

    l1.config(text='Scissor')
    l2.config(text=computer_choices)

    if computer_choices == 'Rock':
        computer_point += 1
        l4.config(text=computer_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Computer Wins!...')
    elif computer_choices == 'Paper':
        player_point += 1
        l3.config(text=player_point)
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'Player Wins!...')
    else:
        tkinter.messagebox.showinfo('Rock-Paper-Scissor', 'It\'s a Tie!..')


def reset():

    Label(play,text='Rock-Paper-Scissor',font=('calibri',15,'bold'),bg='lightblue',fg='red').place(x=270,y=20)

    value = Frame(play,width='660',height='100',bg='lightblue').place(x=20,y=70)

    Label(value,text='Player Selected',font=('calibri',15,'bold'),bg='red',fg='lightblue',
          width='25',height='1').place(x=30,y=90)
    Label(value,text='Computer Selected',font=('calibri',15,'bold'),bg='red',fg='lightblue',width='25',
          height='1').place(x=410,y=90)

    global l1,l2,l3,l4
    global player_point,computer_point

    l1 = Label(value,text='',font=('calibri',15,'bold'),fg='red',bg='lightblue')
    l1.place(x=100,y=140)
    l2 = Label(value,text='',font=('calibri',15,'bold'),fg='red',bg='lightblue')
    l2.place(x=490,y=140)

    Label(play,text='Choose Any One ...',font=('calibri',15,'bold'),bg='red',fg='lightblue').place(x=250,y=190)

    Button(play,text='Rock',font=('calibri',15,'bold'),bg='lightblue',fg='red',width='15',activebackground='red',
           activeforeground='lightblue',command=rock).place(x=30,y=250)
    Button(play,text='Paper',font=('calibri',15,'bold'),bg='lightblue',fg='red',width='15',activebackground='red',
           activeforeground='lightblue',command=paper).place(x=250,y=250)
    Button(play,text='Scissor',font=('calibri',15,'bold'),bg='lightblue',fg='red',width='15',activebackground='red',
           activeforeground='lightblue',command=scissor).place(x=500,y=250)

    Label(play, bg='lightblue', width='45', height='10').place(x=30,y=320)
    Label(play,text='Player Point',font=('calibri',15,'bold'),bg='red',fg='lightblue').place(x=50,y=350)
    Label(play,text='Computer Point',font=('calibri',15,'bold'),bg='red',fg='lightblue').place(x=180,y=350)

    player_point = 0
    computer_point = 0


    l3 = Label(play,text=player_point,font=('calibri',15,'bold'),fg='red',bg='lightblue')
    l3.place(x=90,y=400)
    l4 = Label(play,text=computer_point,font=('calibri',15,'bold'),fg='red',bg='lightblue')
    l4.place(x=240,y=400)

    Button(play,text='Reset',font=('calibri',15,'bold'),bg='lightblue',fg='red',activebackground='red',
           activeforeground='lightblue',command=reset).place(x=500,y=380)


reset()
play.mainloop()


from cProfile import label
from curses import BUTTON1_CLICKED
from pickle import FRAME
from tkinter import *
from tkinter.font import ITALIC
from turtle import right, width
honey_root = Tk()

# width x height
honey_root.geometry("650x500")

# width x height
honey_root.minsize(300,150)

# width x height
honey_root.maxsize(1500,1200)

# honey = Label(text="Honey is a good girl and is her first GUI")
# honey.pack()

honey_root.title("Welcome To Tic-Tac-Toe",)
title_label=Label(text=
                  '''Tic-Tac-Toe is a pencil and paper, two player game where, the two players, in turn mark the spaces in a 3x3 grid, 
                  with their respective symbols, O and X. The player who succeeds in getting three of his in a horizontal, vertical or diagonal row wins. 
                  If none of them gets three in a row, the game ends in a draw. 
                  Every turn the aim of the player is to either complete his “three” or prevent the other player from completing his “three''',bg="pink",fg="blue",padx=180,pady=20,font=("comicsansns",15,ITALIC),borderwidth=5,relief=RIDGE)
title_label.pack()
photo=PhotoImage(file="Tic_tac_toe.svg.png")
photo_honey_label=Label(image=photo)
photo_honey_label.pack()
photo_honey_label.pack(side=RIGHT,anchor=N)
# title_label.pack(side=)

f1 = Frame(honey_root,bg="grey",borderwidth=6,relief=SUNKEN,width=500,height=50)
f1.pack(side="left")
l = Label(f1,text="Game Tic-Tac-Toe")
l.pack()
# btn1 = StringVar()
# btn2 = StringVar()
# btn3 = StringVar()
# btn4 = StringVar()
# btn5 = StringVar()
# btn6 = StringVar()
# btn7 = StringVar()
# btn8 = StringVar()
# btn9 = StringVar()

# xPhoto = PhotoImage(file="index.png")
# oPhoto = PhotoImage(file="index(1).png")
# def play():
#     button1 = Button(honey_root,text="",height=6,width=10,bd=5,bg="pink",textvariable=btn1,command=lambda:press(1,0,0))
#     button2 = Button(honey_root,text="",height=6,width=10,bd=5,bg="pink",textvariable=btn2,command=lambda:press(2,0,1))
#     button3 = Button(honey_root,text="",height=6,width=10,bd=5,bg="pink",textvariable=btn3,command=lambda:press(3,0,2))
#     button4 = Button(honey_root,text="",height=6,width=10,bd=5,bg="skyblue",textvariable=btn4,command=lambda:press(4,1,0))
#     button5 = Button(honey_root,text="",height=6,width=10,bd=5,bg="skyblue",textvariable=btn5,command=lambda:press(5,1,1))
#     button6 = Button(honey_root,text="",height=6,width=10,bd=5,bg="skyblue",textvariable=btn6,command=lambda:press(6,1,2))
#     button7 = Button(honey_root,text="",height=6,width=10,bd=5,bg="grey",textvariable=btn7,command=lambda:press(7,2,0))
#     button8 = Button(honey_root,text="",height=6,width=10,bd=5,bg="grey",textvariable=btn8,command=lambda:press(8,2,1))
#     button9 = Button(honey_root,text="",height=6,width=10,bd=5,bg="grey",textvariable=btn9,command=lambda:press(9,2,2))

#     button1.grid(row=0,column=0)
#     button2.grid(row=0,column=1)
#     button3.grid(row=0,column=2)
#     button4.grid(row=1,column=0)
#     button5.grid(row=1,column=1)
#     button6.grid(row=1,column=2)
#     button7.grid(row=2,column=0)
#     button8.grid(row=2,column=1)
#     button9.grid(row=2,column=2)
                    
#                     #Checks for the winner        

#                 #  RESET BUTTON
#     reset_btn = Button(honey_root,text="",font=("times",26,"bold"),height=2,width=20,
#                                     bg="grey",command=None)
#     reset_btn.place(x=120,y=500)
#     def press(n,r,c):
#         global click,count
        
#         if click==True:
#             labelPhoto = Label(honey_root,image=xPhoto)
#             labelPhoto.grid(row=r,column=c)
#             if n==1:
#                 btn1.set("X")
#             elif n==2:
#                 btn2.set("X")
#             elif n==3:
#                 btn3.set("X")
#             elif n==4:
#                 btn4.set("X")
#             elif n==5:
#                 btn5.set("X")
#             elif n==6:
#                 btn6.set("X")
#             elif n==7:
#                 btn7.set("X")
#             elif n==8:
#                 btn8.set("X")
#             else:
#                 btn9.set("X")
#             count+=1
#             click=False
            
#         else:
#             labelPhoto = Label(honey_root,image=oPhoto)
#             labelPhoto.grid(row=r,column=c)

#             if n==1:
#                 btn1.set("O")
#             elif n==2:
#                 btn2.set("O")
#             elif n==3:
#                 btn3.set("O")
#             elif n==4:
#                 btn4.set("O")
#             elif n==5:
#                 btn5.set("O")
#             elif n==6:
#                 btn6.set("O")
#             elif n==7:
#                 btn7.set("O")
#             elif n==8:
#                 btn8.set("O")
#             else:
#                 btn9.set("O")
#             count+=1
#             click = True
            
                    


honey_root.mainloop()


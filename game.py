# from cProfile import label
# from inspect import classify_class_attrs
# from itertools import count
# from re import I, L
from tkinter import *
# from turtle import width
# import click
from PIL import Image,ImageTk
from tkinter import messagebox
    

honey_root=Tk()
# honey_root.iconbitmap(r'tic tac toe')
# honey_root.resizable(width=False,height=False)

import tkinter.messagebox

click=True

count=0

# honey_root.iconbitmap("")
honey_root.title("tic tac toe")

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

image = Image.open("index.png")
resize_image = image.resize((130,160))
img = ImageTk.PhotoImage(resize_image)

label1  = Label(image=img)
label1.image = img

image = Image.open("index(1).png")
resize_image1 = image.resize((130,160))
img1 = ImageTk.PhotoImage(resize_image1)

label  = Label(image=img1)
label.image = img1



def play():
    button1 = Button(honey_root,text="",height=9,width=13,bd=5,bg="pink",textvariable=btn1,command=lambda:press(1,0,0))
    button2 = Button(honey_root,text="",height=9,width=13,bd=5,bg="pink",textvariable=btn2,command=lambda:press(2,0,1))
    button3 = Button(honey_root,text="",height=9,width=13,bd=5,bg="pink",textvariable=btn3,command=lambda:press(3,0,2))
    button4 = Button(honey_root,text="",height=9,width=13,bd=5,bg="skyblue",textvariable=btn4,command=lambda:press(4,1,0))
    button5 = Button(honey_root,text="",height=9,width=13,bd=5,bg="skyblue",textvariable=btn5,command=lambda:press(5,1,1))
    button6 = Button(honey_root,text="",height=9,width=13,bd=5,bg="skyblue",textvariable=btn6,command=lambda:press(6,1,2))
    button7 = Button(honey_root,text="",height=9,width=13,bd=5,bg="grey",textvariable=btn7,command=lambda:press(7,2,0))
    button8 = Button(honey_root,text="",height=9,width=13,bd=5,bg="grey",textvariable=btn8,command=lambda:press(8,2,1))
    button9 = Button(honey_root,text="",height=9,width=13,bd=5,bg="grey",textvariable=btn9,command=lambda:press(9,2,2))

    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)
    
    def press(n,r,c):
        global click,count
        
        if click==True:
            label1 = Label(honey_root,image=img)
            label1 = Label(image=img)
            label1.image = img
            label1.grid(row=r,column=c)
            
            if n==1:
                btn1.set("X")
            if n==2:
                btn2.set("X")
            if n==3:
                btn3.set("X")
            if n==4:
                btn4.set("X")
            if n==5:
                btn5.set("X")
            if n==6:
                btn6.set("X")
            if n==7:
                btn7.set("X")
            if n==8:
                btn8.set("X")
            else:
                btn9.set("X")
            count+=1
            click=False
            checkwin()
            
        else:
            label = Label(honey_root,image=img1)
            label = Label(image=img1)
            label.image = img1
            label.grid(row=r,column=c)
            
            
            if n==1:
                btn1.set("O")
            elif n==2:
                btn2.set("O")
            if n==3:
                btn3.set("O")
            if n==4:
                btn4.set("O")
            if n==5:
                btn5.set("O")
            if n==6:
                btn6.set("O")
            if n==7:
                btn7.set("O")
            if n==8:
                btn8.set("O")
            else:
                btn9.set("O")
            count+=1
            click = True
            checkwin()
       


    def checkwin():
        global count,click
        if (btn1.get()=="X" and btn2.get()=="X" and btn3.get() == "X" or
            btn4.get()=="X" and btn5.get()=="X" and btn6.get() == "X" or
            btn7.get()=="X" and btn8.get()=="X" and btn9.get() == "X" or
            btn1.get()=="X" and btn4.get()=="X" and btn7.get() == "X" or
            btn2.get()=="X" and btn5.get()=="X" and btn8.get() == "X" or
            btn3.get()=="X" and btn6.get()=="X" and btn9.get() == "X" or
            btn1.get()=="X" and btn5.get()=="X" and btn9.get() == "X" or
            btn3.get()=="X" and btn5.get()=="X" and btn7.get() == "X" ):
            tkinter.messagebox.showinfo("Player Aarti wins!","Better luck next time honey")
            click==True
            count=0
            clear()
            play()
        elif(btn1.get()=="O" and btn2.get()=="O" and btn3.get() == "O" or
             btn4.get()=="O" and btn5.get()=="O" and btn6.get() == "O" or
             btn7.get()=="O" and btn8.get()=="O" and btn9.get() == "O" or
             btn1.get()=="O" and btn4.get()=="O" and btn7.get() == "O" or
             btn2.get()=="O" and btn5.get()=="O" and btn8.get() == "O" or
             btn3.get()=="O" and btn6.get()=="O" and btn9.get() == "O" or
             btn1.get()=="O" and btn5.get()=="O" and btn9.get() == "O" or
             btn3.get()=="O" and btn5.get()=="O" and btn7.get() == "O" ):
             tkinter.messagebox.showinfo("Player HONEY Win!","Better luck next time Aarti")
             click = True
             count=0
             clear()
             play()
        elif(count==9):
            tkinter.messagebox.showinfo("tic-Tac-Toe","game is tie")
            click=False
            count=0
            clear()  
            play()  
            
    def clear():
        btn1.set("")
        btn2.set("")
        btn3.set("")
        btn4.set("")
        btn5.set("")
        btn6.set("")
        btn7.set("")
        btn8.set("")
        btn9.set("")   
            
play()
    
honey_root.mainloop()


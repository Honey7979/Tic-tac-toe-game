from tkinter import*

root = Tk()
root.title("tic tac tae")
root.configure(bg="blue")
# root.geometry("535x600x200x100")

mainframe = Frame(root,height=450,width=600)
mainframe.place(x=0,y=0)

btn1 = Button(mainframe,text="",font=("times",26,"bold"),height=100,
              width=150,bg="pink",command=None)
btn1.grid(row=0,column=0)

btn2 = Button(mainframe,text="",font=("times",26,"bold"),height=100,
              width=150,bg="pink",command=None)
btn2.grid(row=0,column=0)

btn3 = Button(mainframe,text="",font=("times",26,"bold"),height=100,
              width=150,bg="pink",command=None)
btn3.grid(row=0,column=0)

btn4 = Button(mainframe,text="",font=("times",26,"bold"),height=100,
              width=150,bg="pink",command=None)
btn4.grid(row=0,column=0)

btn5 = Button(mainframe,text="",font=("times",26,"bold"),height=50,
              width=10,bg="pink",command=None)
btn5.grid(row=0,column=0)

btn6 = Button(mainframe,text="",font=("times",26,"bold"),height=50,
              width=10,bg="pink",command=None)
btn6.grid(row=0,column=0)

btn7 = Button(mainframe,text="",font=("times",26,"bold"),height=50,
              width=10,bg="pink",command=None)
btn7.grid(row=0,column=0)
btn8 = Button(mainframe,text="",font=("times",26,"bold"),height=50,
              width=10,bg="pink",command=None)
btn8.grid(row=0,column=0)
btn9 = Button(mainframe,text="",font=("times",26,"bold"),height=50,
              width=10,bg="pink",command=None)
btn9.grid(row=0,column=0)
root.mainloop()

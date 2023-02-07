from tkinter import *
# def ttt():
a=[[0,0,0],[0,0,1],[0,1,0]]
i=0
button=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[0][0]== a[0][1]==a[0][2]:
            print("winner1")
        elif a[1][0]==a[1][1]==a[1][2]:
            print("winner2")
        elif a[2][0]==a[2][1]==a[2][2]:
            print("winner3")
        else:
            print("looser")
        break
    while j<len(a[i]):
        if a[0][0]==a[1][0]==a[2][0]:
            print("winner4")
        elif a[0][1]==a[1][1]==a[2][1]:
            print("winner5")
        elif a[0][2]==a[1][2]==a[2][2]:
            print("winner6")
        else:
            print("looser")
        break
    while i==j:
        if a[0][0]==a[1][1]==a[2][2]:
            print("winner7")
        elif a[0][2]==a[1][1]==a[2][0]:
            print("winner8")
        else:
            print("looser")
        j+=1
    break
    i+=1
        
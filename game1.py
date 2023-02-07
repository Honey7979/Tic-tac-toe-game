from ctypes import resize
from tkinter import*
from PIL import Image,ImageTk

root  = Tk()
image = Image.open("index.png")
resize_image = image.resize((40,60))
img = ImageTk.PhotoImage(resize_image)

label1  = Label(image=img)
label1.image = img
label1.pack()
root.mainloop()
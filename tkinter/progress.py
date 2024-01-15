from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame or window
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x250")
def callback():
   Label(win, text="This is Andrew Osula", font=('Georgia 20 bold')).pack(pady=4)

#Create a Label and a Button widget
btn = ttk.Button(win, text="Press Enter to Show a Message", command= callback)
btn.pack(ipadx=10)

win.bind('<Return>',lambda event:callback())

win.mainloop()
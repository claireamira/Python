from tkinter import *
from datetime import datetime

root = Tk()

root.title("my first GUI")

root.geometry('1000x1000')

root.config(bg= "steelblue")

label = Label(root, text= "Welcome", bg = "steelblue", fg= "white", font= ("Arial Black", 58, "bold"))

label.pack(pady= 50)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.config(text=time)
    label.after(1000, clock)

clock()    

root.mainloop()


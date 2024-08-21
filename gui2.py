from tkinter import *

root= Tk()

root.title("BUTTONS")

root.geometry('1000x1000')

root.config(bg= "steelblue")

welcome_label = Label(root, text="Buttons", bg= "lightblue", fg="white", font=("Arial Black", 50, "bold"))
welcome_label.pack(pady=30)

def onClick(userText):
    welcome_label.config(text = userText, bg="purple")

def onClick2():
    root.config(bg="white")

my_button = Button(root, text="click me", bg="blue", fg="red", width=10, height=2, command=lambda:onClick("Hello"))
my_button.pack()

button2 = Button(root, text="Button 2", bg="lightgreen", fg="purple", width=7, height=1, command=onClick2)
button2.pack()

root.mainloop() 
from tkinter import *

root = Tk()

root.title("USER MANAGEMENT")

root.geometry("800x500")

welcome_label = Label(root, text="welcome!", fg="Black", font=("Helvetica", 45, "bold"))
welcome_label.grid(row=0, column=0, pady=45, padx=20, columnspan=2)

def register():
    register_window = Tk()
    register_window.title("Register")
    register_window.geometry('800x800')

    register_label = Label(register_window, text="REGISTER", font=("Helvetica", 40, "bold"), fg='black')
    register_label.grid(row=0, column=0, pady=20, padx=20)

    username_label =Label(register_window, text="Username: ", font=("Helvetica", 20), fg="black")
    username_label.grid(column=0, row=1, padx=20, pady=20)

    username_entry = Entry(register_window, width=25, font=("Helvetica", 20), fg="black")
    username_entry.grid(column=1, row=1)

    password_label =Label(register_window, text="Password: ", font=("Helvetica", 20), fg="black")
    password_label.grid(column=0, row=2, padx=20, pady=20)

    password_entry = Entry(register_window, width=25, font=("Helvetica", 20), fg="black")
    password_entry.grid(column=1, row=2)

    root.destroy()

    register_window.mainloop()



login_button = Button(root, text="LOGIN")
login_button.grid(row=1, column=0)

register_button = Button(root, text="REGISTER")
register_button.grid(row=1, column=1)

root.mainloop()


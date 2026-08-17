from tkinter import *
from tkinter import messagebox
from database import connect_db
import os



root = Tk()

print("LOGIN PAGE OPENED")



root.title("Student Management System")
root.state("zoomed")
root.configure(bg="#ECF0F1")
root.resizable(True, True)

title = Label(
    root,
    text="Student Management System",
    font=("Arial", 22, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack(pady=20)

frame = Frame(root, bg="white", padx=30, pady=30)
frame.pack(pady=20)

Label(frame, text="Username", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky="w", pady=10)
username = Entry(frame, width=30, font=("Arial", 12))
username.grid(row=0, column=1)

Label(frame, text="Password", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w", pady=10)
password = Entry(frame, width=30, font=("Arial", 12), show="*")
password.grid(row=1, column=1)
def login():

    conn = connect_db()
    cursor = conn.cursor()


    sql = "SELECT * FROM users WHERE username=%s AND password=%s"

    values = (
        username.get(),
        password.get()
    )

    cursor.execute(sql, values)

    row = cursor.fetchone()

    if row:
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        os.system("python dashboard.py")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

    cursor.close()
    conn.close()
def open_register():
    root.destroy()
    os.system("python register.py")   
def toggle_password():
    if password.cget("show") == "*":
        password.config(show="")
    else:
        password.config(show="*")

Checkbutton(
    frame,
    text="Show Password",
    command=toggle_password,
    bg="white"
).grid(row=2, column=1, sticky="w")

Button(
    frame,
    text="Login",
    bg="#3498DB",
    fg="white",
    width=15,
    font=("Arial", 11, "bold"),
    command=login
).grid(row=3, column=0, pady=20)
Button(
    frame,
    text="Register",
    bg="#27AE60",
    fg="white",
    width=15,
    font=("Arial",11,"bold"),
    command=open_register
).grid(row=4,column=0,pady=10)
Button(
    frame,
    text="Exit",
    bg="red",
    fg="white",
    width=15,
    font=("Arial", 11, "bold"),
    command=root.destroy
).grid(row=4, column=1,pady=10)

root.mainloop()
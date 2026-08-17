from tkinter import *
from tkinter import messagebox
from database import connect_db

root = Tk()

root.title("Register")
root.geometry("450x600")
root.configure(bg="white")
root.resizable(False, False)
def register_user():

    if username.get() == "" or password.get() == "" or confirm_password.get() == "":
        messagebox.showerror("Error", "All fields are required")
        return

    if password.get() != confirm_password.get():
        messagebox.showerror("Error", "Passwords do not match")
        return

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
INSERT INTO users(username, email, phone, password)
VALUES(%s, %s, %s, %s)
"""

    values = (
    username.get(),
    email.get(),
    phone.get(),
    password.get()
)

    try:
        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo("Success", "Registration Successful")

        username.delete(0, END)
        email.delete(0, END)
        phone.delete(0, END)
        password.delete(0, END)
        confirm_password.delete(0, END)

    except:
        messagebox.showerror("Error", "Username already exists")

    cursor.close()
    conn.close()

# ================= Title =================

title = Label(
    root,
    text="REGISTER",
    font=("Arial",20,"bold"),
    bg="white",
    fg="blue"
)



title.pack(pady=20)

# Username
Label(root, text="Username", font=("Arial",12), bg="white").pack()
username = Entry(root, font=("Arial",12), width=30)
username.pack(pady=5)

# Email
Label(root, text="Email", font=("Arial",12), bg="white").pack()
email = Entry(root, font=("Arial",12), width=30)
email.pack(pady=5)

# Phone Number
Label(root, text="Phone Number", font=("Arial",12), bg="white").pack()
phone = Entry(root, font=("Arial",12), width=30)
phone.pack(pady=5)

# Password
Label(root, text="Password", font=("Arial",12), bg="white").pack()
password = Entry(root, font=("Arial",12), show="*", width=30)
password.pack(pady=5)

# Confirm Password
Label(root, text="Confirm Password", font=("Arial",12), bg="white").pack()
confirm_password = Entry(root, font=("Arial",12), show="*", width=30)
confirm_password.pack(pady=10)
Button(
    root,
    text="Register",
    font=("Arial",12,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    command=register_user
).pack(pady=20)

root.mainloop()
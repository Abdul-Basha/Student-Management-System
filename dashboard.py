import os
from tkinter import *

# ================= Window =================

root = Tk()

root.title("Student Management System")
root.geometry("1000x600")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

# ================= Functions =================

def open_student():
    root.destroy()
    os.system("python student.py")
def logout():
    root.destroy()
    os.system("python login.py")
def open_marks():
    root.destroy()
    os.system("python marks.py")
def logout():
    root.destroy()
    os.system("python login.py")


def open_course():
    root.destroy()
    os.system("python course.py")
def logout():
    root.destroy()
    os.system("python login.py")
def open_trainer():
    root.destroy()
    os.system("python trainer.py")
def logout():
    root.destroy()
    os.system("python login.py")


# ================= HEADER =================

header = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial",24,"bold"),
    bg="#2C3E50",
    fg="white",
    pady=15
)

header.pack(fill=X)

# ================= WELCOME =================

welcome = Label(
    root,
    text="Welcome Admin",
    font=("Arial",18,"bold"),
    bg="#ecf0f1",
    fg="#2C3E50"
)

welcome.pack(pady=25)

# ================= BUTTON FRAME =================

button_frame = Frame(root, bg="#ecf0f1")
button_frame.pack(pady=30)

# ================= Students =================

student_btn = Button(
    button_frame,
    text="Students",
    font=("Arial",16,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    height=2,
    command=open_student
)

student_btn.grid(row=0, column=0, padx=20, pady=20)

# ================= Courses =================

course_btn = Button(
    button_frame,
    text="Courses",
    font=("Arial",16,"bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    height=2,
    command=open_course
)

course_btn.grid(row=0, column=1, padx=20, pady=20)

# ================= Trainers =================

trainer_btn = Button(
    button_frame,
    text="Trainers",
    font=("Arial",16,"bold"),
    bg="#F39C12",
    fg="white",
    width=15,
    height=2,
    command=open_trainer
)

trainer_btn.grid(row=1, column=0, padx=20, pady=20)

# ================= Marks =================

marks_btn = Button(
    button_frame,
    text="Marks",
    font=("Arial",16,"bold"),
    bg="#8E44AD",
    fg="white",
    width=15,
    height=2,
    command=open_marks
)

marks_btn.grid(row=1, column=1, padx=20, pady=20)

# ================= Logout =================

logout_btn = Button(
    root,
    text="Logout",
    font=("Arial",14,"bold"),
    bg="red",
    fg="white",
    width=15,
    command=logout
)

logout_btn.pack(pady=20)

root.mainloop()
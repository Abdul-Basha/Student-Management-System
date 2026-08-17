from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import connect_db

# ================= Window =================
root = Tk()
root.title("Student Management System")
root.geometry("900x600")
root.configure(bg="#ECF0F1")
root.resizable(False, False)

# ================= Functions =================

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    student_table.delete(*student_table.get_children())

    for row in rows:
        student_table.insert("", END, values=row)

    cursor.close()
    conn.close()


def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO student(studentid, sname, email_id)
    VALUES(%s,%s,%s)
    """

    values = (
        student_id.get(),
        student_name.get(),
        email.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Student Added Successfully")

    cursor.close()
    conn.close()

    view_students()


def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE student
    SET sname=%s,
        email_id=%s
    WHERE studentid=%s
    """

    values = (
        student_name.get(),
        email.get(),
        student_id.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Student Updated Successfully")

    cursor.close()
    conn.close()

    view_students()
def delete_student():

    conn = connect_db()
    cursor = conn.cursor()

    sql = "DELETE FROM student WHERE studentid=%s"

    values = (student_id.get(),)

    cursor.execute(sql, values)

    conn.commit()

    messagebox.showinfo("Success", "Student Deleted Successfully")

    cursor.close()
    conn.close()

    view_students()
def clear_fields():

    student_id.delete(0, END)
    student_name.delete(0, END)
    email.delete(0, END)

    student_id.focus()
    


# ================= Title =================

title = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#2C3E50",
    fg="white",
    pady=10
)
title.pack(fill=X)

# ================= Form =================

form = Frame(root, bg="white", bd=2, relief=RIDGE)
form.pack(pady=20, padx=20, fill=X)

Label(form, text="Student ID", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
student_id = Entry(form, font=("Arial", 12), width=30)
student_id.grid(row=0, column=1, padx=10)

Label(form, text="Student Name", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
student_name = Entry(form, font=("Arial", 12), width=30)
student_name.grid(row=1, column=1)

Label(form, text="Email ID", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
email = Entry(form, font=("Arial", 12), width=30)
email.grid(row=2, column=1)

# ================= Buttons =================

button_frame = Frame(root, bg="#ECF0F1")
button_frame.pack(pady=20)

add_btn = Button(
    button_frame,
    text="Add Student",
    font=("Arial",12,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    command=add_student
)
add_btn.grid(row=0, column=0, padx=10, pady=10)

update_btn = Button(
    button_frame,
    text="Update Student",
    font=("Arial",12,"bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    command=update_student
)
update_btn.grid(row=0, column=1, padx=10, pady=10)

delete_btn = Button(
    button_frame,
    text="Delete Student",
    font=("Arial",12,"bold"),
    bg="#E74C3C",
    fg="white",
    width=15,
    command=delete_student
)
delete_btn.grid(row=1, column=0, padx=10, pady=10)

clear_btn = Button(
    button_frame,
    text="Clear",
    font=("Arial",12,"bold"),
    bg="#F39C12",
    fg="white",
    width=15,
    command=clear_fields
)
def get_cursor(event):

    selected_row = student_table.focus()

    data = student_table.item(selected_row)

    row = data["values"]

    if row:

        student_id.delete(0, END)
        student_name.delete(0, END)
        email.delete(0, END)

        student_id.insert(0, row[0])
        student_name.insert(0, row[1])
        email.insert(0, row[2])
clear_btn.grid(row=1, column=1, padx=10, pady=10)

view_btn = Button(
    root,
    text="View Students",
    font=("Arial",12,"bold"),
    bg="#8E44AD",
    fg="white",
    width=20,
    command=view_students
)
view_btn.pack(pady=10)

# ================= Student Table =================

student_table = ttk.Treeview(
    root,
    columns=("ID", "Name", "Email"),
    show="headings",
    height=8
)

student_table.heading("ID", text="Student ID")
student_table.heading("Name", text="Student Name")
student_table.heading("Email", text="Email ID")

student_table.column("ID", width=100)
student_table.column("Name", width=200)
student_table.column("Email", width=300)

student_table.pack(pady=20)
student_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
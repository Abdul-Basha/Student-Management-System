from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

# ================= Window =================

root = Tk()
root.title("Course Management System")
root.geometry("900x650")
root.configure(bg="#ECF0F1")
root.resizable(False, False)

# ================= Functions =================

def view_courses():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()

    course_table.delete(*course_table.get_children())

    for row in rows:
        course_table.insert("", END, values=row)

    cursor.close()
    conn.close()


def add_course():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO course(courseid,cname,duration,fees)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        course_id.get(),
        course_name.get(),
        duration.get(),
        fees.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Course Added Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_courses()


def update_course():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE course
    SET cname=%s,
        duration=%s,
        fees=%s
    WHERE courseid=%s
    """

    values = (
        course_name.get(),
        duration.get(),
        fees.get(),
        course_id.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Course Updated Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_courses()


def delete_course():

    conn = connect_db()
    cursor = conn.cursor()

    sql = "DELETE FROM course WHERE courseid=%s"

    values = (course_id.get(),)

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Course Deleted Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_courses()


def clear_fields():

    course_id.delete(0, END)
    course_name.delete(0, END)
    duration.delete(0, END)
    fees.delete(0, END)

    course_id.focus()


def get_cursor(event):

    selected = course_table.focus()

    data = course_table.item(selected)

    row = data["values"]

    if row:

        clear_fields()

        course_id.insert(0, row[0])
        course_name.insert(0, row[1])
        duration.insert(0, row[2])
        fees.insert(0, row[3])

# ================= Title =================

title = Label(
    root,
    text="COURSE MANAGEMENT SYSTEM",
    font=("Arial",22,"bold"),
    bg="#2C3E50",
    fg="white",
    pady=10
)

title.pack(fill=X)

# ================= Form =================

form = Frame(root,bg="white",bd=2,relief=RIDGE)
form.pack(pady=20,padx=20,fill=X)

Label(form,text="Course ID",font=("Arial",12),bg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
course_id = Entry(form,font=("Arial",12),width=30)
course_id.grid(row=0,column=1)

Label(form,text="Course Name",font=("Arial",12),bg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
course_name = Entry(form,font=("Arial",12),width=30)
course_name.grid(row=1,column=1)

Label(form,text="Duration",font=("Arial",12),bg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
duration = Entry(form,font=("Arial",12),width=30)
duration.grid(row=2,column=1)

Label(form,text="Fees",font=("Arial",12),bg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
fees = Entry(form,font=("Arial",12),width=30)
fees.grid(row=3,column=1)

# ================= Buttons =================

button_frame = Frame(root,bg="#ECF0F1")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Add Course",
    font=("Arial",12,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    command=add_course
).grid(row=0,column=0,padx=10,pady=10)

Button(
    button_frame,
    text="Update Course",
    font=("Arial",12,"bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    command=update_course
).grid(row=0,column=1,padx=10,pady=10)

Button(
    button_frame,
    text="Delete Course",
    font=("Arial",12,"bold"),
    bg="#E74C3C",
    fg="white",
    width=15,
    command=delete_course
).grid(row=1,column=0,padx=10,pady=10)

Button(
    button_frame,
    text="Clear",
    font=("Arial",12,"bold"),
    bg="#F39C12",
    fg="white",
    width=15,
    command=clear_fields
).grid(row=1,column=1,padx=10,pady=10)

Button(
    root,
    text="View Courses",
    font=("Arial",12,"bold"),
    bg="#8E44AD",
    fg="white",
    width=20,
    command=view_courses
).pack(pady=10)

# ================= Table =================

course_table = ttk.Treeview(
    root,
    columns=("ID","Name","Duration","Fees"),
    show="headings",
    height=8
)

course_table.heading("ID",text="Course ID")
course_table.heading("Name",text="Course Name")
course_table.heading("Duration",text="Duration")
course_table.heading("Fees",text="Fees")

course_table.column("ID",width=100)
course_table.column("Name",width=220)
course_table.column("Duration",width=150)
course_table.column("Fees",width=120)

course_table.pack(pady=20)

course_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

# ================= Window =================

root = Tk()
root.title("Marks Management System")
root.geometry("900x650")
root.configure(bg="#ECF0F1")
root.resizable(False, False)
# ================= Functions =================

def view_marks():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM marks")

    rows = cursor.fetchall()

    marks_table.delete(*marks_table.get_children())

    for row in rows:
        marks_table.insert("", END, values=row)

    cursor.close()
    conn.close()


def add_marks():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO marks(marks_id, studentid, course_id, marks_obtained)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        marks_id.get(),
        student_id.get(),
        course_id.get(),
        marks.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Marks Added Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_marks()


def update_marks():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE marks
    SET studentid=%s,
        course_id=%s,
        marks_obtained=%s
    WHERE marks_id=%s
    """

    values = (
        student_id.get(),
        course_id.get(),
        marks.get(),
        marks_id.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Marks Updated Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_marks()


def delete_marks():

    if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):

        conn = connect_db()
        cursor = conn.cursor()

        sql = "DELETE FROM marks WHERE marks_id=%s"

        values = (marks_id.get(),)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo("Success", "Marks Deleted Successfully")

        cursor.close()
        conn.close()

        clear_fields()
        view_marks()
def clear_fields():

    marks_id.delete(0, END)
    student_id.delete(0, END)
    course_id.delete(0, END)
    marks.delete(0, END)

    marks_id.focus()

def get_cursor(event):

    selected = marks_table.focus()

    data = marks_table.item(selected)

    row = data["values"]

    if row:

        clear_fields()

        marks_id.insert(0, row[0])
        student_id.insert(0, row[1])
        course_id.insert(0, row[2])
        marks.insert(0, row[3])
# ================= Title =================

title = Label(
    root,
    text="MARKS MANAGEMENT SYSTEM",
    font=("Arial",22,"bold"),
    bg="#2C3E50",
    fg="white",
    pady=10
)

title.pack(fill=X)
# ================= Form =================

form = Frame(root, bg="white", bd=2, relief=RIDGE)
form.pack(pady=20, padx=20, fill=X)

Label(form, text="Marks ID", font=("Arial",12), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
marks_id = Entry(form, font=("Arial",12), width=30)
marks_id.grid(row=0, column=1)

Label(form, text="Student ID", font=("Arial",12), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
student_id = Entry(form, font=("Arial",12), width=30)
student_id.grid(row=1, column=1)

Label(form, text="Course ID", font=("Arial",12), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
course_id = Entry(form, font=("Arial",12), width=30)
course_id.grid(row=2, column=1)

Label(form, text="Marks Obtained", font=("Arial",12), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
marks = Entry(form, font=("Arial",12), width=30)
marks.grid(row=3, column=1)

# ================= Buttons =================

button_frame = Frame(root, bg="#ECF0F1")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Add Marks",
    font=("Arial",12,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    command=add_marks
).grid(row=0, column=0, padx=10, pady=10)

Button(
    button_frame,
    text="Update Marks",
    font=("Arial",12,"bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    command=update_marks
).grid(row=0, column=1, padx=10, pady=10)

Button(
    button_frame,
    text="Delete Marks",
    font=("Arial",12,"bold"),
    bg="#E74C3C",
    fg="white",
    width=15,
    command=delete_marks
).grid(row=1, column=0, padx=10, pady=10)

Button(
    button_frame,
    text="Clear",
    font=("Arial",12,"bold"),
    bg="#F39C12",
    fg="white",
    width=15,
    command=clear_fields
).grid(row=1, column=1, padx=10, pady=10)

Button(
    root,
    text="View Marks",
    font=("Arial",12,"bold"),
    bg="#8E44AD",
    fg="white",
    width=20,
    command=view_marks
).pack(pady=10)

# ================= Marks Table =================

marks_table = ttk.Treeview(
    root,
    columns=("Marks ID", "Student ID", "Course ID", "Marks"),
    show="headings",
    height=8
)

marks_table.heading("Marks ID", text="Marks ID")
marks_table.heading("Student ID", text="Student ID")
marks_table.heading("Course ID", text="Course ID")
marks_table.heading("Marks", text="Marks Obtained")

marks_table.column("Marks ID", width=120)
marks_table.column("Student ID", width=120)
marks_table.column("Course ID", width=120)
marks_table.column("Marks", width=150)

marks_table.pack(pady=20)

marks_table.bind("<ButtonRelease-1>", get_cursor)
root.mainloop()
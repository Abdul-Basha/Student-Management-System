from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

# ================= Window =================

root = Tk()
root.title("Trainer Management System")
root.geometry("900x650")
root.configure(bg="#ECF0F1")
root.resizable(False, False)

# ================= Functions =================

def view_trainers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trainer")
    rows = cursor.fetchall()

    trainer_table.delete(*trainer_table.get_children())

    for row in rows:
        trainer_table.insert("", END, values=row)

    cursor.close()
    conn.close()


def add_trainer():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO trainer(trainer_id, trainername, expert)
    VALUES(%s,%s,%s)
    """

    values = (
        trainer_id.get(),
        trainer_name.get(),
        expert.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Trainer Added Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_trainers()


def update_trainer():

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE trainer
    SET trainername=%s,
        expert=%s
    WHERE trainer_id=%s
    """

    values = (
        trainer_name.get(),
        expert.get(),
        trainer_id.get()
    )

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Trainer Updated Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_trainers()


def delete_trainer():

    conn = connect_db()
    cursor = conn.cursor()

    sql = "DELETE FROM trainer WHERE trainer_id=%s"

    values = (trainer_id.get(),)

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Trainer Deleted Successfully")

    cursor.close()
    conn.close()

    clear_fields()
    view_trainers()


def clear_fields():

    trainer_id.delete(0, END)
    trainer_name.delete(0, END)
    expert.delete(0, END)

    trainer_id.focus()


def get_cursor(event):

    selected = trainer_table.focus()

    data = trainer_table.item(selected)

    row = data["values"]

    if row:

        clear_fields()

        trainer_id.insert(0, row[0])
        trainer_name.insert(0, row[1])
        expert.insert(0, row[2])

# ================= Title =================

title = Label(
    root,
    text="TRAINER MANAGEMENT SYSTEM",
    font=("Arial",22,"bold"),
    bg="#2C3E50",
    fg="white",
    pady=10
)

title.pack(fill=X)

# ================= Form =================

form = Frame(root,bg="white",bd=2,relief=RIDGE)
form.pack(pady=20,padx=20,fill=X)

Label(form,text="Trainer ID",font=("Arial",12),bg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
trainer_id = Entry(form,font=("Arial",12),width=30)
trainer_id.grid(row=0,column=1)

Label(form,text="Trainer Name",font=("Arial",12),bg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
trainer_name = Entry(form,font=("Arial",12),width=30)
trainer_name.grid(row=1,column=1)

Label(form,text="Expert",font=("Arial",12),bg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
expert = Entry(form,font=("Arial",12),width=30)
expert.grid(row=2,column=1)

# ================= Buttons =================

button_frame = Frame(root,bg="#ECF0F1")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Add Trainer",
    font=("Arial",12,"bold"),
    bg="#3498DB",
    fg="white",
    width=15,
    command=add_trainer
).grid(row=0,column=0,padx=10,pady=10)

Button(
    button_frame,
    text="Update Trainer",
    font=("Arial",12,"bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    command=update_trainer
).grid(row=0,column=1,padx=10,pady=10)

Button(
    button_frame,
    text="Delete Trainer",
    font=("Arial",12,"bold"),
    bg="#E74C3C",
    fg="white",
    width=15,
    command=delete_trainer
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
    text="View Trainers",
    font=("Arial",12,"bold"),
    bg="#8E44AD",
    fg="white",
    width=20,
    command=view_trainers
).pack(pady=10)

# ================= Table =================

trainer_table = ttk.Treeview(
    root,
    columns=("ID","Name","Expert"),
    show="headings",
    height=8
)

trainer_table.heading("ID",text="Trainer ID")
trainer_table.heading("Name",text="Trainer Name")
trainer_table.heading("Expert",text="Expert")

trainer_table.column("ID",width=150)
trainer_table.column("Name",width=250)
trainer_table.column("Expert",width=250)

trainer_table.pack(pady=20)

trainer_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
import tkinter as tk
from tkinter import messagebox, simpledialog
from db_config import get_db_connection
from mysql.connector import Error


# Backend Functions (Unchanged)
def add_student(name, age, gender, course, email):
    connection = get_db_connection()
    if connection is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO students (name, age, gender, course, email) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, gender, course, email))
        connection.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_student(student_id):
    connection = get_db_connection()
    if connection is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        connection.commit()
        messagebox.showinfo("Success", "Student deleted successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def update_student(student_id, name, age, gender, course, email):
    connection = get_db_connection()
    if connection is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE students SET name = %s, age = %s, gender = %s, course = %s, email = %s WHERE id = %s",
                       (name, age, gender, course, email, student_id))
        connection.commit()
        messagebox.showinfo("Success", "Student updated successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
        

def view_students():
    connection = get_db_connection()
    if connection is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        student_list = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Course: {row[4]}, Email: {row[5]}" for row in rows])
        messagebox.showinfo("Student List", student_list if student_list else "No students found.")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# GUI Functions 
def add_student_gui():
    name = simpledialog.askstring("Input", "Enter student name:")
    age = simpledialog.askinteger("Input", "Enter student age:")
    gender = simpledialog.askstring("Input", "Enter gender (Male/Female/Other):")
    course = simpledialog.askstring("Input", "Enter course:")
    email = simpledialog.askstring("Input", "Enter email:")
    if name and age and gender and course and email:
        add_student(name, age, gender, course, email)

def delete_student_gui():
    student_id = simpledialog.askinteger("Input", "Enter student ID to delete:")
    if student_id:
        delete_student(student_id)

def update_student_gui():
    student_id = simpledialog.askinteger("Input", "Enter student ID to update:")
    if student_id:
        name = simpledialog.askstring("Input", "Enter new student name:")
        age = simpledialog.askinteger("Input", "Enter new student age:")
        gender = simpledialog.askstring("Input", "Enter new gender (Male/Female/Other):")
        course = simpledialog.askstring("Input", "Enter new course:")
        email = simpledialog.askstring("Input", "Enter new email:")
        if name and age and gender and course and email:
            update_student(student_id, name, age, gender, course, email)

def view_students_gui():
    view_students()

# Main Application
def main():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")  # Set background color

    title_label = tk.Label(root, text="Student Management System", font=("Arial", 16), bg="#f0f0f0", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    btn_add = tk.Button(root, text="Add Student", command=add_student_gui, width=20, bg="#4CAF50", fg="white")
    btn_add.grid(row=1, column=0, padx=10, pady=10)

    btn_delete = tk.Button(root, text="Delete Student", command=delete_student_gui, width=20, bg="#f44336", fg="white")
    btn_delete.grid(row=1, column=1, padx=10, pady=10)

    btn_update = tk.Button(root, text="Update Student", command=update_student_gui, width=20, bg="#2196F3", fg="white")
    btn_update.grid(row=2, column=0, padx=10, pady=10)

    btn_view = tk.Button(root, text="View Students", command=view_students_gui, width=20, bg="#FF9800", fg="white")
    btn_view.grid(row=2, column=1, padx=10, pady=10)

    btn_exit = tk.Button(root, text="Exit", command=root.quit, width=20, bg="#9E9E9E", fg="white")
    btn_exit.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()

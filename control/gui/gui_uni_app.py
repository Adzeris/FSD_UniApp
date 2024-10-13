# main.py
import tkinter as tk
from tkinter import messagebox

from control.gui.student_control import show_operation_menu
from service.student_service import StudentService
from service.subject_service import SubjectService

student_service = StudentService()
subject_service = SubjectService()


def set_login_session(student):
    student_service.set_student(student)
    subject_service.set_student(student)


def clear_login_session():
    student_service.set_student(None)
    subject_service.set_student(None)


def login():
    email = email_entry.get()
    password = password_entry.get()

    try:
        if student_service.check_register_params(email, password):
            student = student_service.login(email, password)
            if student:
                set_login_session(student)
                # 传递 root 和 student_service
                show_operation_menu(root, student_service, subject_service)  # 显示操作菜单
        else:
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            messagebox.showerror("Error", "Incorrect email and password format.")

    except Exception as e:
        messagebox.showerror("Login fail!", str(e))


# create main window
root = tk.Tk()
root.title("Login")

# Set window size (width x height)
window_width = 600
window_height = 450

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the center of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window geometry (width x height + x_offset + y_offset)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# create labels and entries
email_label = tk.Label(root, text="Email:")
email_label.pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Sign In", command=login)
login_button.pack(pady=20)

# run main loop
root.mainloop()

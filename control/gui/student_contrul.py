# student_contrul.py
import tkinter as tk
from tkinter import messagebox

from util import validation
from util.constant import Constant
from util.validation import Validation


def show_operation_menu(root, student_service, subject_service):
    root.title("Welcome")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Welcome! Student Course Menu").pack(pady=(10, 5))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)  # 在框架和顶部留出一些空间

    button1 = tk.Button(button_frame, text="Change Password",
                        command=lambda: show_change_password_menu(root, student_service, subject_service))
    button1.pack(side=tk.LEFT, padx=5)

    button2 = tk.Button(button_frame, text="Enroll Subject", command=lambda: enroll_subject(root, subject_service))
    button2.pack(side=tk.LEFT, padx=5)

    button3 = tk.Button(button_frame, text="Remove Subject",
                        command=lambda: show_remove_subject_page(root, student_service, subject_service))
    button3.pack(side=tk.LEFT, padx=5)

    button4 = tk.Button(button_frame, text="Show Subjects",
                        command=lambda: show_subjects(root, student_service, subject_service))
    button4.pack(side=tk.LEFT, padx=5)


def show_subjects(root, student_service, subject_service):
    try:
        lists = subject_service.query_subjects()

        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Subjects List").pack(pady=(10, 5))

        subjects_text = tk.Text(root, width=50, height=15)
        subjects_text.pack(pady=(5, 5))

        if lists:
            for subject in lists:
                subjects_text.insert(tk.END, subject)
                subjects_text.insert(tk.END, "\n")

        else:
            subjects_text.insert(tk.END, "No subjects available.")

        back_button = tk.Button(root, text="Back to Menu",
                                command=lambda: show_operation_menu(root, student_service, subject_service))
        back_button.pack(pady=(5, 5))

    except Exception as e:
        messagebox.showerror("Error", str(e))


def enroll_subject(root, subject_service):
    # This function is called when the "Enroll Subject" button is clicked
    try:
        # Replace this with the actual subject enrollment logic
        res = subject_service.enroll_subject()  # Call the backend API
        if res:
            messagebox.showinfo("Success", f"Enrolling in Subject-{res.get(Constant.KEY_SUBJECT_ID)}."
                                           f"\nYou are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_remove_subject_page(root, student_service, subject_service):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Remove Subject").pack(pady=(10, 5))

    tk.Label(root, text="Subject ID").pack(pady=(5, 0))
    subject_id_entry = tk.Entry(root)
    subject_id_entry.pack(pady=(0, 5))
    subject_id_entry.focus_set()

    def confirm_remove_subject():
        try:
            subject_id = subject_id_entry.get()
            if subject_id:
                subject_service.remove_subject(subject_id)
                show_operation_menu(root, student_service, subject_service)
            else:
                messagebox.showerror("Error", "Incorrect input, please try again.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    confirm_button = tk.Button(root, text="Submit", command=confirm_remove_subject)
    confirm_button.pack(pady=(10, 5))

    back_button = tk.Button(root, text="Back to Menu",
                            command=lambda: show_operation_menu(root, student_service, subject_service))
    back_button.pack(pady=(5, 5))


def show_change_password_menu(root, student_service, subject_service):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Change Password").pack(pady=(10, 5))

    tk.Label(root, text="New Password:").pack(pady=(5, 0))
    new_password_entry = tk.Entry(root, show='*')
    new_password_entry.pack(pady=(0, 5))
    new_password_entry.focus_set()

    tk.Label(root, text="Confirm Password:").pack(pady=(5, 0))
    confirm_password_entry = tk.Entry(root, show='*')
    confirm_password_entry.pack(pady=(0, 5))

    def confirm_change_password():
        try:
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()
            if new_password == confirm_password:

                if not Validation.check_password_pattern(new_password):
                    messagebox.showerror("Error", "Incorrect password format.")
                else:
                    student_service.change_password(new_password)

                show_operation_menu(root, student_service, subject_service)
            else:
                messagebox.showerror("Error", "Password does not match - try again!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    confirm_button = tk.Button(root, text="Submit", command=confirm_change_password)
    confirm_button.pack(pady=(10, 5))

    back_button = tk.Button(root, text="Back to Menu",
                            command=lambda: show_operation_menu(root, student_service, subject_service))
    back_button.pack(pady=(5, 5))

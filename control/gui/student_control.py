# student_control.py
import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for displaying alerts and messages

# Import utility functions and constants for validation and other operations
from util import validation  # Import the validation module
from util.constant import Constant  # Import constants used throughout the application
from util.validation import Validation  # Import the Validation class for password checks

# Function to show the main operation menu for students
def show_operation_menu(root, student_service, subject_service):
    root.title("Welcome")  # Set the window title to "Welcome"

    # Destroy any existing widgets in the root window to refresh the UI
    for widget in root.winfo_children():
        widget.destroy()

    # Create and pack a label for the welcome message
    tk.Label(root, text="Welcome! Student Course Menu").pack(pady=(10, 5))

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)  # Add some vertical space around the frame

    # Create a button to change password and set its command
    button1 = tk.Button(button_frame, text="Change Password",
                        command=lambda: show_change_password_menu(root, student_service, subject_service))
    button1.pack(side=tk.LEFT, padx=5)  # Pack the button to the left with some horizontal padding

    # Create a button to enroll in a subject and set its command
    button2 = tk.Button(button_frame, text="Enroll Subject", command=lambda: enroll_subject(root, subject_service))
    button2.pack(side=tk.LEFT, padx=5)  # Pack the button to the left with some horizontal padding

    # Create a button to remove a subject and set its command
    button3 = tk.Button(button_frame, text="Remove Subject",
                        command=lambda: show_remove_subject_page(root, student_service, subject_service))
    button3.pack(side=tk.LEFT, padx=5)  # Pack the button to the left with some horizontal padding

    # Create a button to show subjects and set its command
    button4 = tk.Button(button_frame, text="Show Subjects",
                        command=lambda: show_subjects(root, student_service, subject_service))
    button4.pack(side=tk.LEFT, padx=5)  # Pack the button to the left with some horizontal padding

# Function to display the list of subjects
def show_subjects(root, student_service, subject_service):
    try:
        lists = subject_service.query_subjects()  # Query the subject service for the list of subjects

        # Destroy any existing widgets in the root window to refresh the UI
        for widget in root.winfo_children():
            widget.destroy()

        # Create and pack a label for the subjects list
        tk.Label(root, text="Subjects List").pack(pady=(10, 5))

        # Create a text box to display the list of subjects
        subjects_text = tk.Text(root, width=50, height=15)
        subjects_text.pack(pady=(5, 5))

        # If there are subjects, insert them into the text box
        if lists:
            for subject in lists:
                subjects_text.insert(tk.END, subject)  # Insert each subject
                subjects_text.insert(tk.END, "\n")  # Add a new line after each subject

        else:
            subjects_text.insert(tk.END, "No subjects available.")  # Message if no subjects are found

        # Create a button to go back to the operation menu
        back_button = tk.Button(root, text="Back to Menu",
                                command=lambda: show_operation_menu(root, student_service, subject_service))
        back_button.pack(pady=(5, 5))  # Pack the button with some vertical space

    except Exception as e:  # Handle any exceptions that occur
        messagebox.showerror("Error", str(e))  # Show an error message

# Function to enroll in a subject
def enroll_subject(root, subject_service):
    # This function is called when the "Enroll Subject" button is clicked
    try:
        # Replace this with the actual subject enrollment logic
        res = subject_service.enroll_subject()  # Call the backend API to enroll in a subject
        if res:  # If enrollment is successful
            messagebox.showinfo("Success", f"Enrolling in Subject-{res.get(Constant.KEY_SUBJECT_ID)}."
                                           f"\nYou are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

    except Exception as e:  # Handle any exceptions that occur
        messagebox.showerror("Error", str(e))  # Show an error message

# Function to show the page for removing a subject
def show_remove_subject_page(root, student_service, subject_service):
    # Destroy any existing widgets in the root window to refresh the UI
    for widget in root.winfo_children():
        widget.destroy()

    # Create and pack a label for removing subjects
    tk.Label(root, text="Remove Subject").pack(pady=(10, 5))

    # Create and pack a label and entry for the subject ID
    tk.Label(root, text="Subject ID").pack(pady=(5, 0))
    subject_id_entry = tk.Entry(root)  # Entry for subject ID
    subject_id_entry.pack(pady=(0, 5))  # Pack the entry with some vertical space
    subject_id_entry.focus_set()  # Focus on the entry field

    # Function to confirm the removal of a subject
    def confirm_remove_subject():
        try:
            subject_id = subject_id_entry.get()  # Get the subject ID from the entry
            if subject_id:  # If a subject ID was entered
                subject_service.remove_subject(subject_id)  # Call the service to remove the subject
                show_operation_menu(root, student_service, subject_service)  # Show the operation menu
            else:
                messagebox.showerror("Error", "Incorrect input, please try again.")  # Show error if no input
        except Exception as e:  # Handle any exceptions that occur
            messagebox.showerror("Error", str(e))  # Show an error message

    # Create a button to submit the removal of the subject
    confirm_button = tk.Button(root, text="Submit", command=confirm_remove_subject)
    confirm_button.pack(pady=(10, 5))  # Pack the button with some vertical space

    # Create a button to go back to the operation menu
    back_button = tk.Button(root, text="Back to Menu",
                            command=lambda: show_operation_menu(root, student_service, subject_service))
    back_button.pack(pady=(5, 5))  # Pack the button with some vertical space

# Function to show the change password menu
def show_change_password_menu(root, student_service, subject_service):
    # Destroy any existing widgets in the root window to refresh the UI
    for widget in root.winfo_children():
        widget.destroy()

    # Create and pack a label for changing the password
    tk.Label(root, text="Change Password").pack(pady=(10, 5))

    # Create and pack a label and entry for the new password
    tk.Label(root, text="New Password:").pack(pady=(5, 0))
    new_password_entry = tk.Entry(root, show='*')  # Entry for new password, hiding input
    new_password_entry.pack(pady=(0, 5))  # Pack the entry with some vertical space
    new_password_entry.focus_set()  # Focus on the entry field

    # Create and pack a label and entry for confirming the new password
    tk.Label(root, text="Confirm Password:").pack(pady=(5, 0))
    confirm_password_entry = tk.Entry(root, show='*')  # Entry for confirming password, hiding input
    confirm_password_entry.pack(pady=(0, 5))  # Pack the entry with some vertical space

    # Function to confirm the change of password
    def confirm_change_password():
        try:
            new_password = new_password_entry.get()  # Get the new password
            confirm_password = confirm_password_entry.get()  # Get the confirmed password
            if new_password == confirm_password:  # Check if both passwords match

                # Validate the new password format
                if not Validation.check_password_pattern(new_password):
                    messagebox.showerror("Error", "Incorrect password format.")  # Show error for invalid format
                else:
                    student_service.change_password(new_password)  # Change the password

                show_operation_menu(root, student_service, subject_service)  # Show the operation menu
            else:
                messagebox.showerror("Error", "Password does not match - try again!")  # Show error if mismatch
        except Exception as e:  # Handle any exceptions that occur
            messagebox.showerror("Error", str(e))  # Show an error message

    # Create a button to submit the new password
    confirm_button = tk.Button(root, text="Submit", command=confirm_change_password)
    confirm_button.pack(pady=(10, 5))  # Pack the button with some vertical space

    # Create a button to go back to the operation menu
    back_button = tk.Button(root, text="Back to Menu",
                            command=lambda: show_operation_menu(root, student_service, subject_service))
    back_button.pack(pady=(5, 5))  # Pack the button with some vertical space

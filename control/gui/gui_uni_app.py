import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for displaying error messages

from control.gui.student_control import show_operation_menu  # Import the operation menu function
from service.student_service import StudentService  # Import the StudentService for student-related operations
from service.subject_service import SubjectService  # Import the SubjectService for subject-related operations

# Create instances of StudentService and SubjectService
student_service = StudentService()
subject_service = SubjectService()

def set_login_session(student):
    # Set the current student in both services.
    student_service.set_student(student)  # Set the student in StudentService
    subject_service.set_student(student)  # Set the student in SubjectService

def clear_login_session():
    # Clear the current student session.
    student_service.set_student(None)  # Set student to None in StudentService
    subject_service.set_student(None)  # Set student to None in SubjectService

def login():
    # Retrieve email and password from entry fields.
    email = email_entry.get()  # Get the email entered by the user
    password = password_entry.get()  # Get the password entered by the user

    try:
        # Check if the email and password format is valid.
        if student_service.check_register_params(email, password):
            student = student_service.login(email, password)  # Attempt to log in
            if student:
                set_login_session(student)  # Set the login session if successful
                # Show the operation menu, passing root and services
                show_operation_menu(root, student_service, subject_service)  # Display the operation menu
        else:
            # Clear the entries if the format is incorrect.
            email_entry.delete(0, tk.END)  # Clear the email entry
            password_entry.delete(0, tk.END)  # Clear the password entry
            messagebox.showerror("Error", "Incorrect email and password format.")  # Show error message

    except Exception as e:
        messagebox.showerror("Login fail!", str(e))  # Show error message if login fails

# Create the main window for the application
root = tk.Tk()  # Initialize the Tkinter window
root.title("Login")  # Set the window title

# Set window size (width x height)
window_width = 600  # Width of the window
window_height = 450  # Height of the window

# Get the screen width and height
screen_width = root.winfo_screenwidth()  # Get the screen width
screen_height = root.winfo_screenheight()  # Get the screen height

# Calculate the x and y coordinates for the center of the window
x = (screen_width // 2) - (window_width // 2)  # Calculate x coordinate for centering
y = (screen_height // 2) - (window_height // 2)  # Calculate y coordinate for centering

# Set the window geometry (width x height + x_offset + y_offset)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Set the window size and position

# Create labels and entry fields for email and password
email_label = tk.Label(root, text="Email:")  # Label for email entry
email_label.pack(pady=5)  # Add the label to the window with padding
email_entry = tk.Entry(root)  # Entry field for email
email_entry.pack(pady=5)  # Add the entry to the window with padding

password_label = tk.Label(root, text="Password:")  # Label for password entry
password_label.pack(pady=5)  # Add the label to the window with padding
password_entry = tk.Entry(root, show="*")  # Entry field for password, hide input with asterisks
password_entry.pack(pady=5)  # Add the entry to the window with padding

# Create a login button
login_button = tk.Button(root, text="Sign In", command=login)  # Button to trigger login function
login_button.pack(pady=20)  # Add the button to the window with padding

# Run the main event loop
root.mainloop()  # Start the Tkinter event loop

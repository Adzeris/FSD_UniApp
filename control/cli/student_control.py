from service.student_service import StudentService  # Import StudentService for student-related operations
from service.subject_service import SubjectService  # Import SubjectService for subject-related operations
from util import validation  # Import validation utilities
from util.constant import Constant  # Import constants used in the application
from util.print_util import PrintUtil  # Import PrintUtil for formatted output
from util.validation import Validation  # Import Validation class for password checks


class StudentControl:
    """
    Student control for navigation, menu selection interaction, exception handling, and displaying messages.
    **Note**: DO NOT type any functional methods in this layer (View or Control layer).

    Fields:
        _student_service: Functional service that performs student basic functions.
        _subject_service: Functional service that executes subject enrollment functions.

    Methods:
        __init__:                       Default constructor that initializes _student_service and _subject_service.
        _set_login_session:             Private method to set the login session for the student.
        _clear_login_session:           Private method to clear the login session for the student.
        get_register_params_from_keyboard: Static method to get registration parameters from user input.
        get_login_params_from_keyboard: Static method to get login parameters from user input.
        show_student_main_menu:         Public method to show student's main options.
        _show_student_operation_menu:   Private method to show student's operational options.
        get_new_password_from_keyboard: Static method to get a new password from user input.
    """

    def __init__(self):
        # Initializes the services for student and subject operations.
        self._student_service = StudentService()  # Create an instance of StudentService
        self._subject_service = SubjectService()  # Create an instance of SubjectService

    def _set_login_session(self, student):
        # Sets the student session for both student and subject services.
        self._student_service.set_student(student)  # Set the student in StudentService
        self._subject_service.set_student(student)  # Set the student in SubjectService

    def _clear_login_session(self):
        # Clears the student session for both services.
        self._student_service.set_student(None)  # Clear the student in StudentService
        self._subject_service.set_student(None)  # Clear the student in SubjectService

    @staticmethod
    def get_register_params_from_keyboard():
        # Prompts user for registration details and returns them as a dictionary.
        PrintUtil.print_green("Student Sign Up")  # Print the sign-up prompt in green
        email = str(input("Email: "))  # Prompt for email input
        password = str(input("Password: "))  # Prompt for password input
        return {"email": email, "password": password}  # Return the inputs as a dictionary

    @staticmethod
    def get_login_params_from_keyboard():
        # Prompts user for login details and returns them as a dictionary.
        PrintUtil.print_green("Student Sign In")  # Print the sign-in prompt in green
        email = str(input("Email: "))  # Prompt for email input
        password = str(input("Password: "))  # Prompt for password input
        return {"email": email, "password": password}  # Return the inputs as a dictionary

    def show_student_main_menu(self):
        # Displays the main menu for student actions.
        while True:  # Loop to keep showing the menu until exit
            try:
                # Prompt for user input regarding login or registration.
                option = str(PrintUtil.input_cyan("Student System: (l/r/x) : ")).lower()  # Get user option

                # Handle login option.
                if option == 'l':
                    params = self.get_login_params_from_keyboard()  # Get login parameters.
                    # Check if the email and password formats are valid
                    if self._student_service.check_register_params(params.get("email"), params.get("password")):
                        PrintUtil.print_yellow("Email and password formats acceptable.")
                    else:
                        PrintUtil.print_red("Incorrect email and password format.")
                        continue  # Continue to the next iteration for re-prompting

                    student = self._student_service.login(params.get("email"), params.get("password"))  # Attempt login
                    if student:  # If login is successful
                        self._set_login_session(student)  # Set the login session
                        self._show_student_operation_menu()  # Show the operation menu

                # Handle registration option.
                elif option == 'r':
                    params = self.get_register_params_from_keyboard()  # Get registration parameters.
                    # Check if the email and password formats are valid
                    if self._student_service.check_register_params(params.get("email"), params.get("password")):
                        PrintUtil.print_yellow("Email and password formats acceptable.")
                    else:
                        PrintUtil.print_red("Incorrect email and password format.")
                        continue  # Continue to the next iteration for re-prompting

                    name = str(PrintUtil.input_cyan("Name: "))  # Get student name.
                    self._student_service.register(params.get("email"), params.get("password"), name)  # Register student.
                    print("Enrolling Student " + name)  # Print enrollment message

                # Handle exit option.
                elif option == 'x':
                    self._clear_login_session()  # Clear session before exiting.
                    break  # Exit the loop

                # Handle incorrect input.
                else:
                    raise Exception("Incorrect input, please try again.")  # Raise an exception for invalid input
            except Exception as e:
                PrintUtil.print_red(str(e))  # Print any exceptions that occur in red

    def _show_student_operation_menu(self):
        # Displays the menu for student operations (e.g., enrolling in subjects).
        while True:  # Loop to keep showing the operation menu
            try:
                option = str(PrintUtil.input_cyan("Student Course Menu: (c/e/r/s/x) : ")).lower()  # Get user option

                # Change password option.
                if option == Constant.S_CHANGE_PASSWORD:
                    PrintUtil.print_yellow("Updating Password")  # Indicate password update
                    new_password = self.get_new_password_from_keyboard()  # Get new password from user.
                    # Check if the new password format is valid
                    if not Validation.check_password_pattern(new_password):
                        PrintUtil.print_red("Incorrect password format.")
                        continue  # Continue to the next iteration for re-prompting
                    self._student_service.change_password(new_password)  # Update the password

                # Enroll in a subject.
                elif option == Constant.S_ENROLLING:
                    res = self._subject_service.enroll_subject()  # Enroll the student in a subject.
                    PrintUtil.print_yellow(f"Enrolling in Subject-{res.get(Constant.KEY_SUBJECT_ID)}.")
                    PrintUtil.print_yellow(f"You are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

                # Remove subject enrollment.
                elif option == Constant.S_REMOVING:
                    subject_id = str(PrintUtil.input_cyan("Remove Subject By ID: "))  # Get subject ID to remove.
                    res = self._subject_service.remove_subject(subject_id)  # Remove the subject.
                    PrintUtil.print_yellow(f"Dropping Subject-{res.get(Constant.KEY_SUBJECT_ID)}.")
                    PrintUtil.print_yellow(f"You are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

                # Show enrolled subjects.
                elif option == Constant.S_SHOW:
                    subjects = self._subject_service.query_subjects()  # Query enrolled subjects.
                    PrintUtil.print_yellow(f"Showing {len(subjects)} subjects")  # Print the number of subjects
                    if subjects:  # If there are subjects
                        for subject in subjects:
                            print(str(subject))  # Print each subject.

                # Exit to parent menu.
                elif option == Constant.EXIT:
                    break  # Exit the loop

                # Handle incorrect input.
                else:
                    raise Exception("Incorrect input, please try again.")  # Raise an exception for invalid input
            except Exception as e:
                print(str(e))  # Print any exceptions that occur

    @staticmethod
    def get_new_password_from_keyboard():
        # Prompts the user for a new password and confirmation.
        new_password = str(input("New Password: "))  # Prompt for new password
        confirm_password = str(input("Confirm Password: "))  # Prompt for confirmation
        while True:  # Loop until passwords match
            if new_password != confirm_password:  # Check if passwords match
                print("Password does not match - try again.")  # Indicate mismatch
                confirm_password = str(input("Confirm Password: "))  # Prompt for confirmation again
            else:
                break  # Exit loop if passwords match
        return new_password  # Return the new password once confirmed

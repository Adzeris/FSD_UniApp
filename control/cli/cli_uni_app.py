# Importing necessary classes for admin and student controls and a utility function for input formatting
from control.cli.admin_control import AdminControl  # AdminControl handles admin functionalities
from control.cli.student_control import StudentControl  # StudentControl handles student functionalities
from util.util import input_cyan  # input_cyan is a utility for getting user input in a specific color

# Define the main function that starts the application
def main():
    print("UniApp is running!")  # Print a message indicating the application is running

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function to run the application

# Define the CLIUniApp class for the university system command-line interface
class CLIUniApp:
    """
    University System CLIApp control entrance
    """

    # Initialization method for the CLIUniApp class
    def __init__(self):
        self._admin_control = AdminControl()  # Create an instance of AdminControl
        self._student_control = StudentControl()  # Create an instance of StudentControl

    # Method to display the university menu and handle user input
    def show_uni_menu(self) -> None:
        """
        # TODO add exception handling process
        Show University System Menu
        :return: None
        """
        while True:  # Start an infinite loop to keep showing the menu
            # Prompt user for input and convert to uppercase
            option = str(input_cyan("University System: (A)dmin, (S)tudent, or X : ")).upper()

            # If the user selects admin menu
            if option == 'A':
                self._admin_control.show_admin_main_menu()  # Display the admin main menu

            # If the user selects student menu
            elif option == 'S':
                self._student_control.show_student_main_menu()  # Display the student main menu

            # If the user wants to exit the application
            elif option == 'X':
                print("Thank You")  # Print a thank-you message
                break  # Exit the loop

            # If the user inputs an invalid option
            else:
                print("Incorrect input, please try again.")  # Prompt for correct input

# Final entry point check to start the application
if __name__ == '__main__':
    CLIUniApp().show_uni_menu()  # Create an instance of CLIUniApp and show the university menu

from control.cli.admin_control import AdminControl
from control.cli.student_control import StudentControl
from util.util import input_cyan


class CLIUniApp:
    """
    University System CLIApp control entrance
    """
    def __init__(self):
        self._admin_control = AdminControl()
        self._student_control = StudentControl()

    def show_uni_menu(self) -> None:
        """
        # TODO add exception handling process
        show University System Menu
        :return: None
        """
        while True:
            option = str(input_cyan("University System: (A)dmin, (S)tudent, or X : ")).upper()

            # show admin menu
            if option == 'A':
                self._admin_control.show_admin_main_menu()

            # show student menu
            elif option == 'S':
                self._student_control.show_student_main_menu()

            # exit the system
            elif option == 'X':
                print("Thank You")
                break

            # incorrect input, loop continue
            else:
                print("Incorrect input, please try again.")


if __name__ == '__main__':
    CLIUniApp().show_uni_menu()

from control.cli.admin_control import AdminControl
from control.cli.student_control import StudentControl
from util.constant import Constant
from util.print_util import PrintUtil


class CLIUniApp:
    """
    University System CLIApp control entrance
    """

    def __init__(self):
        self._admin_control = AdminControl()
        self._student_control = StudentControl()

    def show_uni_menu(self) -> None:
        """
        show University System Menu
        :return: None
        """
        while True:
            option = str(PrintUtil.input_cyan("University System: (A)dmin, (S)tudent, or X : ")).lower()

            # show admin menu
            if option == Constant.ADMIN:
                self._admin_control.show_admin_main_menu()

            # show student menu
            elif option == Constant.STUDENT:
                self._student_control.show_student_main_menu()

            # exit the system
            elif option == Constant.EXIT:
                print("Thank You")
                break

            # incorrect input, loop continue
            else:
                print("Incorrect input, please try again.")


if __name__ == '__main__':
    CLIUniApp().show_uni_menu()

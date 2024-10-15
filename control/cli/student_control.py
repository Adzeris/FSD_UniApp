
from service.student_service import StudentService
from service.subject_service import SubjectService
from util import validation
from util.constant import Constant
from util.print_util import PrintUtil
from util.validation import Validation


class StudentControl:
    """
    student control that just for navigation, menu selection interaction, exception handling, display message.
    **Note** DO NOT type any functional methods in this layer (View or Control layer)

    Fields:
        _student_service: functional service that specified to perform student basic functions.
        _subject_service: functional service that specified to execute subject enrollment functions.

    Methods:
        __init__:                       default constructor that init _student_service and _subject_service
        _show_student_operation_menu:   private method that show student's operational options
        show_student_main_menu:         public method that show student's main options.
    """

    def __init__(self):
        self._student_service = StudentService()
        self._subject_service = SubjectService()

    def _set_login_session(self, student):
        self._student_service.set_student(student)
        self._subject_service.set_student(student)

    def _clear_login_session(self):
        self._student_service.set_student(None)
        self._subject_service.set_student(None)

    @staticmethod
    def get_register_params_from_keyboard():
        PrintUtil.print_green("Student Sign Up")
        email = str(input("Email: "))
        password = str(input("Password: "))

        return {"email": email, "password": password}

    @staticmethod
    def get_login_params_from_keyboard():
        PrintUtil.print_green("Student Sign In")
        email = str(input("Email: "))
        password = str(input("Password: "))
        return {"email": email, "password": password}

    def show_student_main_menu(self):
        while True:
            try:
                option = str(PrintUtil.input_cyan("Student System: (l/r/x) : ")).lower()

                # call _student_service.login to log in for performing further operations
                if option == 'l':
                    # upon logining, show student operation menu.
                    params = self.get_login_params_from_keyboard()
                    if self._student_service.check_register_params(params.get("email"), params.get("password")):
                        PrintUtil.print_yellow("email and password formats acceptable.")
                    else:
                        PrintUtil.print_red("Incorrect email and password format.")
                        continue
                    student = self._student_service.login(params.get("email"), params.get("password"))
                    if student:
                        self._set_login_session(student)
                        self._show_student_operation_menu()
                # call student_service.register to register a new student
                elif option == 'r':
                    params = self.get_login_params_from_keyboard()
                    if self._student_service.check_register_params(params.get("email"), params.get("password")):
                        PrintUtil.print_yellow("email and password formats acceptable.")
                    else:
                        PrintUtil.print_red("Incorrect email and password format.")
                        continue
                    name = str(PrintUtil.input_cyan("Name: "))
                    self._student_service.register(params.get("email"), params.get("password"), name)
                    print("Enrolling Student " + name)
                # navigate to University System Menu
                elif option == 'x':
                    self._clear_login_session()
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                PrintUtil.print_red(str(e))

    def _show_student_operation_menu(self):
        while True:
            try:
                option = str(PrintUtil.input_cyan("Student Course Menu: (c/e/r/s/x) : ")).lower()

                # for changing student's password
                # call _student_service.change_password
                if option == Constant.S_CHANGE_PASSWORD:
                    PrintUtil.print_yellow("Updating Password")
                    new_password = self.get_new_password_from_keyboard()
                    if not Validation.check_password_pattern(new_password):
                        PrintUtil.print_red("Incorrect password format.")
                        continue
                    self._student_service.change_password(new_password)

                # for subject enrollment
                # call _subject_service.enroll_subject()
                elif option == Constant.S_ENROLLING:
                    res = self._subject_service.enroll_subject()
                    PrintUtil.print_yellow(f"Enrolling in Subject-{res.get(Constant.KEY_SUBJECT_ID)}.")
                    PrintUtil.print_yellow(f"You are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

                # for removing subject enrollment
                # call _subject_service.remove_subject()
                elif option == Constant.S_REMOVING:
                    subject_id = str(PrintUtil.input_cyan("Remove Subject By ID: "))
                    res = self._subject_service.remove_subject(subject_id)
                    PrintUtil.print_yellow(f"Dropping Subject-{res.get(Constant.KEY_SUBJECT_ID)}.")
                    PrintUtil.print_yellow(f"You are now enrolled in {res.get(Constant.KEY_COUNT)} out of 4 subjects")

                # for showing enrolled subjects
                # call _subject_service.show_subjects()
                elif option == Constant.S_SHOW:
                    subjects = self._subject_service.query_subjects()
                    PrintUtil.print_yellow(f"Showing {len(subjects)} subjects")
                    if subjects:
                        for subject in subjects:
                            print(str(subject))

                # for navigating to parent menu
                elif option == Constant.EXIT:
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                print(str(e))

    @staticmethod
    def get_new_password_from_keyboard():
        new_password = str(input("New Password: "))
        confirm_password = str(input("Confirm Password: "))
        while True:
            if new_password != confirm_password:
                print("Password does not match - try again.")
                confirm_password = str(input("Confirm Password: "))
            else:
                break
        return new_password

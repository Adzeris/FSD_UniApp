import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


##from service.admin_service import AdminService
from service.admin_service import AdminService
from util.util import input_cyan


class AdminControl:
    """
    student control that just for navigation, menu selection interaction, exception handling, display message.
    **Note** DO NOT type any functional methods in this layer (View or Control layer)

    Fields:
        _admin_service:     functional service that specified to query admin basic information.
        _subject_service:   functional service that specified to execute subject enrollment functions.

    Methods:
        __init__:                       default constructor that init _student_service and _subject_service
        _show_student_operation_menu:   private method that show student's operational options
        show_student_main_menu:         public method that show student's main options.
    """

    def __init__(self):
        self._admin_service = AdminService()
        pass

    def show_admin_main_menu(self):
        while True:
            try:
                option = str(input_cyan("Admin System: (c/g/p/r/s/x) : ")).lower()

                # call _admin_service.clear_database to delete all student's information and enrollment records.
                if option == 'c':
                    print("Clearing students database.")
                    confirm = str(input_cyan("Are you sure you want to clear the database (Y)ES/(N)O: "))
                    if confirm == 'Y':
                        self._admin_service.clear_database()
                        print("Students data cleared.")

                # call _admin_service.group_students to show students by grade
                elif option == 'g':
                    subjects = self._admin_service.group_students()
                    print("Grade Grouping")
                    if subjects:
                        for item in subjects:
                            print(str(item))
                    else:
                        print("< Nothing to Display >")

                # call _admin_service.partition_students to partition students to PASS/FAIL categories.
                elif option == 'p':
                    pass_list, fail_list = self._admin_service.partition_students()
                    print("PASS/FAIL Partition.")
                    print(f"FAIL --> {fail_list}")
                    print(f"PASS --> {pass_list}")

                # call _admin_service.remove_student to remove student by id.
                elif option == 'r':
                    student_id = str(input_cyan("Remove by ID: "))
                    self._admin_service.remove_student(student_id)

                # call _admin_service.show_all_students to show all student's and enrollment information.
                elif option == 's':
                    students = self._admin_service.show_all_students()
                    print("Student List")
                    if students:
                        for student in students:
                            print(str(student))
                    else:
                        print("< Nothing to Display >")

                # navigate to University System Menu
                elif option == 'x':
                    break

                # incorrect input, loop continue
                else:
                    raise Exception("Incorrect input, please try again.")
            except Exception as e:
                print(str(e))

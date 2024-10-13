from typing import List

from dao.entity.student import Student
from dao.impl.abs_dao import AbsDao
from util.exception import DataAccessException, PrimaryKeyDuplicationException, UniqueKeyDuplicationException


class StudentDao(AbsDao):
    """
    Student Data Access Object
    providing CRUD operations of student information
        add_student:                add a new student into database
        query_student_info_by_id:   get a specific student by using student_id
        query_student_list:         get a student list which includes all student information
        query_student_by_email:     get a specific student by using student_email
        update_student:             update a student's information and save to the database
        delete_student_by_id:       delete a student and all enrollments by student_id

    ** Note ** About Data Integrity:
        ->  Service layer is responsible for Data integrity, logically.
        ->  Dao layer just for CURD. don't check any data integrity
    """

    def __init__(self):
        # init database instance
        super().__init__()

    def add_student(self, student):
        """
        Add a new student information to database

        :param      student: student information, excluding _student_category and _subject_list
        :return:    return none if process succeed
        """

        # 0: check primary key and non-nullable keys
        self.raise_dao_exception_if_any_empty(student_id=student.get_student_id(),
                                              student_name=student.get_student_name(),
                                              student_email=student.get_student_email())

        # 1: query students list
        students = self._database.get_students()

        # 2: check for none and duplicate entity
        if students:
            # check duplicate entity
            self.raise_dao_exception_if_repeated(students, student)
            students.append(student)
        else:
            students = [student]

        # 3: saving data to file
        self._database.write_students(students)

    def query_student_info_by_id(self, student_id) -> Student | None:
        """
        Query one student information by using a specific student id

        :param      student_id:     student's id, primary key in database
        :return:    Student or None(if there is no entity is related to parameter)
        """
        # 0: check param
        self.raise_dao_exception_if_any_empty(student_id=student_id)

        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return None

        # 2: filter student
        matching_students = [student for student in students if student.get_student_id() == student_id]

        return matching_students[0] if matching_students else None

    def query_student_by_email(self, email) -> Student | None:
        """
        Query one student information by using a specific student email

        :param      email:     student's email, unique key in database
        :return:    Student or None(if there is no entity is related to parameter)
        """
        # 0: check param
        self.raise_dao_exception_if_any_empty(email=email)

        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return None

        # 2: filter student
        matching_students = [student for student in students if student.get_student_email() == email]

        return matching_students[0] if matching_students else None

    def query_student_list(self) -> List[Student]:
        """
        query all students
        :return: List[Student]
        """
        students = self._database.get_students()
        return students if students else []

    def update_student(self, student):
        """
        update a student information by given student from parameter
        using delete first add after to simulate update.

        :param student: student information, student_id must be included
        """
        # 0: check param
        self.raise_dao_exception_if_any_empty(student=student)
        self.raise_dao_exception_if_any_empty(student_id=student.get_student_id(),
                                              student_name=student.get_student_name(),
                                              student_email=student.get_student_email())

        # 1: query student
        students = self._database.get_students()

        # 2: remove student that should be deleted
        remain_students = [item for item in students if item.get_student_id() != student.get_student_id()]

        # 3: check duplication
        self.raise_dao_exception_if_repeated(remain_students, student)

        # 4: add new student that should be added
        remain_students.append(student)

        # 5: saving data to database
        self._database.write_students(remain_students)

    def delete_student_by_id(self, student_id):
        """
        delete one student by using student id

        :param      student_id: student's id, primary key in database
        :exception
        """
        # 0: check param
        self.raise_dao_exception_if_any_empty(student_id=student_id)

        # 1: query all student
        students = self._database.get_students()
        # check if students list is empty
        if not students:
            return

        # 2: filter student to deleting the data that needs to be deleted
        remain_students = [student for student in students if student.get_student_id() != student_id]

        # 3: saving remain students to database
        self._database.write_students(remain_students)

    @staticmethod
    def raise_dao_exception_if_repeated(students, student):
        for item in students:
            if item.get_student_id() == student.get_student_id():
                raise PrimaryKeyDuplicationException("Student id (" + student.get_student_id() + ") already exists.")
            if item.get_student_email() == student.get_student_email():
                raise UniqueKeyDuplicationException("Student email (" + student.get_student_email() + ") already exists.")

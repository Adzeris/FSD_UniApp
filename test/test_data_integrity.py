import unittest

from dao.entity.student import Student
from dao.impl.admin_dao import AdminDao
from dao.impl.student_dao import StudentDao
from dao.impl.subject_dao import SubjectDao
from util.exception import DataAccessException, PrimaryKeyDuplicationException, UniqueKeyDuplicationException


class TestStudentDao(unittest.TestCase):

    def setUp(self):
        self.admin_dao = AdminDao()
        self.student_dao = StudentDao()
        self.subject_dao = SubjectDao
        self.admin_dao.delete_all_students_and_subjects()
        self.students = []

    def test_add_students_raise_DataAccessException(self):
        # 1: student id is null, raise DataAccessException
        with self.assertRaises(DataAccessException):
            self.student_dao.add_student(Student("", "student_name1",
                                                 "student_email1", "pass1"))
        # 2: student name is null, raise DataAccessException
        with self.assertRaises(DataAccessException):
            self.student_dao.add_student(Student("student_id1", "",
                                                 "student_email1", "pass1"))
        # 3: student email is null, raise DataAccessException
        with self.assertRaises(DataAccessException):
            self.student_dao.add_student(Student("student_id1", "student_name1",
                                                 "", "pass1"))

    def test_add_student_raise_PrimaryKeyDuplicationException(self):
        # 1: add a new student information
        self.student_dao.add_student(Student("student_id1", "student_name1",
                                             "student_email1", "pass1"))

        # 2: student id exists, raise PrimaryKeyDuplicationException
        with self.assertRaises(PrimaryKeyDuplicationException):
            self.student_dao.add_student(Student("student_id1", "student_name2222",
                                                 "student_email2222", "pass2222"))

    def test_add_student_raise_UniqueKeyDuplicationException(self):
        # 1: add a new student information
        self.student_dao.add_student(Student("student_id1", "student_name1",
                                             "student_email1", "pass1"))

        # 2: student email exists, raise UniqueKeyDuplicationException
        with self.assertRaises(UniqueKeyDuplicationException):
            self.student_dao.add_student(Student("student_id2", "student_name2222",
                                                 "student_email1", "pass2222"))

    def test_query_student_info_by_id_raise_DataAccessException(self):

        # 1: add a new student information
        self.student_dao.add_student(Student("student_id1", "student_name1",
                                             "student_email1", "pass1"))

        # 2: query student.
        student = self.student_dao.query_student_info_by_id("student_id1")
        self.assertIsNotNone(student)
        self.assertEqual(student.get_student_id(), "student_id1")

        # 3: query student raise DataAccessException if input param is null
        with self.assertRaises(DataAccessException):
            self.student_dao.query_student_info_by_id("")

    def test_query_student_info_by_email_raise_DataAccessException(self):
        # 1: add a new student information
        self.student_dao.add_student(Student("student_id1", "student_name1",
                                             "student_email1", "pass1"))

        # 2: query student.
        student = self.student_dao.query_student_by_email("student_email1")
        self.assertIsNotNone(student)
        self.assertEqual(student.get_student_id(), "student_id1")

        # 3: query student raise DataAccessException if input param is null
        with self.assertRaises(DataAccessException):
            self.student_dao.query_student_by_email("")

    def test_update_student_raise_DataAccessException(self):
        # 1: add a new student information
        self.student_dao.add_student(Student("student_id1", "student_name1",
                                             "student_email1", "pass1"))

        # 2: update student, raise DataAccessException if parameter is null
        with self.assertRaises(DataAccessException):
            self.student_dao.update_student(None)

        # 3: update student, raise DataAccessException if any arguments is null
        with self.assertRaises(DataAccessException):
            self.student_dao.update_student(Student("", "student_name1",
                                                    "student_email1", "pass1"))

        with self.assertRaises(DataAccessException):
            self.student_dao.update_student(Student("student_id1", "",
                                                    "student_email1", "pass1"))

        with self.assertRaises(DataAccessException):
            self.student_dao.update_student(Student("student_id1", "student_name1",
                                                    "", "pass1"))


if __name__ == '__main__':
    unittest.main()

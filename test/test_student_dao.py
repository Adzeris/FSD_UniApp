import unittest

from dao.entity.student import Student
from dao.impl.admin_dao import AdminDao
from dao.impl.student_dao import StudentDao


class TestStudentDao(unittest.TestCase):

    def setUp(self):
        # clear all students and subjects
        self.admin_dao = AdminDao()
        self.student_dao = StudentDao()
        self.admin_dao.delete_all_students_and_subjects()

        # init 3 student into database
        self.student_dao.add_student(Student("student_id1", "student_name1", "student_email1", "pass1"))
        self.student_dao.add_student(Student("student_id2", "student_name2", "student_email2", "pass2"))
        self.student_dao.add_student(Student("student_id3", "student_name3", "student_email3", "pass3"))

    def test_add_students(self):
        # query student list and check length
        students = self.student_dao.query_student_list()
        self.assertEqual(len(students), 3)

        self.student_dao.add_student(Student("student_id4", "student_name4", "student_email4", "pass1"))

        students = self.student_dao.query_student_list()
        self.assertEqual(len(students), 4)

    def test_query_student_by_id(self):
        # query student by email
        student = self.student_dao.query_student_info_by_id("student_id1")
        self.assertEqual(student.get_student_email(), "student_email1")

    def test_query_student_by_email(self):
        # query student by email
        student = self.student_dao.query_student_by_email("student_email2")
        self.assertEqual(student.get_student_id(), "student_id2")

    def test_query_student_list(self):
        # query student by email
        students = self.student_dao.query_student_list()
        self.assertEqual(len(students), 3)

    def test_delete_by_student_id(self):
        self.student_dao.delete_student_by_id("student_id3")
        students = self.student_dao.query_student_list()
        self.assertEqual(len(students), 2)

    def test_update_student(self):
        # query one student information by student id
        student = self.student_dao.query_student_info_by_id("student_id1")
        student.set_student_name("student_name_new")
        student.set_student_email("student_email_new")

        # update student
        self.student_dao.update_student(student)

        # check result
        updated_student = self.student_dao.query_student_info_by_id("student_id1")
        self.assertEqual(updated_student.get_student_name(), "student_name_new")
        self.assertEqual(updated_student.get_student_email(), "student_email_new")


if __name__ == '__main__':
    unittest.main()

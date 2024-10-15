import unittest

from dao.database.database import Database
from dao.entity.student import Student
from dao.entity.subject import Subject


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # create database for preparation
        self.database = Database()

        self.students = [Student("student_id1", "student_name1", "email1", "pass1", "c1"),
                         Student("student_id2", "student_name2", "email2", "pass2", "c2")]

        self.subjects = [Subject("student_id1", "subject_id1", 89, "A")]

    def test_write_and_get_students(self):
        # write students
        self.database.write_students(self.students)
        # get students
        get_students = self.database.read_students()

        # check result
        self.assertEqual(len(get_students), 2)
        self.assertEqual(get_students[0].get_student_id(), "student_id1")
        self.assertEqual(get_students[1].get_student_name(), "student_name2")

    def test_add_new_student(self):
        # add new student
        new_student = Student("student_id3", "student_name3", "email3", "pass3", "c1")
        self.students.append(new_student)
        self.database.write_students(self.students)
        get_students = self.database.read_students()
        # check result
        self.assertEqual(len(get_students), 3)
        self.assertEqual(get_students[2].get_student_id(), "student_id3")
        self.assertEqual(get_students[2].get_student_name(), "student_name3")

    def test_remove_student(self):
        get_students = self.database.read_students()
        students = [student for student in get_students if student.get_student_id() == "student_id3"]
        get_students.remove(students[0])

        self.database.write_students(get_students)
        get_students = self.database.read_students()
        # check result
        self.assertEqual(len(get_students), 2)

    def test_write_and_get_subjects(self):
        # write subjects
        self.database.write_subjects(self.subjects)
        # get subjects
        get_subjects = self.database.read_subjects()

        # check result
        self.assertEqual(len(get_subjects), 1)
        self.assertEqual(get_subjects[0].get_student_id(), "student_id1")
        self.assertEqual(get_subjects[0].get_subject_id(), "subject_id1")
        self.assertEqual(get_subjects[0].get_subject_mark(), 89)
        self.assertEqual(get_subjects[0].get_subject_grade(), 'A')

    def test_add_new_subject(self):
        # update subject
        new_subjects = Subject("student_2", "subject1", 100, "B")
        self.subjects.append(new_subjects)
        self.database.write_subjects(self.subjects)
        get_subjects = self.database.read_subjects()
        self.assertEqual(len(get_subjects), 2)
        self.assertEqual(get_subjects[1].get_student_id(), "student_2")
        self.assertEqual(get_subjects[1].get_subject_id(), "subject1")
        self.assertEqual(get_subjects[1].get_subject_mark(), 100)
        self.assertEqual(get_subjects[1].get_subject_grade(), "B")

    def test_remove_subject(self):
        get_subjects = self.database.read_subjects()
        subjects = [subject for subject in get_subjects if subject.get_subject_id() == "subject1"]
        get_subjects.remove(subjects[0])

        self.database.write_subjects(get_subjects)
        get_subjects = self.database.read_subjects()
        # check result
        self.assertEqual(len(get_subjects), 1)


if __name__ == '__main__':
    unittest.main()

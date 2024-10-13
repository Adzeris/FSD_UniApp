import random

from dao.database.database import Database
from dao.entity.admin import Admin
from dao.entity.student import Student
from dao.entity.subject import Subject
from dao.impl.admin_dao import AdminDao
from dao.impl.student_dao import StudentDao
from dao.impl.subject_dao import SubjectDao


def test_database():

    database = Database()

    students = [Student("id1", "name1","email1", "pass1", "c1"),
                Student("id2", "name2","email2", "pass2", "c2")]

    subjects = [Subject("id1","id1", 89, "A")]

    admins = [Admin("id1", "name1", "email1"), Admin("id2","name2","email2")]

    database.write_admins(admins)
    database.write_subjects(subjects)
    database.write_students(students)

    subjects = [Subject("id1","id1", 100, "B")]
    database.write_subjects(subjects)

    get_subjects = database.get_subjects()
    for item in get_subjects:
        print(item)

    get_students = database.get_students()
    for item in get_students:
        print(item)


def test_admin_dao():
    admin_dao = AdminDao()
    admin = admin_dao.query_admin_by_staff_id("ddd")
    print(str(admin))
    admin = admin_dao.query_admin_by_staff_id("id1")
    print(str(admin))
    admin = admin_dao.query_admin_by_staff_name("ddd")
    print(str(admin))
    admin = admin_dao.query_admin_by_staff_name("name1")
    print(str(admin))


def test_student_dao():
    student_dao = StudentDao()
    students = student_dao.query_student_list()
    for student in students:
        print(str(student))
    print("-----------------------")
    stu = student_dao.query_student_by_email("email3")
    print(str(stu))
    print("---------------------")

    student_dao.delete_student_by_id("id3")

    student_dao.add_student(Student("id3","name3","email3","pa3"))
    student = student_dao.query_student_info_by_id("id3")
    print(str(student))
    print("-----------------------")

    student_dao.delete_student_by_id("id3")
    students = student_dao.query_student_list()
    for student in students:
        print(str(student))
    print("-----------------------")
    student = student_dao.query_student_info_by_id("id1")
    student.set_student_id("")
    student.set_student_email("name" + str(random.randint(100,200)))
    student.set_student_password("password" + str(random.randint(100,200)))
    student_dao.update_student(student)

    students = student_dao.query_student_list()
    for student in students:
        print(str(student))
    print("-----------------------")



def test_subject_dao():
    subject_dao = SubjectDao()

    subject = Subject("id3", "id3", 90, "A")
    subject2 = Subject("id5", "id5", 101, "x")
    subject3 = Subject("id5", "id5", 101, "x")

    subject_dao.add_subject(subject)
    subject_dao.add_subject(subject2)
    subject_dao.add_subject(subject3)

    subject.set_subject_grade("X")
    subject.set_subject_mark(101)
    subject_dao.update_subject(subject)

    lists = subject_dao.query_subject_list_by_student_id("id3")
    if lists:
        for item in lists:
            print(str(item))
    else:
        print("none")

    one = subject_dao.query_subject_by_student_and_subject("id3", "id3")
    print(str(one))

    one = subject_dao.query_subject_by_student_and_subject("id3", "id4")
    print(str(one))

    subject_dao.delete_subject_by_student_and_subject("id4", "id5")
    subject_dao.delete_subject_by_student_and_subject("id3", "id3")
    subject_dao.delete_subject_list_by_student_id("id5")




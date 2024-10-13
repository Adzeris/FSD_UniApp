import random

from dao.database.database import Database
from dao.entity.admin import Admin
from dao.entity.student import Student
from dao.entity.subject import Subject
from dao.impl.admin_dao import AdminDao
from dao.impl.student_dao import StudentDao
from dao.impl.subject_dao import SubjectDao


def test_database():

    su = []
    print(f"showing {len(su)} subjects")


import unittest

from dao.entity.subject import Subject
from dao.impl.admin_dao import AdminDao
from dao.impl.subject_dao import SubjectDao


class TestSubjectDao(unittest.TestCase):

    def setUp(self):
        # clear all students and subjects
        self.admin_dao = AdminDao()
        self.admin_dao.delete_all_students_and_subjects()

        # init subject dao
        self.subject_dao = SubjectDao()

        # create test data
        self.subject1 = Subject("student_id1", "subject_id1", 90, "A")
        self.subject2 = Subject("student_id1", "subject_id2", 102, "B")
        self.subject3 = Subject("student_id1", "subject_id3", 50, "C")
        self.subject4 = Subject("student_id2", "subject_id4", 70, "D")

    def test_add_and_query_subject_list(self):
        # add
        self.subject_dao.add_subject(self.subject1)
        self.subject_dao.add_subject(self.subject2)
        self.subject_dao.add_subject(self.subject3)
        self.subject_dao.add_subject(self.subject4)

        # query subject list
        lists = self.subject_dao.query_all_subjects()
        self.assertIsNotNone(lists)
        self.assertEqual(len(lists), 4)
        self.assertEqual(lists[0].get_subject_id(), "subject_id1")

    def test_query_subject_by_student_and_subject(self):
        self.test_add_and_query_subject_list()

        one = self.subject_dao.query_subject_by_student_and_subject("student_id1", "subject_id1")
        self.assertIsNotNone(one)
        self.assertEqual(one.get_subject_mark(), 90)

        # 查询不存在的subject
        none_subject = self.subject_dao.query_subject_by_student_and_subject("student_id100", "subject_id100")
        self.assertIsNone(none_subject)

    def test_query_subject_count_by_student_id(self):
        self.test_add_and_query_subject_list()

        count = self.subject_dao.query_subject_count_by_student_id("student_id1")
        self.assertIsNotNone(count)
        self.assertEqual(count, 3)

        count = self.subject_dao.query_subject_count_by_student_id("student_id2")
        self.assertIsNotNone(count)
        self.assertEqual(count, 1)

        count = self.subject_dao.query_subject_count_by_student_id("student_id3")
        self.assertIsNotNone(count)
        self.assertEqual(count, 0)

    def test_query_subject_list_by_student_id(self):
        self.test_add_and_query_subject_list()

        lists = self.subject_dao.query_subject_list_by_student_id("student_id1")
        self.assertIsNotNone(lists)
        self.assertEqual(len(lists), 3)

        lists = self.subject_dao.query_subject_list_by_student_id("student_id2")
        self.assertIsNotNone(lists)
        self.assertEqual(len(lists), 1)

    def test_update_subject(self):
        # init
        self.test_add_and_query_subject_list()

        # query one by student id and subject id
        one = self.subject_dao.query_subject_by_student_and_subject("student_id1", "subject_id1")
        # update
        one.set_subject_mark(100000)
        one.set_subject_grade("XXXX")
        self.subject_dao.update_subject(one)

        # query for check
        updated_subject = self.subject_dao.query_subject_by_student_and_subject("student_id1", "subject_id1")
        self.assertEqual(updated_subject.get_subject_grade(), "XXXX")
        self.assertEqual(updated_subject.get_subject_mark(), 100000)

    def test_delete_subject(self):
        # init
        self.test_add_and_query_subject_list()

        # delete one
        self.subject_dao.delete_subject_by_student_and_subject("student_id1", "subject_id1")
        deleted_subject = self.subject_dao.query_subject_by_student_and_subject("student_id1", "subject_id1")
        self.assertIsNone(deleted_subject)

        # delete one that does not exist
        self.subject_dao.delete_subject_by_student_and_subject("student_id100", "subject_id100")
        no_subject = self.subject_dao.query_subject_by_student_and_subject("student_id100", "subject_id100")
        self.assertIsNone(no_subject)

        # 删除整个学生的subject列表
        self.subject_dao.delete_subject_list_by_student_id("student_id1")
        subject_list = self.subject_dao.query_subject_list_by_student_id("student_id1")
        self.assertEqual(len(subject_list), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

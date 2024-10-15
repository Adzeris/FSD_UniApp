import random
from typing import List

from dao.entity.student import Student
from dao.entity.subject import Subject
from dao.impl.subject_dao import SubjectDao
from util.constant import Constant
from util.exception import BusinessException
from util.serialization import Serialization


class SubjectService:
    """
    define basic student method, including:

    Fields:
        _subject_dao refers to the subject data access, it provides CRUD operations with Subject enrollment information

    Methods:
        _init:              public default constructor, init _subject_dao object

        enroll_subject      public method for enrollment student's subject
        remove subject      public method for removing one student's subject
        show_subjects       public method for show all subjects enrolled.
    """

    def __init__(self):
        self._subject_dao = SubjectDao()
        self._student = None

    def set_student(self, student: Student | None):
        self._student = student

    def get_student(self) -> Student:
        return self._student

    def enroll_subject(self) -> dict[Constant, str | int]:
        """
        enroll subject
        1. system generate subject id automatically.
        2. after enrollment, system assigns a mark and grade automatically.
        :return: two key-value pairs, simulate return value for front page to display
                 1. subject_id = xxxx
                 2. enrolled_amount = xxx
        """
        # 1: raise exception if student isn't in logging state.
        if not self._student:
            raise BusinessException("Please login in first.")

        # 2: check total amount of enrolled subjects
        count = self._subject_dao.query_subject_count_by_student_id(self.get_student().get_student_id())
        if count >= 4:
            raise BusinessException("Student are allowed to enroll in 4 subjects only.")

        # 2: generate a subject id, that is a 3-digit number
        subject_id = self.simulate_select_subject()

        # 3: saving subject to database
        subject = Subject(self._student.get_student_id(), subject_id)
        self._subject_dao.add_subject(subject)

        # 4: randomly generate a mark to this subject
        self._assign_mark_grade(subject)

        # 5: encapsulate key-value pairs
        return {Constant.KEY_SUBJECT_ID: subject_id, Constant.KEY_COUNT: count + 1}

    def remove_subject(self, subject_id) -> dict[Constant, str | int]:
        """
        delete a specific subject enrollment of a particular student.
        :param subject_id:
        """

        # 1: raise exception if student isn't in logging state.
        if not self._student:
            raise BusinessException("Please login in first.")

        # 2: check whether such subject exists.
        subject = self._subject_dao.query_subject_by_student_and_subject(self.get_student().get_student_id(),
                                                                         subject_id)
        if not subject:
            raise BusinessException("Subject-" + subject_id + " does not exist.")

        # 3: delete from database
        self._subject_dao.delete_subject_by_student_and_subject(self.get_student().get_student_id(), subject_id)

        # 4: encapsulate result
        count = self._subject_dao.query_subject_count_by_student_id(self._student.get_student_id())
        return {Constant.KEY_SUBJECT_ID: subject_id, Constant.KEY_COUNT: count}

    def query_subjects(self) -> List[Subject]:
        """
        query all subjects of a particular student
        :return: List[Subject]
        """
        # 1: raise exception if student isn't in logging state.
        if not self._student:
            raise BusinessException("Please login in first.")
        # 2: query subjects from database.
        subjects = self._subject_dao.query_subject_list_by_student_id(self.get_student().get_student_id())
        return subjects if subjects else []

    def _assign_mark_grade(self, subject: Subject):
        """
        generate a mark and assign it to subject
        :param subject:
        """
        # 1: generate a random mark
        mark = random.randint(25, 100)

        # 2: assign mark to subject
        subject.set_subject_mark(mark)

        # 3: get grade based on mark
        # mark < 50         -> Z;
        # 50 <= mark < 65   -> P;
        # 65 <= mark < 75   -> C;
        # 75 <= mark < 85   -> D;
        # mark >= 85        -> HD
        grade = "HZ" if mark >= 85 else ("D" if mark >= 75 else ("C" if mark >= 65 else ("P" if mark >= 50 else "Z")))
        subject.set_subject_grade(grade)
        self._subject_dao.update_subject(subject)

    def simulate_select_subject(self) -> str:
        subject_id = Serialization.generate_random_subject_id()
        while True:
            if not self._subject_dao.query_subject_by_student_and_subject(self.get_student().get_student_id(),
                                                                          subject_id):
                break
            subject_id = Serialization.generate_random_subject_id()
        return subject_id

from typing import List

from dao.entity.student import Student
from dao.impl.admin_dao import AdminDao
from dao.impl.student_dao import StudentDao
from dao.impl.subject_dao import SubjectDao
from util.exception import BusinessException


class AdminService:
    """
    define admin service, including:

    Fields:
        _admin_dao refers to the data access, it provides multiple CRUD operations with Student Basic information
            Note: excluding student's enrollment information

    Methods:
        _init:              public default constructor, init _subject_dao object

        enroll_subject      public method for enrollment student's subject
        remove subject      public method for removing one student's subject
        show_subjects       public method for show all subjects enrolled.
    """

    def __init__(self):
        self._admin_dao = AdminDao()
        self._student_dao = StudentDao()
        self._subject_dao = SubjectDao()

    def clear_database(self):
        """
        delete all student's information
        """
        self._admin_dao.delete_all_students_and_subjects()

    def group_students(self) -> List[str]:
        # 1: query all subjects
        subjects = self._subject_dao.query_all_subjects()
        if not subjects:
            return []

        # 2: get all student information and convert to map format
        # each Student object has 'student_id' and 'student_name' attributes
        students = self._student_dao.query_student_list()
        # Create a dictionary where the key is student_id and the value is student_name
        students_map = {student.get_student_id(): student.get_student_name() for student in students}

        # 3: Sort by _subject_grade (primary), _student_id (secondary), and _subject_mark (tertiary)
        sorted_subjects = sorted(subjects, key=lambda subj: (subj.get_subject_grade(), subj.get_student_id(),
                                                             subj.get_subject_mark()))

        # 4: format desc for each subject
        subject_desc_list = []
        for subject in sorted_subjects:
            subject_desc_list.append("{}\t-->[{}\t:: {} --> GRADE: {} - MARK: {}]"
                                     .format(subject.get_subject_grade(),
                                             students_map.get(subject.get_student_id()), subject.get_student_id(),
                                             subject.get_subject_grade(), subject.get_subject_mark()))
        return subject_desc_list

    def partition_students(self):
        # 1: query all subjects
        subjects = self._subject_dao.query_all_subjects()
        if not subjects:
            return [], []

        # 2: get all student information and convert to map format
        # each Student object has 'student_id' and 'student_name' attributes
        students = self._student_dao.query_student_list()
        # Create a dictionary where the key is student_id and the value is student_name
        students_map = {student.get_student_id(): student.get_student_name() for student in students}

        # 4: format desc for each subject
        subject_desc_list_pass = []
        subject_desc_list_fail = []
        for subject in subjects:
            temp_desc = ("{} :: {} --> GRADE: {} - MARK: {}"
                         .format(students_map.get(subject.get_student_id()), subject.get_student_id(),
                                 subject.get_subject_grade(), subject.get_subject_mark()))
            if subject.get_subject_mark() >= 50:
                subject_desc_list_pass.append(temp_desc)
            else:
                subject_desc_list_fail.append(temp_desc)
        return subject_desc_list_pass, subject_desc_list_fail

    def remove_student(self, student_id):
        """
        delete one particular student's information and all subjects
        :param student_id: student's id
        """
        # 1: check if student exists.
        student = self._student_dao.query_student_info_by_id(student_id)
        if not student:
            raise BusinessException("Student " + student_id + " does not exist.")

        # 2: delete student's all subjects from database file
        self._subject_dao.delete_subject_list_by_student_id(student_id)

        # 3: delete student's information from database file
        self._student_dao.delete_student_by_id(student_id)

    def show_all_students(self) -> List[Student]:
        students = self._student_dao.query_student_list()
        return students if students else []

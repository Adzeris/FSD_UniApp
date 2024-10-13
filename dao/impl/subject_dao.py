from typing import List

from dao.entity.subject import Subject
from dao.impl.abs_dao import AbsDao
from util.exception import PrimaryKeyDuplicationException, UniqueKeyDuplicationException


class SubjectDao(AbsDao):
    """
    Subject Data Access Object
    providing CRUD operations of subject information
        add_subject:                            add a new subject enrollment into database
        query_subject_list_by_student_id:       get a student's all subjects by using student id
        query_subject_by_student_and_subject:   get a subject enrollment by using student id and subject id
        delete_subject_by_student_and_subject:  delete a specific subject enrollment by using student id and subject id
        delete_subject_list_by_student_id:      delete a student's all subject by using student id
        update_subject:                         update a subject enrollment part information

    ** Note ** About Data Integrity:
    ->  Service layer is responsible for Data integrity, logically.
    ->  Dao layer just for CURD. don't check any data integrity
    """

    def __init__(self):
        super().__init__()

    def add_subject(self, subject):
        """
        Add a new subject enrollment information to database

        :param      subject: subject enrollment information, excluding mark and grade
        """
        # 0: check primary key and non-nullable keys
        self.raise_dao_exception_if_any_empty(student_id=subject.get_student_id(),
                                              subject_id=subject.get_subject_id())

        # 1: query subjects list
        subjects = self._database.get_subjects()

        # 2: check for none and duplicate entity
        if subjects:
            # check duplication
            self.raise_dao_exception_if_repeated(subjects, subject)

            subjects.append(subject)
        else:
            subjects = [subject]

        # 3: saving data to file
        self._database.write_subjects(subjects)

    def query_subject_count_by_student_id(self, student_id) -> int:
        subjects = self.query_subject_list_by_student_id(student_id)
        return len(subjects) if subjects else 0

    def query_all_subjects(self):
        # 1: query all subject list
        subjects = self._database.get_subjects()
        # check if subjects list is empty
        return subjects if subjects else []

    def query_subject_list_by_student_id(self, student_id) -> List[Subject]:
        """
        query all subject list of one particular student by using student id

        :param      student_id:     student's id, primary key in database
        :return:    Student or empty array (if there is no entity is related to parameter)
        """
        # 0: check non-nullable params
        self.raise_dao_exception_if_any_empty(student_id=student_id)

        # 1: query all subject list
        subjects = self._database.get_subjects()
        # check if subjects list is empty
        if not subjects:
            return []

        # 2: filter subject
        matching_subjects = [subject for subject in subjects if subject.get_student_id() == student_id]

        return matching_subjects if matching_subjects else []

    def query_subject_by_student_and_subject(self, student_id, subject_id) -> Subject | None:
        """
        query one particular enrollment information of a student's subject

        :param      student_id:     student's id, primary key in student table
        :param      subject_id:     subject id
        :return:    Subject or null (if there is no entity is related to parameter)
        """
        # 0: check non-nullable params
        self.raise_dao_exception_if_any_empty(student_id=student_id, subject_id=subject_id)

        # 1: query all subject list
        subjects = self._database.get_subjects()
        # check if subjects list is empty
        if not subjects:
            return None

        # 2: filter subject
        matching_subjects = [subject for subject in subjects if (subject.get_student_id() == student_id
                                                                 and subject.get_subject_id() == subject_id)]

        return matching_subjects[0] if matching_subjects else None

    def delete_subject_by_student_and_subject(self, student_id, subject_id):
        """
        delete one particular enrollment of a student's particular subject

        :param      student_id: student's id, primary key in database
        :param      subject_id: subject id
        """
        # 0: check non-nullable params
        self.raise_dao_exception_if_any_empty(student_id=student_id, subject_id=subject_id)

        # 1: query all subjects
        subjects = self._database.get_subjects()
        # check if students list is empty
        if not subjects:
            return

        # 2: filter subjects to deleting the data that needs to be deleted
        remain_subjects = [subject for subject in subjects if (subject.get_student_id() != student_id
                                                               or subject.get_subject_id() != subject_id)]

        # 3: saving remain students to database
        self._database.write_subjects(remain_subjects)

    def delete_subject_list_by_student_id(self, student_id):
        """
        delete all enrollments of a particular student

        :param      student_id: student's id, primary key in database
        """
        # 0: check non-nullable params
        self.raise_dao_exception_if_any_empty(student_id=student_id)

        # 1: query all subjects
        subjects = self._database.get_subjects()
        # check if students list is empty
        if not subjects:
            return

        # 2: filter subjects to deleting the data that needs to be deleted
        remain_subjects = [subject for subject in subjects if (subject.get_student_id() != student_id)]

        # 3: saving remain subjects to database
        self._database.write_subjects(remain_subjects)

    def update_subject(self, subject):
        """
        update a student's subject enrollment information by using parameter
        using delete first add after to simulate update.

        :param subject: subject enrollment information, student_id and subject_id must be included
        """
        # 0: check non-nullable params
        self.raise_dao_exception_if_any_empty(subject=subject)
        self.raise_dao_exception_if_any_empty(subject_id=subject.get_subject_id(), student_id=subject.get_student_id())

        # 1: query subjects
        subjects = self._database.get_subjects()

        # 2: remove subjects that should be deleted
        remain_subjects = [item for item in subjects if (item.get_student_id() != subject.get_student_id()
                                                         or item.get_subject_id() != subject.get_subject_id())]

        # 3: add new subject that should be added
        remain_subjects.append(subject)

        # 4: saving data to database
        self._database.write_subjects(remain_subjects)

    @staticmethod
    def raise_dao_exception_if_repeated(subjects, subject):
        for item in subjects:
            if item.get_student_id() == subject.get_student_id() and item.get_subject_id() == subject.get_subject_id():
                raise PrimaryKeyDuplicationException(
                    "Student id (" + subject.get_student_id() + ") and subject id ("
                    + subject.get_subject_id() + ") already exists.")

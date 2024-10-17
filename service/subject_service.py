import random  # Import the random module for generating random numbers
from typing import List  # Import List type for type hinting

from dao.entity.student import Student  # Import Student entity class
from dao.entity.subject import Subject  # Import Subject entity class
from dao.impl.subject_dao import SubjectDao  # Import SubjectDao for database operations
from util.constant import Constant  # Import constants used in the application
from util.exception import BusinessException  # Import custom exception for business logic errors
from util.serialization import Serialization  # Import serialization utilities for generating IDs


class SubjectService:
    """
    Defines basic student methods, including:

    Fields:
        _subject_dao: refers to the subject data access, providing CRUD operations with Subject enrollment information.

    Methods:
        __init__:              Public default constructor; initializes _subject_dao object.

        enroll_subject:        Public method for enrolling a student's subject.
        remove_subject:        Public method for removing one student's subject.
        query_subjects:       Public method for showing all subjects enrolled.
    """

    def __init__(self):
        # Initializes the SubjectDao for database operations and sets the student to None.
        self._subject_dao = SubjectDao()  # Create an instance of SubjectDao
        self._student = None  # Initialize student to None

    def set_student(self, student: Student | None):
        # Sets the current student for enrollment operations.
        self._student = student  # Assign the student to the instance variable

    def get_student(self) -> Student:
        # Returns the currently set student.
        return self._student  # Return the current student

    def enroll_subject(self) -> dict[Constant, str | int]:
        """
        Enrolls a subject.
        1. System generates subject ID automatically.
        2. After enrollment, system assigns a mark and grade automatically.
        :return: Two key-value pairs simulating return values for the front page display.
                 1. subject_id = xxxx
                 2. enrolled_amount = xxx
        """
        # 1: Raise exception if student isn't logged in.
        if not self._student:
            raise BusinessException("Please login in first.")  # Raise exception if no student is set

        # 2: Check total number of enrolled subjects.
        count = self._subject_dao.query_subject_count_by_student_id(self.get_student().get_student_id())
        if count >= 4:
            raise BusinessException("Students are allowed to enroll in 4 subjects only.")  # Limit to 4 subjects

        # 3: Generate a subject ID, which is a 3-digit number.
        subject_id = self.simulate_select_subject()  # Generate a unique subject ID

        # 4: Save subject to database.
        subject = Subject(self._student.get_student_id(), subject_id)  # Create a new Subject instance
        self._subject_dao.add_subject(subject)  # Add subject to the database

        # 5: Randomly generate a mark for this subject.
        self._assign_mark_grade(subject)  # Assign mark and grade to the subject

        # 6: Encapsulate key-value pairs for return.
        return {Constant.KEY_SUBJECT_ID: subject_id, Constant.KEY_COUNT: count + 1}  # Return subject ID and count

    def remove_subject(self, subject_id) -> dict[Constant, str | int]:
        """
        Deletes a specific subject enrollment of a particular student.
        :param subject_id: The ID of the subject to remove.
        """

        # 1: Raise exception if student isn't logged in.
        if not self._student:
            raise BusinessException("Please login in first.")  # Raise exception if no student is set

        # 2: Check whether the subject exists.
        subject = self._subject_dao.query_subject_by_student_and_subject(self.get_student().get_student_id(),
                                                                         subject_id)  # Check if subject exists
        if not subject:
            raise BusinessException("Subject-" + subject_id + " does not exist.")  # Raise exception if subject not found

        # 3: Delete the subject from the database.
        self._subject_dao.delete_subject_by_student_and_subject(self.get_student().get_student_id(), subject_id)  # Delete subject

        # 4: Encapsulate result for return.
        count = self._subject_dao.query_subject_count_by_student_id(self._student.get_student_id())  # Get updated subject count
        return {Constant.KEY_SUBJECT_ID: subject_id, Constant.KEY_COUNT: count}  # Return subject ID and updated count

    def query_subjects(self) -> List[Subject]:
        """
        Queries all subjects of a particular student.
        :return: List[Subject] - list of subjects.
        """
        # 1: Raise exception if student isn't logged in.
        if not self._student:
            raise BusinessException("Please login in first.")  # Raise exception if no student is set

        # 2: Query subjects from the database.
        subjects = self._subject_dao.query_subject_list_by_student_id(self.get_student().get_student_id())  # Get list of subjects
        return subjects if subjects else []  # Return subjects or empty list

    def _assign_mark_grade(self, subject: Subject):
        """
        Generates a mark and assigns it to the subject.
        :param subject: The subject to which the mark and grade will be assigned.
        """
        # 1: Generate a random mark.
        mark = random.randint(25, 100)  # Generate a random mark between 25 and 100

        # 2: Assign mark to the subject.
        subject.set_subject_mark(mark)  # Set the mark for the subject

        # 3: Get grade based on mark.
        # Assigns grades based on defined mark ranges.
        grade = "HD" if mark >= 85 else ("D" if mark >= 75 else ("C" if mark >= 65 else ("P" if mark >= 50 else "Z")))  # Determine grade based on mark
        subject.set_subject_grade(grade)  # Set the grade for the subject

        # 4: Update the subject in the database.
        self._subject_dao.update_subject(subject)  # Update the subject in the database

    def simulate_select_subject(self) -> str:
        """
        Simulates the selection of a subject ID that is not already taken by the student.
        :return: A unique subject ID as a string.
        """
        subject_id = Serialization.generate_random_subject_id()  # Generate a random subject ID
        while True:  # Loop until a unique subject ID is found
            # Ensure the generated subject ID is not already taken by the student.
            if not self._subject_dao.query_subject_by_student_and_subject(self.get_student().get_student_id(),
                                                                          subject_id):  # Check if the ID is already taken
                break  # Exit loop if unique ID found
            subject_id = Serialization.generate_random_subject_id()  # Generate a new ID if taken
        return subject_id  # Return the unique subject ID

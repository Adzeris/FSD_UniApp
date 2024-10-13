from dao.entity.student import Student
from dao.impl.student_dao import StudentDao
from util import util
from util.exception import BusinessException


class StudentService:
    """
    define basic student method, including:

    Fields:
        _student_dao refers to the student data access, it provides CRUD operations with Student Basic information

    Methods:
        _init:              public default constructor, init _student_dao object

        login:              public method for login (get login info from keyboard)
        register:           public method for register new student (get key information from keyboard)
        change_password     public method for change student's password

    """

    def __init__(self):
        # init _student_dao by using default constructor of StudentDao
        self._student_dao = StudentDao()
        self._student = None

    def set_student(self, student: Student | None):
        self._student = student

    def get_student(self) -> Student:
        return self._student

    def login(self, email, password) -> Student | None:
        """
        perform login process

        :param email:       student's email used as parameter to query from database.
        :param password:    student's password used for comparison if the input parameter is the same as it in database.
        :return: Student:   if student login successfully, return student object, otherwise None
        """

        # 1: query student basic information by using student_email by calling _student_dao.query_student_by_email
        student = self._student_dao.query_student_by_email(email)
        if not student:
            raise BusinessException("Student does not exist.")

        # 2: encode password of parameter, and then compare the encryption
        password_encryption = util.encode_md5(password)
        if password_encryption != student.get_student_password():
            raise BusinessException("Email or password error.")

        return student

    def register(self, email, password, name):
        """
        register by using username, email and password.
        :param name:        student's name, must be unique
        :param email:       student's email, must be unique
        :param password:    student's password, for safety, please encode it with MD5 or something like that.
        :return: None
        """

        # 1: check whether student exists or not ( eq: check if email exists )
        #    should invoke _student_dao.query_student_by_email to check whether the input email exists.
        if self._student_dao.query_student_by_email(email):
            raise BusinessException("Student " + util.get_prefix_from_email(email) + " already exists.")

        # 2: build student object
        # 2.1: using student's constructor with parameters of student_id, student_name, student_email, student_password
        #   **Note** DO NOT need to init student_category and subject_list
        #            due to system automatically assigned to with a separate process
        # 2.2: generate a encryption for password
        # 2.3: generating a student id
        # 2.4: encode password

        student_id = self.generate_student_unique_id()
        password_encryption = util.encode_md5(password)
        student = Student(student_id, name, email, password_encryption)

        # 3: invoking _student_dao.add_student to saving a new student.
        self._student_dao.add_student(student)

    def change_password(self, new_password):
        """
        used for customer to modify their password.
        """
        # 1: raise exception if student isn't in logging state.
        if not self._student:
            raise BusinessException("Please login in first.")

        # 2: encode password of parameter, and then compare the encryption
        #    call @Util.encode_md5 to get encrypted string
        new_password_encryption = util.encode_md5(new_password)

        # 2: update data to database file
        student = self._student_dao.query_student_info_by_id(self.get_student().get_student_id())
        student.set_student_password(new_password_encryption)
        self._student_dao.update_student(student)

    @staticmethod
    def check_register_params(email, password) -> bool:
        # 1: check parameters to find whether they meet the pattern requirements.
        #   please call Util.check_email_pattern to check whether email is valid.
        #   please call Util.check_password_pattern to check whether password is valid
        ret1 = util.check_email_pattern(email)
        ret2 = util.check_password_pattern(password)

        # 2 encapsulate result of combination of ret1 and ret2
        return ret1 and ret2

    def generate_student_unique_id(self):
        while True:
            student_id = util.generate_random_6_digit_number()
            if not self._student_dao.query_student_info_by_id(student_id):
                return student_id

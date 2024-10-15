import json
import os

from dao.entity.admin import Admin
from dao.entity.student import Student
from dao.entity.subject import Subject


class Database:
    """
    this is a simulation of database basis operations that include query from file and write data to file.
    Fields:
        _students           student array
        _subjects           subject enrollment array
        _data_file_path     database file
    Methods:
        __init__:       default constructor that init 3 attributes for objects storage:
                        _students, _admins, _subjects
                        **Note**:
                        @_init_file() should be called to physically init a file in disk.

        read_students:   public method for getting all students basic information.
        read_subjects:   public method for getting all subjects information.
                         **Note**:
                         @_load_file() should be called to load data from data file in disk in all getter methods.

        write_students:   public method for saving students information to database file.
        write_subjects:   public method for saving a student's all subjects information to database file.
                        **Note**:
                        @_load_file() should be called to load data from data file in disk in all getter methods.
                        @_overwrite_data should be called to physically saving data to data file in disk.

        _load_data      load data from file to memory
        _overwrite_data write data in memory into file
    """

    def __init__(self):
        """
        step 1: define 3 attributes parsed from student.data file
        """
        # _students array, show all students information
        self._students = []
        # _admins array includes all admins information
        self._admins = []
        # _enrollments array includes all students subject enrollments information
        self._subjects = []

        """
        step 2: state the file path as static and then init the file if file exists.
        """
        # current work path
        current_dir = os.getcwd()
        # project root path
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        # data file path
        self._data_file_path = os.path.join(project_root, 'file', 'student.data')

        # init file
        self._init_file()

    def _init_file(self):
        # Check if the file exists, if not, create it
        if not os.path.exists(self._data_file_path):
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(self._data_file_path), exist_ok=True)

            # Create an empty file or initialize with some content
            with open(self._data_file_path, 'w') as file:
                file.write('')  # Write an empty file or add some initial content here

    def read_students(self):
        # getter for _students
        self._load_data()
        return self._students

    def read_admins(self):
        # getter for _admins
        self._load_data()
        return self._admins

    def read_subjects(self):
        # getter for _subjects
        self._load_data()
        return self._subjects

    def write_students(self, students):
        # setter for _students

        # 1. load latest data
        self._load_data()

        # 2. process data
        self._students = students

        # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def write_admins(self, admins):
        # setter for _admins
        # 1. load latest data
        self._load_data()

        # 2. process data
        self._admins = admins

        # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def write_subjects(self, subjects):
        # setter for _subjects
        # 1. load latest data
        self._load_data()

        # # 2. process data
        self._subjects = subjects
        #
        # # 3 call overwrite method for saving data to file
        self._overwrite_data()

    def _load_data(self):
        # load data from file using JSON tools
        self._init_file()

        # step 1: load all data from student.data by using _data_file_path
        with open(self._data_file_path, 'r') as file:
            content = file.read()

        # step 2: parse json string to objects (students array, admin array, subject array)
        if content:
            data = json.loads(content)

            # step 3: assign temp objects to fields.
            self._students = [Student.from_dict(student) for student in data.get('students', [])]
            self._admins = [Admin.from_dict(admin) for admin in data.get('admins', [])]
            self._subjects = [Subject.from_dict(subject) for subject in data.get('subjects', [])]

    def _overwrite_data(self):
        # overwrite all data to student.data file
        self._init_file()

        # step 1: format objects to json string
        data = {
            "students": [student.to_dict() for student in self._students],
            "admins": [admin.to_dict() for admin in self._admins],
            "subjects": [subject.to_dict() for subject in self._subjects]
        }
        json_str = json.dumps(data, indent=4)

        # step 2: overwrite all data to file
        with open(self._data_file_path, 'w') as file:
            file.write(json_str)

    def delete_data_file(self):
        os.remove(self._data_file_path)

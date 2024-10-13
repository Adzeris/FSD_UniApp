class Student:
    """
    Student class
    Declare the attributes and functions in Student

    Fields:
        _student_id
        _student_name
        _student_email
        _student_password
        _student_category
        _subject_list
    Methods:
        1. must override following 4 methods.
            __init__    for definition a full parameters constructor
            __str__     override for outputting the object to string
            __eq__      override for comparison two object whether they are logically the same.
                        please ensure to use @__hash__ to compare two object value
            __hash__    override for definition hash value for each object, used in __eq__ method
        2. must include traditional setter and getter methods.
            getter      for encapsulate the access to all attributes.
                        **NOTE** for better understanding encapsulation,
                        please use traditional getter, don't use property to define getter
            setter      for encapsulate the modification to all attributes.
                        **NOTE** for better understanding encapsulation,
                        please use traditional getter, don't use property to define getter
    """

    def __init__(self, student_id, student_name, student_email, student_password,
                 student_category=None, subject_list=None):
        # _student_id is the unique identifier for each student, exist as primary key in student table.
        # ** Note ** randomly generated number formatted as 6-digit value, ranging from 000001 to 999999.
        self._student_id = student_id

        # _student_name prefers to the preferred given name of a student.
        self._student_name = student_name

        # _student_email is the student's official email, three important notes:
        #   1. must be unique, and exist as key parameter to login in.
        #   2. exist as key parameter to login in
        #   3. must meet a specific pattern
        self._student_email = student_email

        # _student_password is the student's logining password (GUI and CLI), two important notes:
        #   1. must meet a specific pattern
        #   2. for password safety, it must be stored with encryption (put it simply by using md5)
        self._student_password = student_password

        # _student_category refers to if a student passes a course, if the average mark of all subjects is greater or
        # equal than 50, the student would be assigned PASS, otherwise, FAIL.
        # ** Note ** default value is ""
        self._student_category = student_category

        # _subject_list is the student's all subject list,
        # ** Note ** default value is empty array.
        self._subject_list = subject_list

    def get_student_id(self):
        # getter for _student_id
        return self._student_id

    def set_student_id(self, student_id):
        # setter for _student_id
        self._student_id = student_id

    def get_student_name(self):
        # getter for _student_name
        return self._student_name

    def set_student_name(self, student_name):
        # setter for _student_name
        self._student_name = student_name

    def get_student_email(self):
        # getter for _student_email
        return self._student_email

    def set_student_email(self, student_email):
        # setter for _student_email
        self._student_email = student_email

    def get_student_password(self):
        # getter for _student_password
        return self._student_password

    def set_student_password(self, student_password):
        # setter for _student_password
        self._student_password = student_password

    def get_student_category(self):
        # getter for _student_category
        return self._student_category

    def set_student_category(self, student_category):
        # setter for _student_category
        self._student_category = student_category

    def __eq__(self, other):
        """
        :param other:   comparative object
        :return:    True: if the hash value is equal
                    False:  if the other object is not an instance of Student class
                    or
                    if the other object's _student_id is not the same as default one's.
        """
        return isinstance(other, Student) and other.get_student_id() == self._student_id

    def __str__(self):
        """
        override the super default str method to customize an output for a specific Admin object
        :return: a shorten desc combination staff_id and staff_name
        """
        return ("{}\t:: {} --> {}"
                .format(self._student_name, self._student_id, self._student_email))

    def __hash__(self):
        """
        override the super default hash method to customize a hash value by using student_id for better understanding.
        :return: hash value of _student_id
        """
        return hash(self._student_id)

    def to_dict(self):
        return {"id": self._student_id, "name": self._student_name,
                "email": self._student_email, "password": self._student_password,
                "category": self._student_category}

    @classmethod
    def from_dict(cls, dict_data):
        return cls(dict_data['id'], dict_data['name'], dict_data['email']
                   , dict_data['password'], dict_data['category'])

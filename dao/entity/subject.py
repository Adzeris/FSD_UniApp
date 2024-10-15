class Subject:
    """
    Subject class
    Declare the attributes and functions in subject

    Fields:
        _student_id
        _subject_id
        _subject_grade
        _subject_mark

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
        3. must include two method to convert between json string to object
            to_dict     Converts the Student object to a dictionary representation, for json conversion
            from_dict   Creates a Student object from a dictionary representation, for json conversion
    """

    def __init__(self, student_id, subject_id, subject_mark=None, subject_grade=None):
        # _student_id is an attribute of Student class, exist as part of composite primary key of Subject table.
        self._student_id = student_id

        # _subject_id is an attribute of Subject class, exist as part of composite primary key of Subject table.
        # one student can enroll at most 4 subjects.
        self._subject_id = subject_id

        # _subject_mark is randomly generated to each enrolled subject, ranging from 25 to 100
        self._subject_mark = subject_mark

        # _subject_grade is calculated automatically based on the mark in UTS Grading System.
        # mark < 50         -> Z;
        # 50 <= mark < 65   -> P;
        # 65 <= mark < 75   -> C;
        # 75 <= mark < 85   -> D;
        # mark >= 85        -> HD
        self._subject_grade = subject_grade

    def get_student_id(self):
        # getter for _student_id
        return self._student_id

    def set_student_id(self, student_id):
        # setter of student_id
        self._student_id = student_id

    def get_subject_id(self):
        # getter of _subject_id
        return self._subject_id

    def set_subject_id(self, subject_id):
        # setter of _subject_id
        self._subject_id = subject_id

    def get_subject_mark(self):
        # getter of _subject_mark
        return self._subject_mark

    def set_subject_mark(self, subject_mark):
        # setter of _subject_mark
        self._subject_mark = subject_mark

    def get_subject_grade(self):
        # getter of _subject_grade
        return self._subject_grade

    def set_subject_grade(self, subject_grade):
        # setter of _subject_grade
        self._subject_grade = subject_grade

    def __eq__(self, other):
        """
        :param  other:   comparative object
        :return:
            True:   if the hash value is equal
            False:  if the other object is not an instance of subject class
                    or
                    if the other object's combination of_subject_id and _student_id is not the same.
        """
        return (isinstance(other, Subject) and other.get_subject_id() == self._subject_id
                and other.get_student_id() == self._student_id)

    def __str__(self):
        """
        override the super default str method to customize an output for a specific subject object
        :return: a shorten desc combination of all attributes.
        """
        return ("[ Subject::{} -- mark = {} -- grade = {} ]"
                .format(self._subject_id, self._subject_mark, self._subject_grade))

    def __hash__(self):
        """
        override the super default hash method to customize a hash value by using student_id and subject_id.
        :return: hash value of _student_id + _subject_id
        """
        return hash(self._student_id + self._subject_id)

    def to_dict(self):
        return {"student_id": self._student_id, "subject_id": self._subject_id,
                "mark": self._subject_mark, "grade": self._subject_grade}

    @classmethod
    def from_dict(cls, dict_data):
        return cls(dict_data['student_id'], dict_data['subject_id'], dict_data['mark'], dict_data['grade'])

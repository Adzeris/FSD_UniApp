class Admin:
    """
    Admin class
    Declare the attributes and functions in Admin

    Fields:
        _staff_id
        _staff_name
        _staff_email
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
        3. must include two special method for JSON transmission
            to_dict
            from_dict
    """

    def __init__(self, staff_id, staff_name, staff_email):
        # _staff_id is the unique identifier for each staff, exist as primary key of admin table
        self._staff_id = staff_id
        # _staff_name is the staff preferred given name.
        self._staff_name = staff_name
        # _staff_email is the staff formal email
        self._staff_email = staff_email

    def get_staff_id(self):
        # getter for staff_id
        return self._staff_id

    def set_staff_id(self, staff_id):
        # setter for staff_id
        self._staff_id = staff_id

    def get_staff_name(self):
        # getter of staff_name
        return self._staff_name

    def set_staff_name(self, staff_name):
        # setter of staff_name
        self._staff_name = staff_name

    def get_staff_email(self):
        # getter of staff_email
        return self._staff_email

    def set_staff_email(self, staff_email):
        # setter of staff_email
        self._staff_email = staff_email

    def __eq__(self, other):
        """
        :param other:   comparative object
        :return:    True: if the hash value is equal
                    False:  if the other object is not an instance of Admin class
                    or
                    if the other object's _staff_id is not the same as default one's.
        """
        return isinstance(other, Admin) and other.get_staff_id() == self._staff_id

    def __str__(self):
        """
        override the super default str method to customize an output for a specific Admin object
        :return: a shorten desc combination staff_id and staff_name
        """
        return "staffId: {}, \t staffName: {}".format(self._staff_id, self._staff_name)

    def __hash__(self):
        """
        override the super default hash method to customize a hash value by using staff_id for better understanding.
        :return: hash value of subject_id
        """
        return hash(self._staff_id)

    def to_dict(self):
        return {"id": self._staff_id, "name": self._staff_name, "email": self._staff_email}

    @classmethod
    def from_dict(cls, dict_data):
        return cls(dict_data['id'], dict_data['name'], dict_data['email'])






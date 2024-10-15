import re


class Validation:

    @staticmethod
    def is_any_empty(self, *params):
        """if any param is empty，raise data access exception，and show them"""
        empty_params = [key for key, value in params if Validation.is_empty(value)]
        return empty_params

    @staticmethod
    def is_all_empty(self, *params):
        """if all params are empty，raise data access exception，and show them all"""
        return all(Validation.is_empty(value) for value in params)

    @staticmethod
    def is_empty(param) -> bool:
        """check single param if it is empty"""
        return param is None or param == ""

    @staticmethod
    def check_email_pattern(email) -> bool:
        """
        emails should end with the domain “@university.com”,
        hence firstname.lastname@university.com is a valid email,
        while firstname.lastname@university is not

        :param email
        :return:    True: meet pattern
                    False(default value): don't meet pattern
        """
        if email.endswith("@university.com"):
            return True
        else:
            return False

    @staticmethod
    def check_password_pattern(password) -> bool:
        """
        A password is considered valid if it meets the following criteria:
            (i) It starts with an upper-case character,
            (ii) It contains at least five (5) letters,
            (iii) It is followed by three (3) or more digits.
        :param password
        :return: True:  meet pattern
                 False: don't meet pattern
        """
        # Regular expression pattern
        pattern = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'

        # Use regular expression to match the password
        if re.match(pattern, password):
            return True
        else:
            return False

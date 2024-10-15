import unittest

from util.encryption import Encryption
from util.print_util import PrintUtil
from util.serialization import Serialization
from util.validation import Validation
import re


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.encryption = Encryption()
        self.print_util = PrintUtil()
        self.serialization = Serialization()
        self.validation = Validation()

    def test_encryption_encode_md5(self):
        encode_password = self.encryption.encode_md5("my_test_password")
        print(encode_password)
        # check the length for MD5 result: 32
        self.assertEqual(len(encode_password), 32)

        # Check if the string is a hexadecimal string (contains only 0-9 and a-f).
        hex_pattern = re.compile(r'^[0-9a-fA-F]{32}$')
        self.assertRegex(encode_password, hex_pattern)

    def test_serialization_generate_random_6_digit_number(self):
        student_id = self.serialization.generate_random_6_digit_number()

        # Check if student_id is a 6-digit number
        self.assertTrue(student_id.isdigit())  # Verify if all characters are digits
        self.assertEqual(len(student_id), 6)  # Verify if the length is 6

    def test_serialization_generate_random_subject_id(self):
        subject_id = self.serialization.generate_random_subject_id()

        # Check if student_id is a 3-digit number
        self.assertTrue(subject_id.isdigit())  # Verify if all characters are digits
        self.assertEqual(len(subject_id), 3)  # Verify if the length is 3

    def test_validation_is_empty(self):
        res = self.validation.is_empty("")
        self.assertTrue(res)

        res = self.validation.is_empty("aaaa")
        self.assertFalse(res)

        res = self.validation.check_email_pattern("tony@uni.com")
        self.assertFalse(res)

        res = self.validation.check_email_pattern("tony@university.com")
        self.assertTrue(res)

        res = self.validation.check_password_pattern("aaaa")
        self.assertFalse(res)

        res = self.validation.check_password_pattern("Aaaaaa123")
        self.assertTrue(res)

    def test_print(self):
        self.print_util.print_blue("This is blue")
        self.print_util.print_green("This is green")
        self.print_util.print_yellow("This is yellow")
        self.print_util.print_red("This is red")


if __name__ == '__main__':
    unittest.main()

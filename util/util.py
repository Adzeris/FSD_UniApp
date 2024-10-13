import json
import re
import hashlib
import random

def is_any_empty(self, *params):
    """if any param is empty，raise data access exception，and show them"""
    empty_params = [key for key, value in params if is_empty(value)]
    return empty_params


def is_all_empty(self, *params):
    """if all params are empty，raise data access exception，and show them all"""
    return all(is_empty(value) for value in params)


def is_empty(param) -> bool:
    """check single param if it is empty"""
    return param is None or param == ""


def check_email_pattern(email) -> bool:
    """
    emails should end with the domain “@university.com”,
    hence firstname.lastname@university.com is a valid email,
    while firstname.lastname@university is not

    :param email
    :return:    True: meet pattern
                False(default value): don't meet pattern
    """
    # if email.endswith("@university.com"):
    #     return True
    # else:
    #     return False
    return True


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

    # # Use regular expression to match the password
    # if re.match(pattern, password):
    #     return True
    # else:
    #     return False
    return True


def encode_md5(content) -> str:
    """
    Encode content using MD5.

    :param content: Text-based content to be encoded
    :return: MD5 hex hash value with 32-digit value.
    """
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the content
    md5_hash.update(content.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    md5_value = md5_hash.hexdigest()

    return md5_value


def get_prefix_from_email(email):
    if '@' in email:
        prefix, domain = email.split('@', 1)
        return prefix
    else:
        return None


def generate_random_6_digit_number():
    # Generate a random integer between 1 and 999999
    number = random.randint(1, 999999)

    # Format the number as a 6-digit string, padding with leading zeros if necessary
    formatted_number = f"{number:06d}"

    return formatted_number


def generate_random_subject() -> str:
    """
    generate a 3-digit number as a subject id
    :return:
    """
    number = random.randint(1, 999)

    # Format the number as a 6-digit string, padding with leading zeros if necessary
    formatted_number = f"{number:03d}"

    return str(formatted_number)


def print_red(content):
    red = '\033[91m'
    reset = '\033[0m'
    print(f"{red}{content}{reset}")


def print_white(content):
    white = '\033[97m'  # White text
    reset = '\033[0m'
    print(f"{white}{content}{reset}")


def print_green(content):
    green = '\033[92m'  # White text
    reset = '\033[0m'
    print(f"{green}{content}{reset}")


def print_yellow(content):
    yellow = '\033[93m'  # White text
    reset = '\033[0m'
    print(f"{yellow}{content}{reset}")


def print_blue(content):
    blue = '\033[94m'  # White text
    reset = '\033[0m'
    print(f"{blue}{content}{reset}")


def input_cyan(content):
    light_blue = '\033[96m'  # ANSI escape code for light blue/cyan
    reset = '\033[0m'  # Reset to default color
    return input(f"{light_blue}{content}{reset}")




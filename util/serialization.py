import random


class Serialization:

    @staticmethod
    def generate_random_6_digit_number():
        # Generate a random integer between 1 and 999999
        number = random.randint(1, 999999)

        # Format the number as a 6-digit string, padding with leading zeros if necessary
        formatted_number = f"{number:06d}"

        return formatted_number

    @staticmethod
    def generate_random_subject_id() -> str:
        """
        generate a 3-digit number as a subject id
        :return:
        """
        number = random.randint(1, 999)

        # Format the number as a 6-digit string, padding with leading zeros if necessary
        formatted_number = f"{number:03d}"

        return str(formatted_number)

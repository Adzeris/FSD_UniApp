import hashlib


class Encryption:

    @staticmethod
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

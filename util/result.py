from enum import Enum, auto


class Result(Enum):
    # type 1: successful code and message
    SUCCESS = "success"

    # type 2: failure code
    INPUT_ERROR = "input error"

    # type 9:
    EXCEPTION = "exception"

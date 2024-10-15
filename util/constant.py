class Constant:
    # define general constant class to store static value

    # type 1: KEYs for return map in service layer
    KEY_SUBJECT_ID = "subject_id"
    KEY_COUNT = "key_count"

    # Type 2: menu options
    # -----2.1 : Main options
    ADMIN = 'a'
    STUDENT = "s"
    EXIT = 'x'
    # -----2.2: Admin options
    A_CLEARING = "c"
    A_GROUPING = "g"
    A_PARTITION = "p"
    A_REMOVING = 'r'
    A_SHOW_ALL = 's'

    # -----2.3: Student options
    S_CHANGE_PASSWORD = 'c'
    S_ENROLLING = 'e'
    S_REMOVING = 'r'
    S_SHOW = 's'

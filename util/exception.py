class DataAccessException(Exception):
    """
    customised data access layer exception
    """
    pass


class PrimaryKeyDuplicationException(DataAccessException):
    """
    customised data access layer exception
    raise this exception if add*** method are called with same primary key
    """
    pass


class UniqueKeyDuplicationException(DataAccessException):
    """
    customised data access layer exception
    raise this exception if add method, update method are called with same unique key
    """
    pass


class BusinessException(Exception):
    """
    customised service exception
    """
    pass

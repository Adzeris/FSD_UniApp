from dao.database.database import Database
from util import util
from util.exception import DataAccessException


class AbsDao:
    """
    Define an abstract class as super class to all other dao class.
    Providing a common field: _database that includes all data file operations.
    Providing some basic method:
        raise_exception_if_any_empty    if any param is empty，raise data access exception
        raise_exception_if_all_empty    if all params are empty，raise data access exception
        is_empty                        check single param if it is empty
    """

    def __init__(self):
        self._database = Database()

    @staticmethod
    def raise_dao_exception_if_any_empty(**params):
        """if any param is empty，raise data access exception，and show them"""
        empty_params = [key for key, value in params.items() if util.is_empty(value)]
        if empty_params:
            raise DataAccessException(f"some params are empty: {', '.join(empty_params)}, please check and try again.")

    @staticmethod
    def raise_dao_exception_if_all_empty(**params):
        """if all params are empty，raise data access exception，and show them all"""
        if all(util.is_empty(value) for value in params.values()):
            raise DataAccessException(f"all params are empty: {', '.join(params.keys())}, please check and try again.")

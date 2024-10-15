from dao.database.database import Database
from dao.entity.admin import Admin
from dao.impl.abs_dao import AbsDao
from util.exception import DataAccessException


class AdminDao(AbsDao):
    """
    ADMIN Data Access Object
    providing basic query methods:
    Methods:
        query_admin_by_staff_id
        query_admin_by_staff_name
    """

    def __init__(self):
        super().__init__()

    def query_admin_by_staff_id(self, staff_id) -> Admin:
        """
        reserved method, don't need to implement.
        :param staff_id:  staff_id
        :return: Admin
        """
        admins = self._database.read_admins()
        matching_admins = [admin for admin in admins if admin.get_staff_id() == staff_id]
        return matching_admins[0] if matching_admins else None

    def query_admin_by_staff_name(self, staff_name) -> Admin:
        """
        reserved method, don't need to implement.
        :param staff_name: staff name
        :return: Admin
        """
        admins = self._database.read_admins()
        matching_admins = [admin for admin in admins if admin.get_staff_name() == staff_name]
        return matching_admins[0] if matching_admins else None

    def delete_all_students_and_subjects(self):
        try:
            self._database.delete_data_file()
        except Exception as e:
            raise DataAccessException(str(e))

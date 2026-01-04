from data.user import User


class UserFactory:

    @staticmethod
    def admin():
        return User(username="standard_user", password="secret_sauce", role="admin")

    @staticmethod
    def locked():
        return User(username="locked_out_user", password="secret_sauce", role="locked")

    @staticmethod
    def empty_password():
        return User(username="standard_user", password="", role="no_pass")

    @staticmethod
    def empty_username():
        return User(username="", password="secret_sauce", role="no_user")

    @staticmethod
    def wrong_username():
        return User(username="Standard_user", password="secret_sauce", role="non_corresponding_user")

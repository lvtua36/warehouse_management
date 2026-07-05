from app.repositories.user_repository import UserRepository

from app.utils.password import Password

class AuthService:

    @staticmethod
    def login(username,password):

        user = UserRepository.find_by_username(username)

        if user is None:

            return None

        if user["status"] == 0:

            return None

        if not Password.verify(
            password,
            user["password"]
        ):

            return None

        return user
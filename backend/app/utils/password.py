from app.extensions import bcrypt

class Password:

    @staticmethod
    def hash(password):

        return bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

    @staticmethod
    def verify(password, password_hash):

        return bcrypt.check_password_hash(
            password_hash,
            password
        )
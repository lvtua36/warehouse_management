from app.database import Database

class UserRepository:

    @staticmethod
    def get_all():

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                        SELECT

                            u.id,
                            u.full_name,
                            u.username,
                            u.email,
                            u.phone,
                            u.status,
                            r.name AS role_name

                        FROM users u

                        LEFT JOIN roles r
                            ON u.role_id = r.id

                        ORDER BY u.id
                    """

                cursor.execute(sql)

                return cursor.fetchall()

        finally:

            connection.close()

    @staticmethod
    def find_by_username(username):

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "select * from users where username=%s limit 1"

                cursor.execute(sql , (username, ))
                return cursor.fetchone()

        finally:
            connection.close()
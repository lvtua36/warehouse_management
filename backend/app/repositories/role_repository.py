from app.database import Database

class RoleRepository:

    @staticmethod
    def get_all():

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:

                sql = "select * from roles"

                cursor.execute(sql)

                return cursor.fetchall()

        finally:

            connection.close()

    @staticmethod
    def find_by_id(role_id):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "select * from roles where id=%s"

                cursor.execute(sql, (role_id,))
                return cursor.fetchone()

        finally:
            connection.close()

    @staticmethod
    def create(name, description):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:

                sql = "insert into roles (name, description) values (%s, %s)"

                cursor.execute(
                    sql,
                    (
                         name,
                        description
                    )
                )

        finally:
            connection.close()

    @staticmethod
    def update(role_id, name, description):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "update roles set name=%s, description=%s where id=%s"

                cursor.execute(
                    sql,
                    (
                        name,
                        description,
                        role_id
                    )
                )
        finally:
            connection.close()

    @staticmethod
    def delete(role_id):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "delete from roles where id=%s"

                cursor.execute(
                    sql,
                    (role_id,)
                )

        finally:
            connection.close()


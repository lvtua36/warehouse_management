from app.database import Database

class PermissionRepository:

    @staticmethod
    def get_all():

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM permissions order by id"

                cursor.execute(sql)

                return cursor.fetchall()

        finally:
            connection.close()

    @staticmethod
    def find_by_id(permission_id):

        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM permissions where id = %s"
                cursor.execute(sql, (permission_id,))
                return cursor.fetchone()

        finally:
            connection.close()

    @staticmethod
    def create(code, name, module, description):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO permissions (code, name, module, description) VALUES (%s, %s, %s, %s)"
                cursor.execute(
                    sql,
                    (
                        code,
                        name,
                        module,
                        description,
                        code
                    )
                )

            connection.commit()

        finally:
            connection.close()

    @staticmethod
    def update(permission_id, code, name, module, description):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "update permissions set code = %s, name = %s, module = %s, description = %s where id = %s"
                cursor.execute(
                    sql,
                    (
                        code,
                        name,
                        module,
                        description,
                        permission_id
                    )
                )
            connection.commit()

        finally:
            connection.close()

    @staticmethod
    def delete(permission_id):
        connection = Database.get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "delete from permissions where id = %s"

                cursor.execute(sql, (permission_id,))

            connection.commit()

        finally:
            connection.close()
from app.database import Database

conn = Database.get_connection()

print("Kết nối thành công!")

conn.close()
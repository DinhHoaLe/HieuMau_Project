import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()
# Thông tin kết nối
drive = os.getenv('SQL_SERVER_DRIVER')
server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

# Chuỗi kết nối
str_sql = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(drive, server, database, username, password)


class DatabaseConnection:
    def __init__(self):
        try:
            # Kết nối đến cơ sở dữ liệu
            self.cnxn = pyodbc.connect(str_sql)
            print("Kết nối thành công!")
            self.cursor = self.cnxn.cursor()
        except Exception as e:
            print(f"Lỗi kết nối: {e}")
            self.cursor = None

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            return None  # Trả về None cho INSERT, UPDATE, DELETE
        except Exception as e:
            print(f"❌ Lỗi khi thực thi truy vấn: {e}")
            raise

    def commit(self):
        try:
            self.cnxn.commit()
        except Exception as e:
            print(f"Lỗi khi commit: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.cnxn.close()
        except Exception as e:
            print(f"Lỗi khi đóng kết nối: {e}")

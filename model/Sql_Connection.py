import pyodbc

# Thông tin kết nối
drive = 'SQL Server'
server = 'LAPTOP-DVN34OKL'
database = 'BloodBank_db'
username = 'sa'
password = '1'

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
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Lỗi khi thực thi truy vấn: {e}")
            return []

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

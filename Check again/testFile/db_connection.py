import pyodbc

# Thông tin cấu hình kết nối cơ sở dữ liệu
DB_CONFIG = {
    'dsn': 'MySQLServer',  # Tên DSN đã cấu hình trong ODBC Data Source Administrator
    'username': 'huynhnhi',  # Tên đăng nhập
    'password': 'admin',  # Mật khẩu
    'database': 'BloodBank_db'  # Tên cơ sở dữ liệu
}

class Database:
    def __init__(self, config):
        self.dsn = config['dsn']
        self.user = config['username']
        self.password = config['password']
        self.database = config['database']
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Kết nối đến cơ sở dữ liệu
            self.connection = pyodbc.connect(f'DSN={self.dsn};UID={self.user};PWD={self.password};DATABASE={self.database}')
            self.cursor = self.connection.cursor()
            print("Kết nối thành công!")
        except pyodbc.Error as e:
            print(f"Lỗi kết nối: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)  # Truyền tham số vào câu truy vấn
            else:
                self.cursor.execute(query)  # Truy vấn không có tham số
            return self.cursor.fetchall()  # Trả về kết quả truy vấn
        except pyodbc.Error as e:
            print(f"Lỗi truy vấn: {e}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
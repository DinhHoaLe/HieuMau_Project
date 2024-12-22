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
            self.connection = pyodbc.connect(f'DSN={self.dsn};UID={self.user};PWD={self.password};DATABASE={self.database}')
            self.cursor = self.connection.cursor()
            print("Kết nối thành công!")
        except pyodbc.Error as e:
            print(f"Lỗi kết nối: {e}")
            raise

    def is_connected(self):
        try:
            self.connection.cursor()
            return True
        except (pyodbc.InterfaceError, pyodbc.ProgrammingError):
            return False

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Lỗi truy vấn: {e}")
            return None

    def execute_non_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Thao tác thành công!")
        except pyodbc.Error as e:
            print(f"Lỗi khi thực hiện thao tác: {e}")
            self.connection.rollback()

    def query_as_dict(self, query, params=None):
        try:
            self.execute_query(query, params)
            columns = [column[0] for column in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except pyodbc.Error as e:
            print(f"Lỗi truy vấn: {e}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
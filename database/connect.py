import pyodbc

# Chuỗi kết nối
server = 'SERVER_NAME'  # Tên hoặc địa chỉ IP của server
database = 'DATABASE_NAME'  # Tên database
username = 'USERNAME'  # Tên người dùng
password = 'PASSWORD'  # Mật khẩu

# Tạo kết nối
connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

# Tạo con trỏ để thực thi các lệnh SQL
cursor = connection.cursor()

# Truy vấn ví dụ
cursor.execute("SELECT TOP 10 * FROM YourTableName")
rows = cursor.fetchall()

# Hiển thị kết quả
for row in rows:
    print(row)

# Đóng kết nối
connection.close()

# Sử dụng db_connection.py
from db_connection import Database, DB_CONFIG

# Khởi tạo đối tượng Database với cấu hình từ DB_CONFIG
db = Database(DB_CONFIG)

# Kết nối tới cơ sở dữ liệu
db.connect()

# Ví dụ thực hiện truy vấn
query = "SELECT * FROM Users"
results = db.execute_query(query)

# Hiển thị kết quả
for row in results:
    print(row)

# Đóng kết nối
db.close()

import pyodbc  # Lệnh cài đặt thư viện: pip install pyodbc

# Thông tin kết nối
drive = 'SQL Server'
server = 'LAPTOP-DVN34OKL'
database = 'BloodBank_db'
username = 'sa'
password = '1'

# Chuỗi kết nối
str_sql = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(drive, server, database, username, password)

# Test Truy vấn SQL
SQL_TEST = "SELECT * FROM PATIENTS"

try:
    # Kết nối đến cơ sở dữ liệu
    cnxn = pyodbc.connect(str_sql)
    print("Kết nối thành công!")

    # Tạo cursor và thực thi truy vấn
    cursor = cnxn.cursor()
    cursor.execute(SQL_TEST)  # Thực thi câu lệnh SQL

    # Lấy kết quả và in ra
    print("Kết quả của test truy vấn lấy thông tin của bệnh nhân là:")
    rows = cursor.fetchall()  # Dùng fetchall() để lấy tất cả các dòng
    for row in rows:
        print(row)  # In mỗi dòng kết quả

    # Đóng kết nối
    cursor.close()
    cnxn.close()

except Exception as e:
    print(f"Lỗi kết nối: {e}")

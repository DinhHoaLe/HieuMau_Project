class UserModel:
    def __init__(self, db):
        """Khởi tạo UserModel với đối tượng kết nối được truyền vào."""
        self.db = db

    def login(self, username, password):
        """Kiểm tra thông tin đăng nhập."""
        query = "SELECT * FROM Users WHERE username = ? AND password = ?"
        params = (username, password)
        result = self.db.execute_query(query, params)
        return result  # Trả về kết quả từ cơ sở dữ liệu

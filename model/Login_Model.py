from model.Sql_Connection_Hoa import DatabaseConnection


class LoginModel:
    def __init__(self):
        self.db = DatabaseConnection()

    def login(self, username, password):
        """Kiểm tra thông tin đăng nhập."""
        print(username, password)
        query = "SELECT * FROM Users WHERE username = ? AND password = ?"
        params = (username, password)
        result = self.db.execute_query(query, params)
        return result  # Trả về kết quả từ cơ sở dữ liệu

from model.Login_Model import LoginModel
from db_connection import Database, DB_CONFIG


class LoginController:
    def __init__(self):
        """Khởi tạo UserController và kết nối đến cơ sở dữ liệu."""
        self.db = Database(DB_CONFIG)
        self.db.connect()
        self.user_model = LoginModel(self.db)  # Truyền kết nối vào model

    def login(self, username, password):
        """Xử lý logic đăng nhập."""
        result = self.user_model.login(username, password)
        return len(result) > 0 if result else False

    def close_db(self):
        """Đóng kết nối cơ sở dữ liệu."""
        self.db.close()

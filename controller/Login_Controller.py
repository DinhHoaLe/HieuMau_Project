from model.Login_Model import LoginModel

class UserController:
    def __init__(self):
        """Khởi tạo UserController."""
        self.user_model = LoginModel()
        print("✅ UserController đã được khởi tạo.")

    def login(self, username, password):
        """Xử lý logic đăng nhập."""
        print(f"🛠️ Xử lý đăng nhập: Username={username}, Password={password}")
        result = self.user_model.login(username, password)
        if result:
            print("✅ Đăng nhập thành công!")
            return True
        else:
            print("❌ Đăng nhập thất bại!")
            return False

    def close_db(self):
        """Đóng kết nối cơ sở dữ liệu."""
        self.user_model.close_db()
        print("✅ Kết nối cơ sở dữ liệu đã đóng.")

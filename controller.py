import tkinter as tk
from model import DashboardModel
from tkinter import messagebox
from view import DashboardView
from LogInView import LoginView


class DashboardController:
    """Controller điều khiển logic giữa Model và View."""

    def __init__(self):
        self.model = DashboardModel()  # Model quản lý dữ liệu
        self.root = tk.Tk()  # Tạo cửa sổ chính (chỉ tạo một lần)

        self.login_view = LoginView(root=self.root)  # Sử dụng cửa sổ chính cho giao diện đăng nhập
        self.dashboard_view = None  # Giao diện dashboard sẽ được khởi tạo sau khi đăng nhập thành công

        # Gán hành động cho nút đăng nhập
        self.login_view.login_button.config(command=self.handle_login)



    def handle_login(self):
        """Xử lý logic khi nhấn nút đăng nhập."""
        email = self.login_view.email_entry.get()  # Truy cập đúng vào email_entry
        password = self.login_view.password_entry.get()
        print(f"Email: {email}, Password: {password}")

        # Kiểm tra thông tin đăng nhập
        if email == "test@gmail.com" and password == "12345":
            messagebox.showinfo("Success", "Login successful!")
            self.show_dashboard()  # Chuyển sang giao diện dashboard
        else:
            messagebox.showerror("Error", "Invalid email or password!")

    def show_dashboard(self):
        """Chuyển sang giao diện Dashboard."""
        for widget in self.root.winfo_children():  # Xóa tất cả widget hiện tại
            widget.destroy()

        # Hiển thị giao diện Dashboard
        self.dashboard_view = DashboardView(self.root)

    def refresh_table(self):
        """Làm mới bảng dữ liệu trong Dashboard."""
        data = self.model.get_data()
        self.dashboard_view.populate_table(data)

    def run(self):
        """Khởi chạy ứng dụng."""
        self.root.mainloop()  # Bắt đầu vòng lặp giao diện



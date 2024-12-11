import tkinter as tk
from tkinter import messagebox


class LoginView:
    """Quản lý giao diện đăng nhập."""

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        # Tạo nhãn và entry cho email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack(pady=10)

        self.email_entry = tk.Entry(root)  # Khai báo email_entry
        self.email_entry.pack(pady=10)

        # Tạo nhãn và entry cho password
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*")  # Khai báo password_entry
        self.password_entry.pack(pady=10)

        # Tạo nút đăng nhập
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        """Hàm kiểm tra thông tin đăng nhập."""
        email = self.email_entry.get()  # Lấy thông tin từ email_entry
        password = self.password_entry.get()  # Lấy thông tin từ password_entry

        # Kiểm tra thông tin đăng nhập
        if email == "test@gmail.com" and password == "12345":
            messagebox.showinfo("Login Success", "Đăng nhập thành công!")
            self.root.destroy()  # Đóng cửa sổ đăng nhập

            # Mở dashboard sau khi đăng nhập thành công
            dashboard_root = tk.Tk()  # Tạo cửa sổ mới cho dashboard
            dashboard_root.title("Dashboard")
            dashboard_root.geometry("600x400")

            dashboard_label = tk.Label(dashboard_root, text="Welcome to the Dashboard!")
            dashboard_label.pack(pady=50)

            dashboard_root.mainloop()

        else:
            messagebox.showerror("Login Failed", "Email hoặc mật khẩu không đúng.")

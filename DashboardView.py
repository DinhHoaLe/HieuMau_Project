import tkinter as tk

class DashboardView:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("800x600")  # Đặt kích thước cửa sổ

        # Sidebar (thanh menu bên trái)
        self.sidebar = tk.Frame(root, bg="#0056b3", width=200)
        self.sidebar.pack(side="left", fill="y")

        # Thêm các nút vào sidebar
        self.menu_items = [
            ("Home", self.show_home),
            ("Donor Management", self.show_donor_management),
            ("Blood Sample Management", self.show_blood_samples),
            ("Blood Requests", self.show_blood_requests),
            ("Statistics", self.show_statistics),
            ("Logout", self.logout),
        ]

        for item in self.menu_items:
            btn = tk.Button(self.sidebar, text=item[0], bg="#0056b3", fg="white", font=("Arial", 12), relief="flat",
                            anchor="w", command=item[1])
            btn.pack(fill="x", padx=10, pady=5)

        # Main content area
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.pack(side="right", fill="both", expand=True)

        # Hiển thị nội dung mặc định trong Dashboard
        self.show_home()

    def show_home(self):
        """Hiển thị trang chính của Dashboard."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()  # Xóa các widget hiện tại

        tk.Label(self.main_frame, text="Welcome to the Admin Dashboard", font=("Arial", 16)).pack(pady=20)

    def show_donor_management(self):
        """Hiển thị giao diện quản lý người hiến máu."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Donor Management", font=("Arial", 16)).pack(pady=20)

    def show_blood_samples(self):
        """Hiển thị giao diện quản lý mẫu máu."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Blood Sample Management", font=("Arial", 16)).pack(pady=20)

    def show_blood_requests(self):
        """Hiển thị giao diện quản lý yêu cầu máu."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Blood Requests", font=("Arial", 16)).pack(pady=20)

    def show_statistics(self):
        """Hiển thị giao diện thống kê."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Statistics", font=("Arial", 16)).pack(pady=20)

    def logout(self):
        """Đăng xuất khỏi ứng dụng."""
        self.root.destroy()  # Đóng ứng dụng

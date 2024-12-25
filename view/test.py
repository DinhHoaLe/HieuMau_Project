import tkinter as tk
from tkinter import ttk


class DonorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Donor Table Example")

        # Tạo Treeview với tên cột
        columns = ("ID", "Tên Nhà Tài Trợ", "Số Tiền", "Ngày Tài Trợ")
        self.treeview = ttk.Treeview(root, columns=columns, show="headings")

        # Đặt tiêu đề cột
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Tên Nhà Tài Trợ", text="Tên Nhà Tài Trợ")
        self.treeview.heading("Số Tiền", text="Số Tiền")
        self.treeview.heading("Ngày Tài Trợ", text="Ngày Tài Trợ")

        # Đặt độ rộng cho cột
        self.treeview.column("ID", width=50, anchor="center")
        self.treeview.column("Tên Nhà Tài Trợ", width=200, anchor="w")
        self.treeview.column("Số Tiền", width=100, anchor="e")
        self.treeview.column("Ngày Tài Trợ", width=100, anchor="center")

        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Hiển thị dữ liệu ngay khi khởi chạy
        self.load_fake_data()

    def update_donor_table(self, data):
        """Cập nhật dữ liệu trong bảng"""
        print("📊 Dữ liệu nhận được từ Controller:", data)
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in data:
            print("🔎 Dòng dữ liệu đang chèn:", request)
            self.treeview.insert("", "end", values=request)

    def load_fake_data(self):
        fake_data = [
            (1, "Nguyễn Văn A", 1000, "2024-12-01"),
            (2, "Trần Thị B", 2000, "2024-12-02"),
            (3, "Lê Văn C", 1500, "2024-12-03"),
            (4, "Phạm Thị D", 3000, "2024-12-04"),
            (5, "Hoàng Văn E", 500, "2024-12-05")
        ]
        self.update_donor_table(fake_data)


# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = DonorApp(root)
    root.mainloop()

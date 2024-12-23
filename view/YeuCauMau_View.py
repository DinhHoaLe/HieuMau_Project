import tkinter as tk
from tkinter import ttk, messagebox


class BloodRequestManagementView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="white")  # Tạo Frame chính cho giao diện

    def create_request_management_frame(self):
        self.setup_search_section()
        self.setup_request_table()
        return self.frame

    def setup_search_section(self):
        """Thiết lập thanh tìm kiếm ở giữa."""
        # Frame chứa toàn bộ thanh tìm kiếm
        outer_frame = tk.Frame(self.frame, bg="#ffffff")
        outer_frame.pack(fill="x")  # Chỉ giãn ngang, bỏ expand=True

        # Frame con chứa thanh tìm kiếm
        search_frame = tk.Frame(outer_frame, bg="#f8f9fa")
        search_frame.pack(pady=5, anchor="center")  # Giảm padding dọc xuống 5

        # Label Tìm kiếm
        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="#f8f9fa")
        search_label.grid(row=0, column=0, padx=10)

        # Entry Ô nhập tìm kiếm
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60)
        self.search_entry.grid(row=0, column=1, padx=10)

        # Button Nút tìm kiếm
        search_button = tk.Button(
            search_frame,
            text="Tìm kiếm",
            command=self.search_blood_requests,
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        search_button.grid(row=0, column=2, padx=10)

    def setup_request_table(self):
        """Thiết lập bảng dữ liệu"""
        self.table_frame = tk.Frame(self.frame)  # Gắn vào self.frame
        self.table_frame.pack(pady=20, fill="both", expand=True)

        columns = (
            "Mã định danh yêu cầu",
            "Mã yêu cầu máu",
            "Mã bệnh nhân",
            "Khoa yêu cầu",
            "Nhóm máu yêu cầu",
            "Yếu tố Rh",
            "Lượng máu",
            "Ngày yêu cầu",
            "Trạng thái",
            "Ghi chú"
        )

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold"),
            background="#D3D3D3",
            foreground="black"
        )
        style.configure(
            "Treeview",
            font=("Arial", 11),
            rowheight=25
        )

        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.treeview.pack(fill="both", expand=True)

        for col in columns:
            self.treeview.heading(col, text=col)
            if col in ("Khoa yêu cầu", "Trạng thái", "Ghi chú"):
                self.treeview.column(col, width=150, anchor="w", stretch=True)
            else:
                self.treeview.column(col, width=150, anchor="center", stretch=True)

    def update_request_table(self, data):
        """Cập nhật dữ liệu trong bảng"""
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in data:
            self.treeview.insert("", "end", values=request)

    def search_blood_requests(self):
        search_term = self.search_entry.get()
        messagebox.showinfo("Tìm kiếm", f"Tìm kiếm người hiến máu với từ khóa: {search_term}")

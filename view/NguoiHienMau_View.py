import tkinter as tk
from tkinter import ttk, messagebox
import datetime

from model.NguoiHienMau_Model import DonorModel


class DonorManagementView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root, bg="white")  # Frame chính của View

        self.setup_search_section()
        self.setup_donor_table()
        self.load_donor()

        # Ràng buộc sự kiện thay đổi kích thước
        self.treeview.bind("<Configure>", self.adjust_column_width)

    def create_frame(self):
        return self.frame

    def setup_search_section(self):
        """Thiết lập thanh tìm kiếm."""
        outer_frame = tk.Frame(self.frame, bg="#ffffff")
        outer_frame.pack(fill="x")

        search_frame = tk.Frame(outer_frame, bg="#f8f9fa")
        search_frame.pack(pady=5, anchor="center")

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="#f8f9fa")
        search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60)
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(
            search_frame,
            text="Tìm kiếm",
            command=self.controller.search_donor,
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        search_button.grid(row=0, column=2, padx=10)

    def setup_donor_table(self):
        """Thiết lập bảng dữ liệu"""
        self.table_frame = tk.Frame(self.frame)
        self.table_frame.pack(pady=20, fill="both", expand=True)

        columns = (
            "Mã định danh", "Mã máu", "Họ và tên", "Sinh nhật", "Giới tính", "Nhóm máu", "Yếu tố Rh",
            "Ngày hiến gần nhất", "Điện thoại", "Địa chỉ", "Action"
        )

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#D3D3D3", foreground="black")
        style.configure("Treeview", font=("Arial", 11), rowheight=25)

        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.treeview.pack(fill="both", expand=True)

        # Cấu hình cột với chiều rộng cố định và động
        self.fixed_columns = {
            "Mã định danh": 120,
            "Mã máu": 100,
            "Sinh nhật": 100,
            "Giới tính": 80,
            "Action": 80,
            "Nhóm máu": 100,
            "Yếu tố Rh": 100,
        }
        self.dynamic_columns = [
            "Họ và tên",
            "Ngày hiến gần nhất", "Điện thoại", "Địa chỉ", "Action"
        ]

        for col in columns:
            self.treeview.heading(col, text=col)
            if col in self.fixed_columns:
                self.treeview.column(col, width=self.fixed_columns[col], anchor="center", stretch=False)
            else:
                self.treeview.column(col, width=100, anchor="center", stretch=True)

    def adjust_column_width(self, event):
        """Tự động điều chỉnh độ rộng cột khi thay đổi kích thước"""
        total_width = self.treeview.winfo_width()
        fixed_width = sum(self.fixed_columns.values())
        dynamic_columns_count = len(self.dynamic_columns)

        if dynamic_columns_count > 0 and total_width > fixed_width:
            dynamic_width = (total_width - fixed_width) // dynamic_columns_count
            for col in self.dynamic_columns:
                if col == "Địa chỉ":
                    self.treeview.column(col, width=int(dynamic_width * 1.5))  # Địa chỉ chiếm nhiều hơn
                elif col == "Ngày hiến gần nhất":
                    self.treeview.column(col, width=int(dynamic_width * 1.2))  # Ngày hiến chiếm thêm
                else:
                    self.treeview.column(col, width=dynamic_width)

    def update_donor_table(self, data):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in data:
            # Chuyển datetime.date thành chuỗi
            formatted_row = (
                request[0],  # ID
                request[1],  # Mã Nhà Tài Trợ
                request[2],  # Tên Nhà Tài Trợ
                request[3].strftime('%Y-%m-%d') if isinstance(request[3], datetime.date) else request[3],
                request[4],  # Giới Tính
                request[5],  # Nhóm Máu
                request[6],  # Rh
                request[7].strftime('%Y-%m-%d') if isinstance(request[7], datetime.date) else request[7],
                request[8],  # Số Điện Thoại
                request[9],  # Địa Chỉ
                "Xử lý"  # Dữ liệu cho Action
            )
            self.treeview.insert("", "end", values=formatted_row)

    def load_donor(self):
        data = DonorModel.get_all_donor()
        self.update_donor_table(data)

    def setup_donor_table(self):
        """Thiết lập bảng dữ liệu"""
        self.table_frame = tk.Frame(self.frame)
        self.table_frame.pack(pady=20, fill="both", expand=True)

        columns = (
            "Mã định danh", "Mã máu", "Họ và tên", "Sinh nhật", "Giới tính", "Nhóm máu", "Yếu tố Rh",
            "Ngày hiến gần nhất", "Điện thoại", "Địa chỉ", "Action"
        )

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#D3D3D3", foreground="black")
        style.configure("Treeview", font=("Arial", 11), rowheight=25)

        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.treeview.pack(fill="both", expand=True)

        self.fixed_columns = {
            "Mã định danh": 120,
            "Mã máu": 100,
            "Sinh nhật": 100,
            "Giới tính": 80,
            "Action": 100,
            "Nhóm máu": 100,
            "Yếu tố Rh": 100,
            "Điện thoại": 120,
            "Địa chỉ": 120,
            "Ngày hiến gần nhất": 120,
        }
        self.dynamic_columns = [
            "Họ và tên",

        ]

        for col in columns:
            self.treeview.heading(col, text=col)
            if col in self.fixed_columns:
                self.treeview.column(col, width=self.fixed_columns[col], anchor="center", stretch=False)
            else:
                self.treeview.column(col, width=100, anchor="center", stretch=True)

        # Ràng buộc sự kiện click vào cột "Action"
        self.treeview.bind("<Button-1>", self.on_action_click)

    def on_row_select(self, event):
        """Xử lý sự kiện chọn một dòng trong Treeview"""
        selected_item = self.treeview.selection()
        if selected_item:
            self.edit_button.config(state="normal")
            self.delete_button.config(state="normal")
            self.view_button.config(state="normal")
        else:
            self.edit_button.config(state="disabled")
            self.delete_button.config(state="disabled")
            self.view_button.config(state="disabled")

    def on_action_click(self, event):
        """Hiển thị menu khi click vào cột 'Action'"""
        region = self.treeview.identify_region(event.x, event.y)
        column = self.treeview.identify_column(event.x)
        row_id = self.treeview.identify_row(event.y)

        # Kiểm tra xem click có nằm ở cột 'Action' không
        if region == "cell" and column == f"#{len(self.treeview['columns'])}":
            if row_id:
                # Hiển thị menu
                action_menu = tk.Menu(self.root, tearoff=0)
                action_menu.add_command(label="View", command=lambda: self.show_edit_modal(row_id))
                action_menu.add_command(label="Edit", command=lambda: self.controller.edit_donor(row_id))
                action_menu.add_command(label="Delete", command=lambda: self.controller.delete_donor(row_id))
                action_menu.post(event.x_root, event.y_root)

    def show_edit_modal(self, row_id):
        """Hiển thị modal chỉnh sửa thông tin người hiến máu."""
        modal = tk.Toplevel(self.root)
        modal.title("Chỉnh sửa thông tin người hiến máu")
        modal.geometry("600x500")

        fields = ["Mã định danh", "Mã máu", "Họ và tên", "Sinh nhật", "Giới tính", "Nhóm máu", "Yếu tố Rh",
                  "Ngày hiến gần nhất", "Điện thoại", "Địa chỉ"]
        self.edit_entries = {}

        for i, field in enumerate(fields):
            tk.Label(modal, text=field, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(modal, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.edit_entries[field] = entry

        button_frame = tk.Frame(modal)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        save_button = tk.Button(button_frame, text="Lưu", command=lambda: self.controller.save_donor_edit(row_id))
        save_button.pack(side="left", padx=10)

        cancel_button = tk.Button(button_frame, text="Hủy", command=modal.destroy)
        cancel_button.pack(side="left", padx=10)

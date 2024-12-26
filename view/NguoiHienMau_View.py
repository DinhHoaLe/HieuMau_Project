import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from tkcalendar import DateEntry

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

        add_button = tk.Button(
            search_frame,
            text="Thêm",
            command=self.show_add_modal,
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        add_button.grid(row=0, column=0, padx=10)

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="#f8f9fa")
        search_label.grid(row=0, column=1, padx=10)

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

        if region == "cell" and column == f"#{len(self.treeview['columns'])}":
            if row_id:
                # Lấy giá trị DonorID từ dòng được chọn
                item = self.treeview.item(row_id)
                values = item.get('values')
                if values:
                    donor_id = values[0]  # Lấy giá trị Mã định danh (ID) từ cột đầu tiên
                    # Hiển thị menu
                    action_menu = tk.Menu(self.root, tearoff=0)
                    action_menu.add_command(label="View", command=lambda: self.show_edit_modal(donor_id))
                    action_menu.add_command(label="Edit", command=lambda: self.controller.edit_donor(donor_id))
                    action_menu.add_command(label="Delete", command=lambda: self.controller.delete_donor(self,donor_id))
                    action_menu.post(event.x_root, event.y_root)

    def show_edit_modal(self, donor_id=None):
        if donor_id is None:
            messagebox.showerror("Lỗi", "Không tìm thấy ID người hiến máu.")
            return

        # Tạo cửa sổ modal
        modal = tk.Toplevel(self.root)
        modal.title("Chỉnh sửa thông tin người hiến máu")
        modal.geometry("600x500")
        modal.resizable(False, False)
        modal.transient(self.root)  # Giữ modal trên cửa sổ chính
        modal.grab_set()  # Ngăn chặn tương tác với cửa sổ chính khi modal mở

        # Trường dữ liệu cần chỉnh sửa
        fields = [
            ("Mã định danh", "Mã định danh"),
            ("Mã máu", "Mã máu"),
            ("Họ và tên", "Họ và tên"),
            ("Sinh nhật", "Sinh nhật"),
            ("Giới tính", "Giới tính"),
            ("Nhóm máu", "Nhóm máu"),
            ("Yếu tố Rh", "Yếu tố Rh"),
            ("Ngày hiến gần nhất", "Ngày hiến gần nhất"),
            ("Điện thoại", "Điện thoại"),
            ("Địa chỉ", "Địa chỉ")
        ]
        self.edit_entries = {}

        # Lấy thông tin người hiến máu từ Controller
        donor_data = self.controller.get_info_donor(donor_id)

        if not donor_data:
            messagebox.showerror("Lỗi", f"Không tìm thấy thông tin người hiến máu với ID {donor_id}.")
            modal.destroy()
            return

        # Tạo các ô nhập liệu và điền dữ liệu ban đầu
        for i, (label, key) in enumerate(fields):
            tk.Label(modal, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(modal, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            # Chèn dữ liệu từ donor_data vào ô nhập liệu
            value = donor_data.get(key, "")
            if isinstance(value, (datetime.date, datetime.datetime)):
                value = value.strftime('%Y-%m-%d')  # Chuyển ngày thành chuỗi
            entry.insert(0, value)  # Điền giá trị vào ô nhập liệu

            self.edit_entries[key] = entry

        # Khung nút điều khiển
        button_frame = tk.Frame(modal)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        save_button = tk.Button(
            button_frame,
            text="Lưu",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.controller.update_donor(self, donor_id, self.get_edited_data())
        )
        save_button.pack(side="left", padx=10)

        cancel_button = tk.Button(
            button_frame,
            text="Hủy",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            command=modal.destroy
        )
        cancel_button.pack(side="left", padx=10)

        # modal.mainloop()

    def get_edited_data(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        edited_data = {}
        for key, entry in self.edit_entries.items():
            edited_data[key] = entry.get()
        # print("✅ Dữ liệu chỉnh sửa:", edited_data)
        return edited_data

    def show_add_modal(self):
        # Tạo cửa sổ modal
        modal = tk.Toplevel(self.root)
        modal.title("Chỉnh sửa thông tin người hiến máu")
        modal.geometry("500x400")
        modal.resizable(False, False)
        modal.transient(self.root)  # Giữ modal trên cửa sổ chính
        modal.grab_set()  # Ngăn chặn tương tác với cửa sổ chính khi modal mở

        # Danh sách các trường thông tin
        fields = [
            ("Họ và tên", "text"),
            ("Sinh nhật", "date"),
            ("Giới tính", "select_gender"),
            ("Nhóm máu", "select_blood"),
            ("Yếu tố Rh", "text"),
            ("Ngày hiến gần nhất", "date"),
            ("Điện thoại", "text"),
            ("Địa chỉ", "text")
        ]

        # Frame chứa các trường nhập liệu
        form_frame = tk.Frame(modal, padx=10, pady=10)
        form_frame.pack(fill="both", expand=True)

        # Lưu trữ các widget để xử lý sau này
        self.entries = {}

        # Tạo các nhãn và ô nhập liệu
        for i, (field_name, field_type) in enumerate(fields):
            # Nhãn
            label = tk.Label(form_frame, text=field_name, font=("Arial", 12))
            label.grid(row=i, column=0, sticky="w", pady=5)

            # Xử lý loại widget dựa trên field_type
            if field_type == "text":
                # Ô nhập liệu thông thường
                entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
                entry.grid(row=i, column=1, pady=5, padx=10)
                self.entries[field_name] = entry

            elif field_type == "date":
                # DateEntry cho ngày tháng
                entry = DateEntry(form_frame, font=("Arial", 12), width=28, date_pattern='yyyy-mm-dd')
                entry.grid(row=i, column=1, pady=5, padx=10)
                self.entries[field_name] = entry

            elif field_type == "select_gender":

                gender_var = tk.StringVar()
                gender_var.set("Chọn giới tính")  # Giá trị mặc định

                entry = ttk.OptionMenu(form_frame, gender_var, "Chọn giới tính", "F", "M")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")

                # Thêm frame phụ để căn chỉnh chiều rộng
                entry_frame = tk.Frame(form_frame)
                entry_frame.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=40)
                self.entries[field_name] = gender_var

            elif field_type == "select_blood":
                blood_var = tk.StringVar()
                blood_var.set("Chọn nhóm máu")  # Giá trị mặc định

                entry = ttk.OptionMenu(form_frame, blood_var, "Chọn nhóm máu", "A", "B", "AB", "O")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")

                entry_frame = tk.Frame(form_frame)
                entry_frame.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=40)
                self.entries[field_name] = blood_var

        # Frame chứa nút bấm
        button_frame = tk.Frame(modal, padx=10, pady=10)
        button_frame.pack(pady=10)

        # Nút lưu
        save_button = tk.Button(
            button_frame,
            text="Lưu",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.controller.add_donor(self, self.save_donor_data())
        )
        save_button.grid(row=0, column=0, padx=10)

        # Nút hủy
        cancel_button = tk.Button(
            button_frame,
            text="Hủy",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            command=modal.destroy
        )
        cancel_button.grid(row=0, column=1, padx=10)

    def save_donor_data(self):
        # Lấy dữ liệu từ các trường nhập
        donor_data = {}
        for field, widget in self.entries.items():
            if isinstance(widget, tk.StringVar):  # Dùng với OptionMenu
                donor_data[field] = widget.get()
            else:  # Dùng với Entry hoặc DateEntry
                donor_data[field] = widget.get()
        print("Dữ liệu người hiến máu:", donor_data)
        return donor_data

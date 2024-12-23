import tkinter as tk
from tkinter import ttk, messagebox


class StatisticsView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="white")  # Frame chính của View

    def create_statistics_frame(self):
        self.setup_search_section()
        self.setup_patient_table()
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
            command=self.search_donors,
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        search_button.grid(row=0, column=2, padx=10)

    def setup_patient_table(self):
        # Bảng danh sách bệnh nhân
        self.table_frame = tk.Frame(self.frame)
        self.table_frame.pack(pady=20, fill="both", expand=True)
        # Tạo thanh cuộn
        scroll_y = tk.Scrollbar(self.table_frame, orient="vertical")
        # Cập nhật danh sách cột mới
        columns = (
            "Mã bệnh nhân", "Tên bệnh nhân", "Ngày sinh", "Giới tính", "Nhóm máu", "Yếu tố RH", "Số điện thoại",
            "Địa chỉ")

        # Thiết lập style trước khi tạo Treeview
        style = ttk.Style()
        style.theme_use("clam")  # Sử dụng theme phù hợp
        style.configure(
            "Treeview.Heading",  # Style cho tiêu đề
            font=("Arial", 12, "bold"),  # Font chữ in đậm
            background="#D3D3D3",  # Màu nền tiêu đề (xanh dương)
            foreground="black"  # Màu chữ tiêu đề (trắng)
        )

        # Thiết lập font chữ và kích thước cho nội dung bảng
        style.configure(
            "Treeview",
            font=("Arial", 11),  # Kích thước chữ 11 cho các dòng trong bảng
            rowheight=25  # Chiều cao mỗi hàng
        )

        # Tạo Treeview với thanh cuộn
        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set)
        self.treeview.pack(fill="both", expand=True, side="left")

        # Gắn thanh cuộn vào Treeview
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.treeview.yview)

        # Định dạng các cột
        for col in columns:
            self.treeview.heading(col, text=col)
            if col == "Tên bệnh nhân":
                self.treeview.column(col, width=100, anchor="w")
            elif col == "Địa chỉ":
                self.treeview.column(col, width=250, anchor="w")
            else:
                self.treeview.column(col, width=60, anchor="center")

        # Hiển thị dữ liệu bệnh nhân
        self.load_patients()

    def setup_action_buttons(self):
        # Khung nút chức năng
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)

        add_button = tk.Button(button_frame, text="Thêm bệnh nhân", command=self.add_patient, font=("Arial", 12),
                               bg="#4CAF50", fg="white")
        add_button.grid(row=0, column=0, padx=10)

        edit_button = tk.Button(button_frame, text="Sửa bệnh nhân", command=self.edit_patient, font=("Arial", 12),
                                bg="#FFA500", fg="white")
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Xóa bệnh nhân", command=self.delete_patient, font=("Arial", 12),
                                  bg="#FF6347", fg="white")
        delete_button.grid(row=0, column=2, padx=10)

    def load_patients(self):
        """Tải danh sách bệnh nhân giả lập"""
        patients = [
            ("PAT001", "Nguyễn Văn A", "01/01/1990", "Nam", "A", "+", "0123456789", "Hà Nội"),
            ("PAT002", "Trần Thị B", "02/02/1985", "Nữ", "B", "-", "0987654321", "TP. Hồ Chí Minh"),
            ("PAT003", "Phạm Văn C", "03/03/1995", "Nam", "O", "+", "0912345678", "Đà Nẵng"),
            ("PAT004", "Lê Thị D", "04/04/1980", "Nữ", "AB", "-", "0945678901", "Hải Phòng"),
            ("PAT005", "Ngô Văn E", "05/05/1975", "Nam", "O", "-", "0934561234", "Huế"),
            ("PAT006", "Hoàng Thị F", "06/06/1992", "Nữ", "A", "+", "0901234567", "Quảng Ninh"),
            ("PAT001", "Nguyễn Văn A", "01/01/1990", "Nam", "A", "+", "0123456789", "Hà Nội"),
            ("PAT002", "Trần Thị B", "02/02/1985", "Nữ", "B", "-", "0987654321", "TP. Hồ Chí Minh"),
            ("PAT003", "Phạm Văn C", "03/03/1995", "Nam", "O", "+", "0912345678", "Đà Nẵng"),
            ("PAT004", "Lê Thị D", "04/04/1980", "Nữ", "AB", "-", "0945678901", "Hải Phòng"),
            ("PAT005", "Ngô Văn E", "05/05/1975", "Nam", "O", "-", "0934561234", "Huế"),
            ("PAT006", "Hoàng Thị F", "06/06/1992", "Nữ", "A", "+", "0901234567", "Quảng Ninh"),
            ("PAT001", "Nguyễn Văn A", "01/01/1990", "Nam", "A", "+", "0123456789", "Hà Nội"),
            ("PAT002", "Trần Thị B", "02/02/1985", "Nữ", "B", "-", "0987654321", "TP. Hồ Chí Minh"),
            ("PAT003", "Phạm Văn C", "03/03/1995", "Nam", "O", "+", "0912345678", "Đà Nẵng"),
            ("PAT004", "Lê Thị D", "04/04/1980", "Nữ", "AB", "-", "0945678901", "Hải Phòng"),
            ("PAT005", "Ngô Văn E", "05/05/1975", "Nam", "O", "-", "0934561234", "Huế"),
            ("PAT006", "Hoàng Thị F", "06/06/1992", "Nữ", "A", "+", "0901234567", "Quảng Ninh"),
            ("PAT001", "Nguyễn Văn A", "01/01/1990", "Nam", "A", "+", "0123456789", "Hà Nội"),
            ("PAT002", "Trần Thị B", "02/02/1985", "Nữ", "B", "-", "0987654321", "TP. Hồ Chí Minh"),
            ("PAT003", "Phạm Văn C", "03/03/1995", "Nam", "O", "+", "0912345678", "Đà Nẵng"),
            ("PAT004", "Lê Thị D", "04/04/1980", "Nữ", "AB", "-", "0945678901", "Hải Phòng"),
            ("PAT005", "Ngô Văn E", "05/05/1975", "Nam", "O", "-", "0934561234", "Huế"),
            ("PAT006", "Hoàng Thị F", "06/06/1992", "Nữ", "A", "+", "0901234567", "Quảng Ninh")
        ]
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for patient in patients:
            self.treeview.insert("", "end", values=patient)

    def search_patients(self):
        """Tìm kiếm bệnh nhân giả lập"""
        search_term = self.search_entry.get()
        # Giả lập tìm kiếm
        filtered_patients = [
            ("PAT001", "Nguyễn Văn A", "Nam", "01/01/1990", "Hà Nội", "0123456789", "email@example.com",
             "Đang điều trị") if "A" in search_term else (
                "PAT002", "Trần Thị B", "Nữ", "02/02/1985", "TP. Hồ Chí Minh", "0987654321", "b@example.com",
                "Khỏe mạnh")
        ]
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for patient in filtered_patients:
            self.treeview.insert("", "end", values=patient)

    def add_patient(self):
        """Thêm bệnh nhân giả lập"""
        messagebox.showinfo("Thêm bệnh nhân", "Chức năng thêm bệnh nhân sẽ được thực hiện tại đây!")

    def edit_patient(self):
        """Sửa bệnh nhân giả lập"""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Chọn bệnh nhân", "Vui lòng chọn bệnh nhân cần sửa!")
            return
        messagebox.showinfo("Sửa bệnh nhân", "Chức năng sửa bệnh nhân sẽ được thực hiện tại đây!")

    def delete_patient(self):
        """Xóa bệnh nhân giả lập"""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Chọn bệnh nhân", "Vui lòng chọn bệnh nhân cần xóa!")
            return
        confirmation = messagebox.askyesno("Xác nhận xóa", "Bạn có chắc muốn xóa bệnh nhân này?")
        if confirmation:
            self.load_patients()  # Cập nhật lại bảng sau khi xóa

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()

    def search_donors(self):
        search_term = self.search_entry.get()
        messagebox.showinfo("Tìm kiếm", f"Tìm kiếm người hiến máu với từ khóa: {search_term}")

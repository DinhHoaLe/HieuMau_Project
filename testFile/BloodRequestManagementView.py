import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BloodRequestManagementView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.root.title("Quản lý ngân hàng máu")
        # Thiết lập cửa sổ có kích thước 1200x700
        window_width = 1200
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.resizable(True, True)
        self.root.configure(bg="#ffffff")
        self.root.resizable(True, True)

        self.setup_header()
        self.setup_search_section()
        self.setup_request_table()
        self.setup_action_buttons()

    def setup_header(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#610a0a", height=100)
        header_frame.pack(fill="x")
        header_text = tk.Label(header_frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter", 18), fg="#ffffff", bg="#610a0a")
        header_text.pack(pady=30)
        self.setup_buttons()

    def setup_buttons(self):
        # Create the buttons frame
        buttons_frame = tk.Frame(self.root, bg="#610a0a")
        buttons_frame.pack(fill="x")  # Nút trải ngang theo cửa sổ

        # Define the button names and corresponding actions
        button_names = [
            "Quản lý yêu cầu máu",
            "Quản lý kho máu",
            "Quản lý bệnh nhân",
            "Quản lý người hiến máu",
            "Quản lý lịch hiến máu",
            "Thống kê kho máu",
        ]

        # Create buttons dynamically
        for text in button_names:
            self.create_button(buttons_frame, text, self.on_button_click)

    def create_button(self, parent, text, command):
        # Đặt màu cho nút "Quản lý yêu cầu máu"
        button_color = "#FFDD57" if text == "Quản lý yêu cầu máu" else "#d9d9d9"
    
        # Tạo nút với màu nền tương ứng
        button = tk.Button(
            parent,
            text=text,
            font=("Inter", 12, "bold"),
            fg="#000000",
            bg=button_color,  # Sử dụng màu được xác định ở trên
        command=lambda: command(text, button)
        )
        # Đặt các tham số khác cho nút
        button.pack(side="left", padx=5, pady=10, expand=True, fill="both")

    def on_button_click(self, text, button):
        print(f"Button clicked: {text}")

    def setup_search_section(self):
        # Khung tìm kiếm
        search_frame = tk.Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=20)

        # Tìm kiếm theo tên bệnh nhân
        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14))
        search_label.grid(row=0, column=0, padx=10)
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60)
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.search_blood_requests, font=("Arial", 12))
        search_button.grid(row=0, column=2, padx=10)

    def setup_request_table(self):
        # Bảng danh sách yêu cầu máu
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=20, fill="both", expand=True)
        
        # Cập nhật danh sách cột mới
        columns = ("Mã yêu cầu", "Tên bệnh nhân", "Nhóm máu", "Yếu tố Rh", "Lượng máu", "Khoa yêu cầu", "Ngày yêu cầu", "Trạng thái", "Ghi chú")
        # Thiết lập style trước khi tạo Treeview
        style = ttk.Style()
        style.theme_use("clam")  # Sử dụng theme phù hợp
        style.configure(
            "Treeview.Heading",  # Style cho tiêu đề
            font=("Arial", 12, "bold"),  # Font chữ in đậm
            background="#007BFF",       # Màu nền tiêu đề (xanh dương)
            foreground="white"          # Màu chữ tiêu đề (trắng)
        )
        # Đảm bảo không có trạng thái hover nào thay đổi màu
        style.map("Treeview.Heading", background=[])
        
        # Thiết lập font chữ và kích thước cho nội dung bảng
        style.configure(
            "Treeview",
            font=("Arial", 11),  # Kích thước chữ 11 cho các dòng trong bảng
            rowheight=25         # Chiều cao mỗi hàng
        )
        # Tạo Treeview (cột)
        
        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.treeview.pack(fill="both", expand=True)  # Đảm bảo Treeview có thể mở rộng

        # Định dạng các cột
        for col in columns:
            self.treeview.heading(col, text=col)
            # Căn lề trái cho các cột "Tên bệnh nhân", "Khoa yêu cầu" và "Ghi chú"
            if col in ("Tên bệnh nhân", "Khoa yêu cầu", "Trạng thái", "Ghi chú"):
                self.treeview.column(col, width=110, anchor="w", stretch=True)  # Căn trái
            else:
                self.treeview.column(col, width=110, anchor="center", stretch=True)  # Căn giữa cho các cột còn lại

        # Hiển thị dữ liệu yêu cầu máu
        self.load_blood_requests()

    def setup_action_buttons(self):
        # Khung nút chức năng
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)

        add_button = tk.Button(button_frame, text="Thêm yêu cầu", command=self.add_blood_request, font=("Arial", 12), bg="#4CAF50", fg="white")
        add_button.grid(row=0, column=0, padx=10)

        edit_button = tk.Button(button_frame, text="Sửa yêu cầu", command=self.edit_blood_request, font=("Arial", 12), bg="#FFA500", fg="white")
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Xóa yêu cầu", command=self.delete_blood_request, font=("Arial", 12), bg="#FF6347", fg="white")
        delete_button.grid(row=0, column=2, padx=10)

    def load_blood_requests(self):
        """Tải danh sách yêu cầu máu giả lập"""
        requests = [
            ("REQ001", "Nguyễn Văn A", "O", "+", "500ml", "Khoa A", "01/12/2024", "Đang chờ", "Không có"),
            ("REQ002", "Trần Thị B", "A", "-", "300ml", "Khoa B", "02/12/2024", "Hoàn thành", "Cần gấp"),
            ("REQ003", "Phạm Văn C", "AB", "+", "400ml", "Khoa C", "03/12/2024", "Đang chờ", "Không có"),
            ("REQ004", "Lê Thị D", "B", "-", "200ml", "Khoa D", "04/12/2024", "Hoàn thành", "Gấp"),
        ]
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in requests:
            self.treeview.insert("", "end", values=request)

    def search_blood_requests(self):
        """Tìm kiếm yêu cầu máu giả lập"""
        search_term = self.search_entry.get()
        # Giả lập tìm kiếm
        filtered_requests = [
            ("REQ001", "Nguyễn Văn A", "O", "+", "500ml", "Khoa A", "01/12/2024", "Đang chờ", "Không có") if "A" in search_term else ("REQ002", "Trần Thị B", "A", "-", "300ml", "Khoa B", "02/12/2024", "Hoàn thành", "Cần gấp")
        ]
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in filtered_requests:
            self.treeview.insert("", "end", values=request)

    def add_blood_request(self):
        """Thêm yêu cầu máu giả lập"""
        messagebox.showinfo("Thêm yêu cầu", "Chức năng thêm yêu cầu máu sẽ được thực hiện tại đây!")

    def edit_blood_request(self):
        """Sửa yêu cầu máu giả lập"""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Chọn yêu cầu", "Vui lòng chọn yêu cầu máu cần sửa!")
            return
        messagebox.showinfo("Sửa yêu cầu", "Chức năng sửa yêu cầu máu sẽ được thực hiện tại đây!")

    def delete_blood_request(self):
        """Xóa yêu cầu máu giả lập"""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Chọn yêu cầu", "Vui lòng chọn yêu cầu máu cần xóa!")
            return
        confirmation = messagebox.askyesno("Xác nhận xóa", "Bạn có chắc muốn xóa yêu cầu này?")
        if confirmation:
            self.load_blood_requests()  # Cập nhật lại bảng sau khi xóa

if __name__ == "__main__":
    root = tk.Tk()
    app = BloodRequestManagementView(root)
    root.mainloop()

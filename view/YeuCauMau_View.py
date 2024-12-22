import tkinter as tk
from tkinter import ttk, messagebox

class BloodRequestManagementView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
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

        # Thiết lập các thành phần giao diện
        self.setup_header()
        self.setup_buttons()
        self.setup_search_section()
        self.setup_request_table()

    def setup_header(self):
        header_frame = tk.Frame(self.root, bg="#610a0a", height=100)
        header_frame.pack(fill="x")
        header_text = tk.Label(header_frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter", 18), fg="#ffffff",
                               bg="#610a0a")
        header_text.pack(pady=30)

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
        search_frame = tk.Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=20)

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14))
        search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60)
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.controller.search_blood_requests,
                                  font=("Arial", 12))
        search_button.grid(row=0, column=2, padx=10)

    def setup_request_table(self):
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=20, fill="both", expand=True)

        columns = ("Mã định danh yêu cầu",
                   "Mã yêu cầu máu",
                   "Mã bệnh nhân",
                   "Khoa yêu cầu",
                   "Nhóm máu yêu cầu",
                   "Yếu tố Rh",
                   "Lượng máu",
                   "Ngày yêu cầu",
                   "Trạng thái",
                   "Ghi chú")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold"),
            background="#007BFF",
            foreground="white"
        )
        style.map("Treeview.Heading", background=[])
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

        # Đặt tiêu đề cho các cột
        for col in columns:
            self.treeview.heading(col, text=col)

    def update_request_table(self, data):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in data:
            self.treeview.insert("", "end", values=request)

    def show_message(self, message):
        messagebox.showinfo("Thông báo", message)

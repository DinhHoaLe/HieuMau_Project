import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Thêm thư viện Pillow
from controller import UserController

class LoginView:
    def __init__(self, root):
        self.root = root
        self.controller = UserController()
        self.root.title("Đăng nhập")

        # Thiết lập cửa sổ có kích thước 1200x700
        window_width = 600
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.resizable(False, False)

        # Màu nền và các cấu hình về giao diện
        background_color = "#FFFFFF"  # Màu nền trắng
        button_color = "#8B0000"  # Màu nút màu đỏ
        label_color = "#333333"  # Màu chữ đen cho nhãn
        entry_background_color = "#FFFFFF"  # Màu nền trắng cho ô nhập liệu

        # Định nghĩa bộ font cho các widget
        self.header_font = ('Arial', 18, 'bold')  # Font cho header
        self.label_font = ('Arial', 14)          # Font cho label
        self.input_font = ('Arial', 14)          # Font cho entry
        self.button_font = ('Arial', 14, 'bold') # Font cho button

        # Khung chứa form đăng nhập
        self.frame = tk.Frame(root, bg=background_color)
        self.frame.pack(expand=True, fill='both')

        # Đảm bảo các cột và hàng được phân bổ đều khi thay đổi kích thước
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=3)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_rowconfigure(5, weight=1)

        # Tạo header cho form đăng nhập
        self.label_header = tk.Label(self.frame, text="ĐĂNG NHẬP", font=self.header_font, fg="#8B0000", bg=background_color)
        self.label_header.grid(row=0, column=0, columnspan=2, pady=0, sticky='nsew')

        # Thêm hình ảnh dưới header (sử dụng Pillow để tải ảnh JPG và thay đổi kích thước)
        img_path = r"C:\Users\Admin\Desktop\logo_icon.jpg"  # Đường dẫn đến hình ảnh
        img = Image.open(img_path)

        # Thay đổi kích thước hình ảnh sao cho phù hợp (ví dụ: chiều rộng 200px, tự động điều chỉnh chiều cao)
        img_resized = img.resize((250, int(img.height * 250 / img.width)))

        self.img_login = ImageTk.PhotoImage(img_resized)  # Sử dụng ImageTk để chuyển đổi từ PIL Image sang PhotoImage
        self.label_image = tk.Label(self.frame, image=self.img_login, bg=background_color)
        self.label_image.grid(row=1, column=0, columnspan=2, pady=0)

        # Tạo label và entry cho tên người dùng
        self.label_username = tk.Label(self.frame, text="Tên người dùng:", font=self.label_font, anchor='w', fg=label_color, bg=background_color)
        self.label_username.grid(row=2, column=0, padx=40, pady=10, sticky='w')  

        self.entry_username = tk.Entry(self.frame, width=30, font=self.input_font, bg=entry_background_color, bd=2, relief="solid", )
        self.entry_username.grid(row=2, column=1, padx=40, pady=10, sticky='e') 

        # Tạo label và entry cho mật khẩu
        self.label_password = tk.Label(self.frame, text="Mật khẩu:", font=self.label_font, anchor='w', fg=label_color, bg=background_color)
        self.label_password.grid(row=3, column=0, padx=40, pady=10, sticky='w') 

        self.entry_password = tk.Entry(self.frame, show="*", width=30, font=self.input_font, bg=entry_background_color, bd=2, relief="solid")
        self.entry_password.grid(row=3, column=1, padx=40, pady=10, sticky='e') 

        # Thêm checkbox để hiển thị mật khẩu, nằm dưới ô nhập mật khẩu
        self.show_password_var = tk.BooleanVar()
        self.checkbox_show_password = tk.Checkbutton(self.frame, text="Hiển thị mật khẩu", variable=self.show_password_var, bg=background_color, command=self.toggle_password_visibility)
        self.checkbox_show_password.grid(row=4, column=1, padx=40, pady=10, sticky='e')  

        # Tạo nút đăng nhập
        self.button_login = tk.Button(self.frame, text="Đăng nhập", command=self.handle_login, width=20, font=self.button_font, bg=button_color, fg="white")
        self.button_login.grid(row=5, column=0, columnspan=2, pady=10)
        # *** Key binding cho phím Enter ***
        self.root.bind('<Return>', lambda event: self.handle_login())

    def toggle_password_visibility(self):
        """Toggle việc hiển thị mật khẩu."""
        if self.show_password_var.get():
            self.entry_password.config(show="")  # Hiển thị mật khẩu
        else:
            self.entry_password.config(show="*")  # Ẩn mật khẩu
    def handle_login(self):
        """Xử lý đăng nhập khi người dùng nhấn nút."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.controller.login(username, password):
            
            self.show_dashboard()  # Chuyển sang Dashboard
            self.frame.pack_forget() # Ẩn giao màn hình đăng nhập
        else:
            messagebox.showerror("Lỗi đăng nhập", "Tên người dùng hoặc mật khẩu không đúng!")
    def show_dashboard(self):
        """Hiển thị giao diện Dashboard sau khi đăng nhập thành công"""
        dashboard = Dashboard(self.root)
    def close(self):
        """Đóng kết nối cơ sở dữ liệu khi đóng giao diện."""
        self.controller.close_db()
class AppHeader:
    """Header component used across different views"""
    def __init__(self, root, active_button):
        self.root = root
        self.active_button = active_button
        self.setup_header()

    def setup_header(self):
        # Header frame
        self.frame = tk.Frame(self.root, bg="#610a0a", height=119)
        self.frame.pack(fill="x")

        # Header text
        header_text = tk.Label(self.frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter", 18), fg="#ffffff", bg="#610a0a")
        header_text.pack(pady=30)

        # Buttons frame
        self.setup_buttons()

    def setup_buttons(self):
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#610a0a")
        buttons_frame.pack(fill="x")

        button_names = [
            "Tổng quan",
            "Quản lý người hiến máu",
            "Quản lý kho máu",
            "Quản lý yêu cầu máu",
            "Quản lý bệnh nhân"
        ]

        for text in button_names:
            button_color = "#FFDD57" if text == self.active_button else "#d9d9d9"
            button = tk.Button(
                buttons_frame,
                text=text,
                font=("Inter", 12, "bold"),
                fg="#000000",
                bg=button_color,
                command=lambda t=text: self.on_button_click(t)
            )
            button.pack(side="left", padx=5, pady=10, expand=True, fill="both")

    def on_button_click(self, text):
        # Trước khi hiển thị màn hình mới, ẩn các màn hình hiện tại
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.frame:
                widget.pack_forget()  # Ẩn các frame hiện tại

        if text == "Quản lý yêu cầu máu":
            # Use self.frame to hide the header frame in Dashboard
            self.frame.pack_forget()  # Hide the header frame
            BloodRequestManagementView(self.root).show()
        elif text == "Tổng quan":
            print("Quản lý kho máu view placeholder")
        # Add other navigation as needed

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.root.title("Quản lý Ngân hàng Máu")

        window_width = 1200
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.resizable(True, True)
        self.root.configure(bg="#ffffff")

        # Header component
        self.header = AppHeader(self.root, "Tổng quan")  # Tạo AppHeader với nút "Thống kê kho máu" được chọn
        self.setup_content()

    def setup_content(self):
        # Tạo phần nội dung của Dashboard
        self.content_frame = tk.Frame(self.root, bg="#ffffff")
        self.content_frame.pack(fill="both", expand=True)

        label = tk.Label(self.content_frame, text="Dashboard: Thống kê kho máu", font=("Arial", 18), bg="#ffffff")
        label.pack(pady=20)

        # Add more widgets for the dashboard
    def show(self):
        # Hiển thị màn hình
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        # Ẩn màn hình
        self.frame.pack_forget()
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

        self.header = AppHeader(root, "Quản lý yêu cầu máu")
        
        self.setup_search_section()
        self.setup_request_table()
        self.setup_action_buttons()

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

    def show(self):
        self.frame.pack(fill="both", expand=True)
    def hide(self):
        self.frame.pack_forget()

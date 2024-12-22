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
        """Ẩn các màn hình hiện tại và hiển thị màn hình mới"""
        # Ẩn tất cả các frame con, trừ header
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.frame:
                widget.pack_forget()

        # Hiển thị màn hình tương ứng dựa trên lựa chọn
        new_view = None
        if text == "Quản lý yêu cầu máu":
            new_view = BloodRequestManagementView(self.root)
        elif text == "Quản lý người hiến máu":
            new_view = DonorManagementView(self.root)
        elif text == "Quản lý kho máu":
            new_view = BloodStorageManagementView(self.root)
        elif text == "Quản lý bệnh nhân":
            new_view = PatientManagementView(self.root)
        elif text == "Tổng quan":
            new_view = Dashboard(self.root)

        if new_view:
            # Ẩn frame hiện tại (header)
            self.frame.pack_forget()
            # Hiển thị màn hình mới
            new_view.show()
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
        # Tạo thanh cuộn
        scroll_y = tk.Scrollbar(self.table_frame, orient="vertical")
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
        # Tạo Treeview với thanh cuộn
        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set)
        self.treeview.pack(fill="both", expand=True, side="left")

        # Gắn thanh cuộn vào Treeview
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.treeview.yview)
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
import tkinter as tk
from tkinter import ttk, messagebox

class DonorManagementView:
    def __init__(self, root):
            self.root = root
            self.root.title("Quản lý hiến máu")
            
            # Đặt cửa sổ ở giữa màn hình
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            window_width = 1200
            window_height = 700

            position_top = int(screen_height / 2 - window_height / 2)
            position_right = int(screen_width / 2 - window_width / 2)

            self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

            # Header component
            self.header = AppHeader(root, "Quản lý người hiến máu")
            self.header.frame.pack(side="top", fill="x", pady=0)  # Đảm bảo header được đặt ở trên cùng

            # Frame chính bao bọc toàn bộ giao diện
            self.frame = tk.Frame(self.root, bg="white")
            self.frame.pack(fill="both", expand=True)

            
            # Thiết lập style cho ttk
            style = ttk.Style()
            style.theme_use("clam")  # Sử dụng theme phù hợp
            style.configure(
                "Treeview.Heading",  # Style cho tiêu đề bảng
                font=("Arial", 12, "bold"),  # Font chữ in đậm
                background="#007BFF",       # Màu nền tiêu đề (xanh dương)
                foreground="white"          # Màu chữ tiêu đề (trắng)
            )
            style.configure(
                "Treeview", 
                background="white", 
                foreground="black", 
                rowheight=25, 
                fieldbackground="white"
            )
            style.configure("TNotebook", background="white")  # Màu nền container của tab
            style.configure("TNotebook.Tab", background="white", foreground="black", font=("Arial", 12, "bold"))
            style.map(
                "TNotebook.Tab", 
                background=[("selected", "#D3D3D3")],  # Màu nền tab được chọn (vàng)
                foreground=[("selected", "black")]  # Màu chữ tab được chọn
            )
            style.configure("TButton", background="#ffffff", foreground="black", font=("Arial", 12))
            style.configure("TLabel", background="white", foreground="black", font=("Arial", 14))
            style.configure("TEntry", background="white", foreground="black", font=("Arial", 14))

            # Tạo Notebook (Tab container) trong frame chính
            self.notebook = ttk.Notebook(self.frame)
            self.notebook.pack(fill="both", expand=True)

            # Tab 1: Quản lý người hiến máu
            self.donor_management_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.donor_management_tab, text="Quản lý người hiến máu")
            self.setup_donor_management_tab()

            # Tab 2: Lịch sử hiến máu
            self.donation_history_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.donation_history_tab, text="Lịch sử hiến máu")
            self.setup_donation_history_tab()
    def setup_donor_management_tab(self):
        search_frame = tk.Frame(self.donor_management_tab, bg="white")
        search_frame.pack(pady=20)

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="white")
        search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60, bg="white", fg="black")
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.search_donors, font=("Arial", 12), bg="gray", fg="black")
        search_button.grid(row=0, column=2, padx=10)

        table_frame = tk.Frame(self.donor_management_tab, bg="white")
        table_frame.pack(pady=10, fill="both", expand=True)

        scroll_y = tk.Scrollbar(table_frame, orient="vertical")
        columns = ("Mã người hiến", "Tên người hiến", "Nhóm máu", "Yếu tố Rh", "Ngày hiến gần nhất", "Số điện thoại", "Địa chỉ")

        self.treeview = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set)
        self.treeview.pack(fill="both", expand=True, side="left")
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.treeview.yview)

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150, anchor="w")

        button_frame = tk.Frame(self.donor_management_tab, bg="white")
        button_frame.pack(pady=20)

        add_button = tk.Button(button_frame, text="Thêm người hiến", command=self.add_donor, font=("Arial", 12), bg="#4CAF50", fg="white")
        add_button.grid(row=0, column=0, padx=10)

        edit_button = tk.Button(button_frame, text="Sửa thông tin", command=self.edit_donor, font=("Arial", 12), bg="#FFA500", fg="white")
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Xóa người hiến", command=self.delete_donor, font=("Arial", 12), bg="#FF6347", fg="white")
        delete_button.grid(row=0, column=2, padx=10)

        self.load_donors()

    def setup_donation_history_tab(self):
        search_frame = tk.Frame(self.donation_history_tab, bg="white")
        search_frame.pack(pady=20)

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="white")
        search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60, bg="white", fg="black")
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.search_donors, font=("Arial", 12), bg="gray", fg="black")
        search_button.grid(row=0, column=2, padx=10)

        table_frame = tk.Frame(self.donation_history_tab, bg="white")
        table_frame.pack(pady=10, fill="both", expand=True)

        scroll_y = tk.Scrollbar(table_frame, orient="vertical")
        columns = ("Mã người hiến", "Tên người hiến", "Ngày hiến", "Nhóm máu", "Yếu tố Rh")

        self.history_treeview = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set)
        self.history_treeview.pack(fill="both", expand=True, side="left")
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.history_treeview.yview)

        for col in columns:
            self.history_treeview.heading(col, text=col)
            self.history_treeview.column(col, width=150, anchor="w")

        self.load_history()

    def load_donors(self):
        donors = [
            ("D001", "Nguyễn Văn A", "O", "+", "01/12/2024", "0123456789", "Hà Nội"),
            ("D002", "Trần Thị B", "A", "-", "15/11/2024", "0354656884", "Hải Phòng"),
        ]
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for donor in donors:
            self.treeview.insert("", "end", values=donor)

    def load_history(self):
        history = [
            ("D001", "Nguyễn Văn A", "01/12/2024", "O", "+"),
            ("D002", "Trần Thị B", "15/11/2024", "A", "-"),
        ]
        for row in self.history_treeview.get_children():
            self.history_treeview.delete(row)
        for record in history:
            self.history_treeview.insert("", "end", values=record)

    def search_donors(self):
        search_term = self.search_entry.get()
        messagebox.showinfo("Tìm kiếm", f"Tìm kiếm người hiến máu với từ khóa: {search_term}")

    def add_donor(self):
        messagebox.showinfo("Thêm người hiến máu", "Chức năng thêm người hiến máu")

    def edit_donor(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Sửa thông tin", "Vui lòng chọn người hiến máu để sửa!")
        else:
            messagebox.showinfo("Sửa thông tin", "Chức năng sửa thông tin người hiến máu")

    def delete_donor(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("Xóa người hiến máu", "Vui lòng chọn người hiến máu để xóa!")
        else:
            confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa người hiến máu này?")
            if confirm:
                messagebox.showinfo("Xóa người hiến máu", "Người hiến máu đã được xóa!")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()

class BloodStorageManagementView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.root.title("Quản lý kho máu")
        
        # Thiết lập cửa sổ
        window_width = 1200
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.resizable(True, True)
        self.root.configure(bg="#ffffff")

        self.header = AppHeader(root, "Quản lý kho máu")

        # Setup các phần
        self.setup_inventory_info_section()
        self.setup_blood_entry_section()

    def setup_inventory_info_section(self):
        """Phần thông tin tồn kho"""
        inventory_frame = tk.Frame(self.root, bg="#ffffff")
        inventory_frame.pack(pady=5, fill="x")

        inventory_label = tk.Label(inventory_frame, text="Thông tin tồn kho", font=("Arial", 16, "bold"),bg="#ffffff")
        inventory_label.pack(pady=1)

        # Tạo 8 ô vuông cho các nhóm máu
        groups = [("A", "+", 500000), ("A", "-", 400000),
                  ("B", "+", 350000), ("B", "-", 300000),
                  ("AB", "+", 200000), ("AB", "-", 150000),
                  ("O", "+", 600000), ("O", "-", 450000)]

        # Tạo frame chính để chứa các ô vuông
        row_frame = tk.Frame(inventory_frame,bg="#ffffff")
        row_frame.pack(pady=5)

        # Tạo các ô vuông cho mỗi nhóm máu và yếu tố Rh
        for i, (group, rh, stock) in enumerate(groups):
            group_frame = tk.Frame(row_frame, bg="#f2f2f2", width=150, height=150, relief="solid", borderwidth=2)
            group_frame.grid(row=0, column=i, padx=15, pady=10)  # Sử dụng grid để đặt ô vuông

            # Thêm tên nhóm máu và yếu tố Rh vào ô vuông
            group_label = tk.Label(group_frame, text=f"{group} {rh}", font=("Arial", 14, "bold"), bg="#f2f2f2")
            group_label.pack(pady=10)

            # Thêm thông tin tồn kho vào ô vuông
            stock_label = tk.Label(group_frame, text=f"Tồn: {stock} ml", font=("Arial", 12), bg="#f2f2f2")
            stock_label.pack(pady=10)
    def setup_blood_entry_section(self):
        """Phần quản lý nhập kho"""
        entry_frame = tk.Frame(self.root, bg="#ffffff")
        entry_frame.pack(pady=1, fill="x")

        entry_label = tk.Label(entry_frame, text="Quản lý nhập kho", font=("Arial", 16, "bold"), bg="#ffffff")
        entry_label.pack(pady=5)

        # Nút nhập kho
        entry_button = tk.Button(entry_frame, text="Nhập kho", command=self.show_blood_entry_popup, 
                             font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
        entry_button.pack(pady=10, padx=10, anchor="w")

        # Cấu hình bảng nhập kho
        columns = ("Mã nhập kho", "Nhóm máu", "Yếu tố Rh", "Ngày nhập", "Nguồn")

        # Tạo style cho bảng
        style = ttk.Style()
        style.theme_use("clam")  # Thay đổi theme nếu cần

        # Chỉnh màu tiêu đề
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#007BFF", foreground="white")

        # Tạo frame chứa bảng và scrollbar
        table_frame = tk.Frame(entry_frame, bg="#ffffff")
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Tạo scrollbar dọc
        scroll_y = tk.Scrollbar(table_frame, orient="vertical")

        # Tạo bảng quản lý nhập kho với scrollbar
        self.entry_treeview = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set,height=20)
    
        # Đặt scrollbar bên cạnh Treeview
        scroll_y.pack(side="right", fill="y")
        self.entry_treeview.pack(side="left", fill="both", expand=True)

        # Kết nối thanh cuộn với bảng
        scroll_y.config(command=self.entry_treeview.yview)

        # Cấu hình các cột và tiêu đề
        for col in columns:
            self.entry_treeview.heading(col, text=col)
            self.entry_treeview.column(col, width=150, anchor="center")

        # Chỉnh màu các dòng
        style.configure("Treeview", font=("Arial", 11), rowheight=25, background="#f9f9f9", foreground="black")
        style.map("Treeview", background=[("selected", "#5e9aef")], foreground=[("selected", "white")])

        # Dữ liệu giả lập
        self.load_blood_entry_info()
    def load_blood_entry_info(self):
        """Tải thông tin nhập kho giả lập"""
        entry_data = [
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z"),
            ("N001", "A", "+", "01/12/2024", "Bệnh viện X"),
            ("N002", "O", "-", "10/11/2024", "Bệnh viện Y"),
            ("N003", "B", "+", "20/10/2024", "Bệnh viện Z")
        ]

        for row in self.entry_treeview.get_children():
            self.entry_treeview.delete(row)

        for unit in entry_data:
            self.entry_treeview.insert("", "end", values=unit)
    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
    def show_blood_entry_popup(self):
        """Hiển thị popup nhập kho"""
        popup = tk.Toplevel(self.root)
        popup.title("Nhập kho")
        popup.configure(bg="#ffffff")

        # Kích thước popup
        popup_width = 400
        popup_height = 400

        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tính toán vị trí để đặt popup ở giữa màn hình
        x_coordinate = (screen_width // 2) - (popup_width // 2)
        y_coordinate = (screen_height // 2) - (popup_height // 2)

        # Cập nhật vị trí và kích thước popup
        popup.geometry(f"{popup_width}x{popup_height}+{x_coordinate}+{y_coordinate}")

        # Tiêu đề
        popup_label = tk.Label(popup, text="Nhập kho", font=("Arial", 16, "bold"), bg="#ffffff")
        popup_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Frame chứa các trường thông tin
        form_frame = tk.Frame(popup, bg="#ffffff")
        form_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Đồng bộ chiều rộng cột
        form_frame.grid_columnconfigure(1, weight=1, uniform="equal")

        # Nguồn (Radio Buttons)
        source_var = tk.StringVar(value="Người hiến máu")
        source_frame = tk.Frame(form_frame, bg="#ffffff")
        source_frame.grid(row=0, column=0, columnspan=2, pady=(5, 10), sticky="w")

        tk.Radiobutton(source_frame, text="Người hiến máu", variable=source_var, value="Người hiến máu",
                    bg="#ffffff", font=("Arial", 11), command=lambda: toggle_source("Người hiến máu")).pack(side="left", padx=5)
        tk.Radiobutton(source_frame, text="Cơ sở khác", variable=source_var, value="Cơ sở khác",
                    bg="#ffffff", font=("Arial", 11), command=lambda: toggle_source("Cơ sở khác")).pack(side="left", padx=5)

        # Người hiến máu (Label và Dropdown)
        donor_var = tk.StringVar()
        donor_frame = tk.Frame(form_frame, bg="#ffffff")
        donor_label = tk.Label(donor_frame, text="Người hiến máu:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        donor_label.grid(row=0, column=0, padx=5, pady=5)
        donor_combobox = ttk.Combobox(donor_frame, textvariable=donor_var, state="readonly", font=("Arial", 11), width=25)
        donor_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        donor_combobox["values"] = ["Nguyễn Văn A - A+", "Trần Thị B - O-", "Lê Văn C - B+"]
        donor_combobox.bind("<<ComboboxSelected>>", lambda e: on_donor_selected())

        # Tên cơ sở (Label và Entry)
        facility_var = tk.StringVar()
        facility_frame = tk.Frame(form_frame, bg="#ffffff")
        facility_label = tk.Label(facility_frame, text="Tên cơ sở:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        facility_label.grid(row=0, column=0, padx=5, pady=5)
        facility_entry = tk.Entry(facility_frame, textvariable=facility_var, font=("Arial", 11), width=27)
        facility_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Nhóm máu (Label và Dropdown)
        blood_type_var = tk.StringVar()
        blood_frame = tk.Frame(form_frame, bg="#ffffff")
        blood_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")
        blood_label = tk.Label(blood_frame, text="Nhóm máu:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        blood_label.grid(row=0, column=0, padx=5, pady=5)
        blood_combobox = ttk.Combobox(blood_frame, textvariable=blood_type_var, font=("Arial", 11), state="readonly", width=25)
        blood_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        blood_combobox["values"] = ["A", "B", "O", "AB"]

        # Yếu tố Rh (Label và Dropdown)
        rh_factor_var = tk.StringVar()
        rh_frame = tk.Frame(form_frame, bg="#ffffff")
        rh_frame.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")
        rh_label = tk.Label(rh_frame, text="Yếu tố Rh:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        rh_label.grid(row=0, column=0, padx=5, pady=5)
        rh_combobox = ttk.Combobox(rh_frame, textvariable=rh_factor_var, font=("Arial", 11), state="readonly", width=25)
        rh_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        rh_combobox["values"] = ["+", "-"]

        # Lượng máu (Label và Entry)
        quantity_var = tk.StringVar()
        quantity_frame = tk.Frame(form_frame, bg="#ffffff")
        quantity_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
        quantity_label = tk.Label(quantity_frame, text="Lượng máu (ml):", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        quantity_label.grid(row=0, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(quantity_frame, textvariable=quantity_var, font=("Arial", 11), width=27)
        quantity_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Nút xác nhận
        def submit_entry():
            if source_var.get() == "Người hiến máu" and not donor_var.get():
                messagebox.showwarning("Nhập thông tin", "Vui lòng chọn người hiến máu!")
                return
            if source_var.get() == "Cơ sở khác" and not facility_var.get():
                messagebox.showwarning("Nhập thông tin", "Vui lòng nhập tên cơ sở!")
                return
            if not blood_type_var.get() or not rh_factor_var.get() or not quantity_var.get():
                messagebox.showwarning("Nhập thông tin", "Vui lòng điền đầy đủ thông tin!")
                return
            messagebox.showinfo("Nhập kho thành công", f"Đã nhập kho thành công!\n"
                                                        f"Nhóm máu: {blood_type_var.get()} {rh_factor_var.get()}\n"
                                                        f"Lượng máu: {quantity_var.get()} ml\n"
                                                        f"Nguồn: {source_var.get()}")
            popup.destroy()

        submit_button = tk.Button(popup, text="Nhập kho", command=submit_entry, font=("Arial", 12), bg="#4CAF50", fg="white")
        submit_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Xử lý khi thay đổi nguồn
        def toggle_source(source):
            donor_var.set("")
            facility_var.set("")
            blood_type_var.set("")
            rh_factor_var.set("")
            quantity_var.set("")
            if source == "Người hiến máu":
                donor_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")
                facility_frame.grid_forget()
                blood_combobox.config(state="disabled")
                rh_combobox.config(state="disabled")
            elif source == "Cơ sở khác":
                donor_frame.grid_forget()
                facility_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")
                blood_combobox.config(state="normal")
                rh_combobox.config(state="normal")

        # Xử lý khi chọn người hiến máu
        def on_donor_selected():
            selected = donor_var.get()
            if selected == "Nguyễn Văn A - A+":
                blood_type_var.set("A")
                rh_factor_var.set("+")
            elif selected == "Trần Thị B - O-":
                blood_type_var.set("O")
                rh_factor_var.set("-")
            elif selected == "Lê Văn C - B+":
                blood_type_var.set("B")
                rh_factor_var.set("+")

        # Hiển thị khung đầu tiên (dựa trên giá trị mặc định)
        toggle_source("Người hiến máu")
class PatientManagementView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.root.title("Quản lý bệnh nhân")
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

        self.header = AppHeader(self.root, "Quản lý bệnh nhân")
        self.setup_search_section()
        self.setup_patient_table()
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

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.search_patients, font=("Arial", 12))
        search_button.grid(row=0, column=2, padx=10)

    def setup_patient_table(self):
        # Bảng danh sách bệnh nhân
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=20, fill="both", expand=True)
        # Tạo thanh cuộn
        scroll_y = tk.Scrollbar(self.table_frame, orient="vertical")
        # Cập nhật danh sách cột mới
        columns = ("Mã bệnh nhân", "Tên bệnh nhân", "Ngày sinh", "Giới tính","Nhóm máu", "Yếu tố RH", "Số điện thoại", "Địa chỉ")
        
        # Thiết lập style trước khi tạo Treeview
        style = ttk.Style()
        style.theme_use("clam")  # Sử dụng theme phù hợp
        style.configure(
            "Treeview.Heading",  # Style cho tiêu đề
            font=("Arial", 12, "bold"),  # Font chữ in đậm
            background="#007BFF",       # Màu nền tiêu đề (xanh dương)
            foreground="white"          # Màu chữ tiêu đề (trắng)
        )
        
        # Thiết lập font chữ và kích thước cho nội dung bảng
        style.configure(
            "Treeview",
            font=("Arial", 11),  # Kích thước chữ 11 cho các dòng trong bảng
            rowheight=25         # Chiều cao mỗi hàng
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

        add_button = tk.Button(button_frame, text="Thêm bệnh nhân", command=self.add_patient, font=("Arial", 12), bg="#4CAF50", fg="white")
        add_button.grid(row=0, column=0, padx=10)

        edit_button = tk.Button(button_frame, text="Sửa bệnh nhân", command=self.edit_patient, font=("Arial", 12), bg="#FFA500", fg="white")
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Xóa bệnh nhân", command=self.delete_patient, font=("Arial", 12), bg="#FF6347", fg="white")
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
            ("PAT001", "Nguyễn Văn A", "Nam", "01/01/1990", "Hà Nội", "0123456789", "email@example.com", "Đang điều trị") if "A" in search_term else ("PAT002", "Trần Thị B", "Nữ", "02/02/1985", "TP. Hồ Chí Minh", "0987654321", "b@example.com", "Khỏe mạnh")
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
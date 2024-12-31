import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Thêm thư viện Pillow


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")

        # Thiết lập cửa sổ có kích thước 800x500
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
        button_color = "#8B0000"  # Màu nút xanh lá cây
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

    def toggle_password_visibility(self):
        """Toggle việc hiển thị mật khẩu."""
        if self.show_password_var.get():
            self.entry_password.config(show="")  # Hiển thị mật khẩu
        else:
            self.entry_password.config(show="*")  # Ẩn mật khẩu
    def handle_login(self):
        """Xử lý đăng nhập khi người dùng nhấn nút đăng nhập"""
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == "admin" and password == "12345":
            messagebox.showinfo("Đăng nhập thành công", "Chào mừng đến với Ngân hàng máu!")
        else:
            messagebox.showerror("Lỗi đăng nhập", "Tên người dùng hoặc mật khẩu không đúng!")

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()

# Tạo đối tượng View và hiển thị UI
view = LoginView(root)

# Chạy ứng dụng
root.mainloop()

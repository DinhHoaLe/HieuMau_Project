import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DonorManagementView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý hiến máu")
        
        # Đặt cửa sổ ở giữa màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1200
        window_height = 700

        # Tính toán tọa độ x, y để căn giữa cửa sổ
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Đặt kích thước và vị trí cửa sổ
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Đặt màu nền cho cửa sổ chính là màu trắng
        self.root.config(bg="white")

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

        # Tạo Notebook (Tab container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1: Quản lý người hiến máu
        self.donor_management_tab = ttk.Frame(self.notebook, style="TNotebook")
        self.notebook.add(self.donor_management_tab, text="Quản lý người hiến máu")
        self.setup_donor_management_tab()

        # Tab 2: Lịch sử hiến máu
        self.donation_history_tab = ttk.Frame(self.notebook, style="TNotebook")
        self.notebook.add(self.donation_history_tab, text="Lịch sử hiến máu")
        self.setup_donation_history_tab()

    def setup_donor_management_tab(self):
        """Thiết lập giao diện Quản lý người hiến máu"""
        # Tìm kiếm
        search_frame = tk.Frame(self.donor_management_tab, bg="white")
        search_frame.pack(pady=20)

        search_label = tk.Label(search_frame, text="Tìm kiếm:", font=("Arial", 14), bg="white")
        search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=60, bg="white", fg="black")
        self.search_entry.grid(row=0, column=1, padx=10)

        search_button = tk.Button(search_frame, text="Tìm kiếm", command=self.search_donors, font=("Arial", 12), bg="gray", fg="black")
        search_button.grid(row=0, column=2, padx=10)

        # Bảng danh sách người hiến máu
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
            if col == "Tên người hiến":
                self.treeview.column(col, width=150, anchor="w")
            elif col == "Ngày hiến gần nhất":
                self.treeview.column(col, width=120, anchor="center")
            elif col == "Địa chỉ":
                self.treeview.column(col, width=250, anchor="w")
            else:
                self.treeview.column(col, width=60, anchor="center")

        # Nút chức năng
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
        """Thiết lập giao diện Lịch sử hiến máu"""
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
            self.history_treeview.column(col, anchor="w", width=150)

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
if __name__ == "__main__":
    root = tk.Tk()
    app = DonorManagementView(root)
    root.mainloop()

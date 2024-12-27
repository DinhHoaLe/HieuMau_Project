import tkinter as tk
from tkinter import ttk, messagebox


class BloodStorageView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="white")  #

    def create_blood_storage_frame(self):
        self.setup_inventory_info_section()
        self.setup_blood_entry_section()
        return self.frame

    def setup_inventory_info_section(self):
        """Phần thông tin tồn kho"""
        inventory_frame = tk.Frame(self.frame, bg="#ffffff")
        inventory_frame.pack(pady=5, fill="x")

        inventory_label = tk.Label(inventory_frame, text="Thông tin tồn kho", font=("Arial", 16, "bold"), bg="#ffffff")
        inventory_label.pack(pady=1)

        # Tạo 8 ô vuông cho các nhóm máu
        groups = [("A", "+", 500000), ("A", "-", 400000),
                  ("B", "+", 350000), ("B", "-", 300000),
                  ("AB", "+", 200000), ("AB", "-", 150000),
                  ("O", "+", 600000), ("O", "-", 450000)]

        # Tạo frame chính để chứa các ô vuông
        row_frame = tk.Frame(inventory_frame, bg="#ffffff")
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
        entry_frame = tk.Frame(self.frame, bg="#ffffff")
        entry_frame.pack(pady=1, fill="x")

        entry_label = tk.Label(entry_frame, text="Quản lý nhập kho", font=("Arial", 16, "bold"), bg="#ffffff")
        entry_label.pack(pady=5)

        # Nút nhập kho
        entry_button = tk.Button(entry_frame, text="Nhập kho", command=self.show_blood_entry_popup,
                                 font=("Arial", 12), bg="#D3D3D3", fg="white", width=20, foreground="black")
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
        self.entry_treeview = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set,
                                           height=20)

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
                       bg="#ffffff", font=("Arial", 11), command=lambda: toggle_source("Người hiến máu")).pack(
            side="left", padx=5)
        tk.Radiobutton(source_frame, text="Cơ sở khác", variable=source_var, value="Cơ sở khác",
                       bg="#ffffff", font=("Arial", 11), command=lambda: toggle_source("Cơ sở khác")).pack(side="left",
                                                                                                           padx=5)

        # Người hiến máu (Label và Dropdown)
        donor_var = tk.StringVar()
        donor_frame = tk.Frame(form_frame, bg="#ffffff")
        donor_label = tk.Label(donor_frame, text="Người hiến máu:", font=("Arial", 12), bg="#ffffff", width=15,
                               anchor="w")
        donor_label.grid(row=0, column=0, padx=5, pady=5)
        donor_combobox = ttk.Combobox(donor_frame, textvariable=donor_var, state="readonly", font=("Arial", 11),
                                      width=25)
        donor_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        donor_combobox["values"] = ["Nguyễn Văn A - A+", "Trần Thị B - O-", "Lê Văn C - B+"]
        donor_combobox.bind("<<ComboboxSelected>>", lambda e: on_donor_selected())

        # Tên cơ sở (Label và Entry)
        facility_var = tk.StringVar()
        facility_frame = tk.Frame(form_frame, bg="#ffffff")
        facility_label = tk.Label(facility_frame, text="Tên cơ sở:", font=("Arial", 12), bg="#ffffff", width=15,
                                  anchor="w")
        facility_label.grid(row=0, column=0, padx=5, pady=5)
        facility_entry = tk.Entry(facility_frame, textvariable=facility_var, font=("Arial", 11), width=27)
        facility_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Nhóm máu (Label và Dropdown)
        blood_type_var = tk.StringVar()
        blood_frame = tk.Frame(form_frame, bg="#ffffff")
        blood_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")
        blood_label = tk.Label(blood_frame, text="Nhóm máu:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        blood_label.grid(row=0, column=0, padx=5, pady=5)
        blood_combobox = ttk.Combobox(blood_frame, textvariable=blood_type_var, font=("Arial", 11), state="readonly",
                                      width=25)
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
        quantity_label = tk.Label(quantity_frame, text="Lượng máu (ml):", font=("Arial", 12), bg="#ffffff", width=15,
                                  anchor="w")
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

        submit_button = tk.Button(popup, text="Nhập kho", command=submit_entry, font=("Arial", 12), bg="#D3D3D3",
                                  fg="black")
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




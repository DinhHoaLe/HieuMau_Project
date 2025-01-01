import tkinter as tk
from tkinter import ttk, messagebox


class BloodStorageView:
    def __init__(self, root,controller):
        self.root = root
        self.frame = tk.Frame(self.root, bg="white")
        self.controller = controller
        self.rh_factor_var = tk.StringVar()  # Define here to be accessible throughout the class
        self.blood_type_var = tk.StringVar()

        self.setup_inventory_info_section()
        self.setup_blood_entry_section()
    def create_blood_storage_frame(self):

        return self.frame

    def setup_inventory_info_section(self):
        """Phần thông tin tồn kho"""
        inventory_frame = tk.Frame(self.frame, bg="#ffffff")
        inventory_frame.pack(pady=5, fill="x")

        inventory_label = tk.Label(inventory_frame, text="Thông tin tồn kho", font=("Arial", 16, "bold"), bg="#ffffff")
        inventory_label.pack(pady=1)

        # Tạo 8 ô vuông cho các nhóm máu
        groups = self.controller.get_blood_groups_stock()
        print("Thông tin nhóm máu ban đầu:", groups)  # Debug: Kiểm tra dữ liệu ban đầu

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

    def update_inventory_display(self):
        """Cập nhật thông tin lượng máu tồn kho trên giao diện."""
        groups = self.controller.get_blood_groups_stock()  # controller trả lại thông tin kho máu mới nhất
        print("Thông tin nhóm máu trong kho sau khi gọi controller:", groups)

        # Lấy các frame con trong inventory_info_section
        inventory_frame = self.frame.winfo_children()[0]  # Phần thông tin tồn kho là frame đầu tiên
        row_frame = inventory_frame.winfo_children()[-1]  # Lấy frame chứa các ô vuông nhóm máu

        # Xóa tất cả widget trong row_frame (tức là các ô vuông nhóm máu cũ)
        for widget in row_frame.winfo_children():
            widget.destroy()

        # Tạo lại các ô vuông và thông tin mới
        for i, (group, rh, stock) in enumerate(groups):
            group_frame = tk.Frame(row_frame, bg="#f2f2f2", width=150, height=150, relief="solid", borderwidth=2)
            group_frame.grid(row=0, column=i, padx=15, pady=10)  # Sử dụng grid để đặt ô vuông

            # Thêm tên nhóm máu và yếu tố Rh vào ô vuông
            group_label = tk.Label(group_frame, text=f"{group} {rh}", font=("Arial", 14, "bold"), bg="#f2f2f2")
            group_label.pack(pady=10)

            # Thêm thông tin tồn kho vào ô vuông
            stock_label = tk.Label(group_frame, text=f"Tồn: {stock} ml", font=("Arial", 12), bg="#f2f2f2")
            stock_label.pack(pady=10)

        # Đảm bảo giao diện được làm mới ngay lập tức
        self.frame.update_idletasks()  # Cập nhật giao diện ngay lập tức

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
        columns = ("Mã nhập kho", "Nhóm máu", "Yếu tố Rh","Lượng máu", "Ngày nhập", "Nguồn")

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
            if col == "Nguồn":
                self.entry_treeview.column(col, width=200, anchor="w")
            else:
                self.entry_treeview.column(col, width=100, anchor="center")

        # Chỉnh màu các dòng
        style.configure("Treeview", font=("Arial", 11), rowheight=25, background="#f9f9f9", foreground="black")
        style.map("Treeview", background=[("selected", "#5e9aef")], foreground=[("selected", "white")])

        # Load data từ controller và cập nhật vào bảng
        self.load_blood_entry_info_from_db()

    def load_blood_entry_info_from_db(self):
        """Tải thông tin nhập kho từ cơ sở dữ liệu qua controller"""
        # Lấy dữ liệu từ controller
        entry_data = self.controller.get_list_load_blood_entry_inf()

        # Kiểm tra nếu không có dữ liệu (danh sách trống)
        if not entry_data:
            # Nếu không có dữ liệu, bạn có thể chọn chỉ xóa các dòng hiện tại mà không làm gì thêm
            for row in self.entry_treeview.get_children():
                self.entry_treeview.delete(row)
            return  # Dừng lại nếu không có dữ liệu để thêm

        # Xóa tất cả các dòng hiện tại trong bảng
        for row in self.entry_treeview.get_children():
            self.entry_treeview.delete(row)

        # Duyệt qua kết quả và thêm vào bảng
        for unit in entry_data:
            # unit là đối tượng ImportInventory, lấy các giá trị tương ứng
            self.entry_treeview.insert("", "end", values=(
            unit.import_code, unit.blood_type, unit.rh_factor, unit.volume, unit.import_date, unit.source))

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
        popup_height = 500

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

        # Khai báo các label lỗi
        error_labels = {}

        # Hàm hiển thị lỗi
        def show_error(row, error_message):
            error_label = tk.Label(form_frame, text=error_message, font=("Arial", 10, "italic"), fg="red", bg="#ffffff")
            error_label.grid(row=row + 1, column=1, pady=5, sticky="w")
            error_labels[row] = error_label

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
        donor_label.grid(row=1, column=0, padx=5, pady=5)
        donor_combobox = ttk.Combobox(donor_frame, textvariable=donor_var, state="readonly", font=("Arial", 11),
                                      width=25)
        donor_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Lấy dữ liệu người hiến máu từ cơ sở dữ liệu
        donors = self.controller.fetch_donors_for_dropdown()  # Đây là hàm lấy dữ liệu từ DB
        donor_combobox["values"] = donors
        donor_combobox.bind("<<ComboboxSelected>>", lambda e: on_donor_selected())

        donor_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")


        # Tên cơ sở (Label và Entry)
        facility_var = tk.StringVar()
        facility_frame = tk.Frame(form_frame, bg="#ffffff")
        facility_label = tk.Label(facility_frame, text="Tên cơ sở:", font=("Arial", 12), bg="#ffffff", width=15,
                                  anchor="w")
        facility_label.grid(row=2, column=0, padx=5, pady=5)
        facility_entry = tk.Entry(facility_frame, textvariable=facility_var, font=("Arial", 11), width=27)
        facility_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        facility_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")


        # Nhóm máu (Label và Dropdown)
        blood_type_var = tk.StringVar()
        blood_frame = tk.Frame(form_frame, bg="#ffffff")
        blood_label = tk.Label(blood_frame, text="Nhóm máu:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        blood_label.grid(row=0, column=0, padx=5, pady=5)
        blood_combobox = ttk.Combobox(blood_frame, textvariable=blood_type_var, font=("Arial", 11), state="readonly",
                                      width=25)
        blood_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        blood_combobox["values"] = ["A", "B", "O", "AB"]

        blood_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")



        # Yếu tố Rh (Label và Dropdown)
        rh_factor_var = tk.StringVar()
        rh_frame = tk.Frame(form_frame, bg="#ffffff")
        rh_label = tk.Label(rh_frame, text="Yếu tố Rh:", font=("Arial", 12), bg="#ffffff", width=15, anchor="w")
        rh_label.grid(row=0, column=0, padx=5, pady=5)
        rh_combobox = ttk.Combobox(rh_frame, textvariable=rh_factor_var, font=("Arial", 11), state="readonly", width=25)
        rh_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        rh_combobox["values"] = ["+", "-"]

        rh_frame.grid(row=7, column=0, columnspan=2, pady=5, sticky="ew")



        # Lượng máu (Label và Entry)
        quantity_var = tk.StringVar()
        quantity_frame = tk.Frame(form_frame, bg="#ffffff")
        quantity_label = tk.Label(quantity_frame, text="Lượng máu (ml):", font=("Arial", 12), bg="#ffffff", width=15,
                                  anchor="w")
        quantity_label.grid(row=0, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(quantity_frame, textvariable=quantity_var, font=("Arial", 11), width=27)
        quantity_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        quantity_frame.grid(row=9, column=0, columnspan=2, pady=5, sticky="ew")



        # Nút xác nhận
        def submit_entry():
            # Reset lỗi trước đó
            for label in error_labels.values():
                label.grid_forget()

            error_found = False

            # Kiểm tra lỗi cho từng trường
            if source_var.get() == "Người hiến máu" and not donor_var.get():
                show_error(1, "Vui lòng chọn người hiến máu")
                error_found = True
            if source_var.get() == "Cơ sở khác" and not facility_var.get():
                show_error(2, "Vui lòng nhập tên cơ sở")
                error_found = True
            if not blood_type_var.get():
                show_error(4, "Vui lòng chọn nhóm máu")
                error_found = True
            if not rh_factor_var.get():
                show_error(7, "Vui lòng chọn yếu tố Rh")
                error_found = True
            quantity_value = quantity_var.get()
            if not quantity_value.isdigit() or int(quantity_value) <= 0:
                show_error(9, "Vui lòng nhập lượng máu hợp lệ (chỉ nhập số và lớn hơn 0)")
                error_found = True

            if error_found:
                return

            # Nếu không có lỗi tiến hành thêm nhập kho
            if source_var.get() == "Người hiến máu":
                source= "Người hiến: " + donor_var.get()
            else:
                source = "Cơ sở: " + facility_var.get()
            # Gọi trực tiếp hàm từ controller
            self.controller.add_blood_entry(
                volume=quantity_value,
                source = source,
                blood_type=blood_type_var.get(),
                rh_factor=rh_factor_var.get()
                )
            self.load_blood_entry_info_from_db()
            self.update_inventory_display()
            popup.destroy()

        submit_button = tk.Button(popup, text="Nhập kho", command=submit_entry, font=("Arial", 12), bg="#4CAF50",
                                  fg="white")
        submit_button.grid(row=6, column=0, columnspan=2, pady=20)

        # Xử lý khi thay đổi nguồn
        def toggle_source(source):
            donor_var.set("")
            facility_var.set("")
            blood_type_var.set("")
            rh_factor_var.set("")
            quantity_var.set("")
            for label in error_labels.values():
                label.grid_forget()
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

            # Cắt chuỗi để lấy mã người hiến máu trước dấu ngoặc vuông
            donor_code = selected.split(']')[0].strip('[')  # Tách chuỗi và lấy phần trước dấu ] (sau khi đã bỏ dấu [)

            # Cập nhật nhóm máu và yếu tố Rh dựa trên mã người hiến máu
            donor_info = self.controller.get_blood_info(donor_code)
            if donor_info:
                blood_type_var.set(donor_info["blood_type"])
                rh_factor_var.set(donor_info["rh_factor"])

        # Hiển thị khung đầu tiên (dựa trên giá trị mặc định)
        toggle_source("Người hiến máu")
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from tkcalendar import DateEntry

from model.YeuCauMau_Model import BloodRequest

class BloodRequestManagementView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root, bg="white")
        self.setup_search_section()
        self.setup_request_table()
        self.load_blood_requests()
        # self.treeview.bind("<Configure>", self.adjust_column_width)

        # self.treeview.bind("<Configure>", self.adjust_column_width)

    def create_request_management_frame(self):
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
        # Bind the Enter key press event to the search method
        self.search_entry.bind('<Return>', self.search_blood_requests)

        # Button Nút tìm kiếm
        search_button = tk.Button(
            search_frame,
            text="Tìm kiếm",
            command=self.search_blood_requests,  # Gọi phương thức tìm kiếm trong controller
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        search_button.grid(row=0, column=2, padx=10)

        add_button = tk.Button(
            search_frame,
            text="Thêm",
            command=self.show_add_modal,
            font=("Arial", 12),
            bg="#D3D3D3",
            fg="black"
        )
        add_button.grid(row=0, column=3, padx=10)


    def update_request_table_for_search(self, requests):
        for row in self.treeview.get_children():
            self.treeview.delete(row)  # Xóa tất cả các dòng hiện tại trong bảng

        # Thêm các yêu cầu máu tìm được vào bảng
        for request in requests:
            formatted_row = (
                request[0],  # Mã yêu cầu máu
                request[1],  # Mã bệnh nhân
                request[2],  # Tên bệnh nhân
                request[3],  # Khoa yêu cầu
                request[4],  # Nhóm máu
                request[5],  # Yếu tố Rh
                request[6],  # Lượng máu
                request[7],  # Ngày yêu cầu
                request[8],  # Trạng thái
                request[9],  # Ghi chú
                "Xử lý"  # Dữ liệu cho Action
            )
            self.treeview.insert("", "end", values=formatted_row)  # Thêm dòng vào bảng

    def setup_request_table(self):
        """Thiết lập bảng dữ liệu"""
        self.table_frame = tk.Frame(self.frame)  # Gắn vào self.frame
        self.table_frame.pack(pady=20, fill="both", expand=True)

        columns = (
            "Mã yêu cầu máu",
            "Mã bệnh nhân",
            "Tên bệnh nhân",
            "Nhóm máu",
            "Yếu tố Rh",
            "Lượng máu",
            "Khoa yêu cầu",
            "Ngày yêu cầu",
            "Trạng thái",
            "Ghi chú",
            "Xử lí"
        )

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold"),
            background="#D3D3D3",
            foreground="black"
        )
        style.configure(
            "Treeview",
            font=("Arial", 11),
            rowheight=25
        )

        self.treeview = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.treeview.pack(fill="both", expand=True)

        self.fixed_columns = {
            "Action": 100,
            "Nhóm máu": 100,
            "Yếu tố Rh": 100,
            "Lượng máu": 100,
        }
        self.dynamic_columns = [
            "Mã định danh", "Mã yêu cầu máu", "Mã bệnh nhân", "Khoa yêu cầu"
        ]

        for col in columns:
            self.treeview.heading(col, text=col)
            if col in self.fixed_columns:
                self.treeview.column(col, width=self.fixed_columns[col], anchor="center", stretch=False)
            else:
                self.treeview.column(col, width=100, anchor="center", stretch=True)

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
                    request_code = values[0]  # Lấy giá trị Mã định danh (ID) từ cột đầu tiên
                    blood_type = values[3]
                    rh_factor = values[4]
                    volume  = values[5]
                    request_status = values[8]
                    if request_status != "Chờ xử lý":
                        # Hiển thị thông báo nếu trạng thái không phải "Chờ xử lý"
                        tk.messagebox.showwarning(
                            "Hành động không hợp lệ",
                            "Không được sửa hoặc xóa yêu cầu khác trạng thái 'Chờ xử lý'."
                        )
                    else:
                        # Hiển thị menu nếu trạng thái là "Chờ xử lý"
                        action_menu = tk.Menu(self.root, tearoff=0)
                        action_menu.add_command(label="Sửa", command=lambda: self.show_edit_modal(request_code))
                        action_menu.add_command(label="Xóa",
                                                command=lambda: self.show_confirm_delete(request_code))
                        action_menu.add_command(label="Xác nhận",
                                                command=lambda: self.show_confirm_complete(request_code,blood_type,rh_factor,volume))
                        action_menu.post(event.x_root, event.y_root)

    def load_blood_requests(self):
        requests = BloodRequest.get_all_requests()
        self.update_request_table(requests)

    def update_request_table(self, data):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for request in data:
            # Chuyển datetime.date thành chuỗi
            formatted_row = (
                request[0],  # Mã yêu cầu
                request[1],  # Mã bệnh nhân
                request[2],  # Tên bệnh nhân
                request[3],    # Nhóm máu
                request[4],  # Yếu tố Rh
                request[5],  # Lượng máu
                request[6],  # Khoa Yêu Cầu
                request[7].strftime('%Y-%m-%d') if isinstance(request[7], datetime.date) else request[7],
                request[8],  # Trạng thái
                request[9],  # Ghi chú
                "Xử lý"  # Dữ liệu cho Action
            )
            self.treeview.insert("", "end", values=formatted_row)

    def search_blood_requests(self, event=None):
        # Check if event is None (button click), otherwise it's Enter key press
        search_term = self.search_entry.get().strip()

        if not search_term:
            result = BloodRequest.get_all_requests()
        else:
            result = BloodRequest.search_requests_by_patient(search_term)  # Perform search with the term

        # Call method to update the table or UI with results
        self.update_request_table(result)

    def show_add_modal(self):
        # Tạo cửa sổ modal
        modal = tk.Toplevel(self.root)
        modal.title("Thêm yêu cầu hiến máu")
        modal.geometry("600x400")
        modal.resizable(False, False)
        modal.transient(self.root)  # Giữ modal trên cửa sổ chính
        modal.grab_set()  # Ngăn chặn tương tác với cửa sổ chính khi modal mở

        # Danh sách các trường thông tin

        fields = [
            ("Mã bệnh nhân", "select_patientId"),
            # ("Tên bệnh nhân","select_fullname"),
            ("Khoa yêu cầu", "select_RequestingDepartment"),
            ("Nhóm máu", "select_blood"),
            ("Yếu tố Rh", "text"),
            ("Lượng máu", "text"),
            ("Ngày yêu cầu", "date"),
            # ("Trạng thái", "select_status"),
            ("Trạng thái", "status_disable"),
            ("Ghi chú", "text")
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

            elif field_type == "select_RequestingDepartment":

                gender_var = tk.StringVar()
                gender_var.set("Chọn khoa")  # Giá trị mặc định

                entry = ttk.OptionMenu(form_frame, gender_var, "Chọn khoa", "Khoa Hồi Sức", "Khoa Cấp Cứu",
                                       "Khoa Chấn Thương Chỉnh Hình")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")

                # Thêm frame phụ để căn chỉnh chiều rộng
                entry_frame = tk.Frame(form_frame)
                entry_frame.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=40)
                self.entries[field_name] = gender_var

            elif field_type == "select_patientId":

                gender_var = tk.StringVar()
                gender_var.set("Chọn mã bệnh nhân")  # Giá trị mặc định

                entry = ttk.OptionMenu(form_frame, gender_var, "Chọn mã bệnh nhân", "1", "2")
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

            # elif field_type == "select_status":
            #     blood_var = tk.StringVar()
            #     blood_var.set("Chọn trạng thái")  # Giá trị mặc định
            #
            #     entry = ttk.OptionMenu(form_frame, blood_var, "Chọn trạng thái", "Chờ xử lý", "Đã hoàn thành",
            #                            "Đã từ chối")
            #     entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")
            #
            #     entry_frame = tk.Frame(form_frame)
            #     entry_frame.grid(row=i, column=1, pady=5, padx=10, sticky="w")
            #     entry.config(width=40)
            #     self.entries[field_name] = blood_var

            elif field_type == "status_disable":
                entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
                entry.insert(0, "Chờ xử lý")  # Insert the text "Chờ xử lý"
                entry.config(state="disabled")  # Disable the entry widget to prevent editing
                entry.grid(row=i, column=1, pady=5, padx=10)
                self.entries[field_name] = entry

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
            command=lambda: self.controller.add_blood_request(self, self.save_request_data())
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

    def save_request_data(self):
        # Lấy dữ liệu từ các trường nhập
        request_data = {}
        for field, widget in self.entries.items():
            if isinstance(widget, tk.StringVar):  # Dùng với OptionMenu
                request_data[field] = widget.get()
            else:  # Dùng với Entry hoặc DateEntry
                request_data[field] = widget.get()
        return request_data

    # def show_edit_modal(self, request_id):
    #     if request_id is None:
    #         messagebox.showerror("Lỗi", "Không tìm thấy ID yêu cầu hiến máu.")
    #         return

    def show_confirm_delete(self, request_code):
        """Hiển thị hộp thoại xác nhận xóa."""
        print(request_code)
        # selected_item = self.treeview.selection()  # Lấy dòng được chọn

        if not request_code:
            messagebox.showwarning("Không có dòng được chọn", "Vui lòng chọn dòng để xóa.")
            return

        confirm = messagebox.askyesno("Xác nhận xóa", "Bạn có chắc muốn xóa yêu cầu này?")
        if confirm:
            # Xóa dòng được chọn
            print("Selected Item:", request_code)
            print("Type of Selected Item:", type(request_code))

            self.controller.delete_request_by_id(self,request_code)
            # self.treeview.delete(selected_item)
            messagebox.showinfo("Thông báo", "Dòng đã bị xóa.")
        else:
            print("Yêu cầu không bị xóa.")

    def show_confirm_complete(self, request_code, blood_type,rh_factor,volume):
        """Hiển thị hộp thoại xác nhận hoàn thành."""
        print(request_code)

        if not request_code:
            messagebox.showwarning("Không có dòng được chọn", "Vui lòng chọn dòng để hoàn thành.")
            return

        confirm = messagebox.askyesno("Xác nhận hoàn thành", "Bạn có chắc muốn đánh dấu yêu cầu này là hoàn thành?")
        if confirm:
            # Thực hiện đánh dấu hoàn thành yêu cầu
            self.controller.confirm_request_by_id(self,request_code,blood_type,rh_factor,volume)



    def edit_request(self):
        """Xử lý sự kiện nút Sửa."""
        # Lấy dòng được chọn từ Treeview
        selected_item = self.treeview.selection()

        if not selected_item:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một yêu cầu để chỉnh sửa.")
            return

        # Lấy mã yêu cầu (request_code) từ dòng được chọn
        request_code = self.treeview.item(selected_item[0], "values")[0]

        # Mở cửa sổ chỉnh sửa với request_code
        self.show_edit_modal(request_code)

    def show_edit_modal(self, request_code=None):
        if request_code is None:
            messagebox.showerror("Lỗi", "Không tìm thấy ID yêu cầu hiến máu.")
            return

        # Tạo cửa sổ modal
        modal = tk.Toplevel(self.root)
        modal.title("Chỉnh sửa thông tin yêu cầu hiến máu")
        modal.geometry("400x450")
        modal.resizable(False, False)
        modal.transient(self.root)  # Giữ modal trên cửa sổ chính
        modal.grab_set()  # Ngăn chặn tương tác với cửa sổ chính khi modal mở

        # Trường dữ liệu cần chỉnh sửa
        fields = [
            ("Mã bệnh nhân", "select_patientId"),
            ("Khoa yêu cầu", "select_RequestingDepartment"),
            ("Nhóm máu", "select_blood"),
            ("Yếu tố Rh", "text"),
            ("Lượng máu", "text"),
            ("Ngày yêu cầu", "date"),
            ("Trạng thái", "select_status"),
            ("Ghi chú", "text")
        ]

        form_frame = tk.Frame(modal, padx=10, pady=10)
        form_frame.pack(fill="both", expand=True)

        self.edit_entries = {}

        # Lấy dữ liệu từ Controller
        request_data = self.controller.get_info_request(request_code)
        print("📝 Dữ liệu yêu cầu:", request_data)

        if not request_data:
            messagebox.showerror("Lỗi", f"Không tìm thấy thông tin yêu cầu với ID {request_code}.")
            modal.destroy()
            return

        for i, (field_name, field_type) in enumerate(fields):
            label = tk.Label(form_frame, text=field_name, font=("Arial", 12))
            label.grid(row=i, column=0, sticky="w", pady=5)

            value = request_data.get(field_name, "")

            if field_type == "text":
                entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
                entry.grid(row=i, column=1, pady=5, padx=10)
                entry.insert(0, value)
                self.edit_entries[field_name] = entry

            elif field_type == "date":
                entry = DateEntry(form_frame, font=("Arial", 12), width=28, date_pattern='yyyy-mm-dd')
                entry.grid(row=i, column=1, pady=5, padx=10)
                if isinstance(value, (datetime.date, datetime.datetime)):
                    entry.set_date(value)
                self.edit_entries[field_name] = entry

            elif field_type == "select_patientId":
                patient_var = tk.StringVar()
                patient_var.set(value if value else "Chọn mã bệnh nhân")
                entry = ttk.OptionMenu(form_frame, patient_var, value, "1", "2", "3")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=30)
                self.edit_entries[field_name] = patient_var

            elif field_type == "select_RequestingDepartment":
                department_var = tk.StringVar()
                department_var.set(value if value else "Chọn khoa")
                entry = ttk.OptionMenu(form_frame, department_var, value,
                                       "Khoa Hồi Sức", "Khoa Cấp Cứu", "Khoa Chấn Thương Chỉnh Hình")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=30)
                self.edit_entries[field_name] = department_var

            elif field_type == "select_blood":
                blood_var = tk.StringVar()
                blood_var.set(value if value else "Chọn nhóm máu")
                entry = ttk.OptionMenu(form_frame, blood_var, value, "A", "B", "AB", "O")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=30)
                self.edit_entries[field_name] = blood_var

            elif field_type == "select_status":
                status_var = tk.StringVar()
                status_var.set(value if value else "Chọn trạng thái")
                entry = ttk.OptionMenu(form_frame, status_var, value,
                                       "Chờ xử lý", "Đã hoàn thành", "Đã từ chối")
                entry.grid(row=i, column=1, pady=5, padx=10, sticky="w")
                entry.config(width=30)
                entry["state"] = "disabled"  # Vô hiệu hóa không cho chọn
                self.edit_entries[field_name] = status_var

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        save_button = tk.Button(
            button_frame,
            text="Lưu",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.controller.update_request(self, request_code, self.get_edited_data())
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

    def get_edited_data(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        edited_data = {}
        for key, entry in self.edit_entries.items():
            edited_data[key] = entry.get()
        print("✅ Dữ liệu chỉnh sửa:", edited_data)
        return edited_data










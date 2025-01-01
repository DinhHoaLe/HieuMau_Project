import tkinter as tk
from tkinter import ttk, messagebox

from controller.KhoMau_Controller import BloodInventoryController
from controller.YeuCauMau_Controller import BloodRequestController
from view.BenhNhan_View import StatisticsView
from view.KhoMau_View import BloodStorageView
from view.NguoiHienMau_View import DonorManagementView
from view.TongQuan_View import StatisticalView
from view.YeuCauMau_View import BloodRequestManagementView
from controller.NguoiHIenMau_Controller import DonorBloodController
from controller.TongQuan_Controller import StatisticalController


class AppView:
    def __init__(self, root):
        self.root = root
        # self.controller = controller
        self.root.title("Quản lý ngân hàng máu")

        self.root.state('zoomed')
        self.root.resizable(True, True)
        self.root.configure(bg="#ffffff")

        self.setup_header()
        self.setup_buttons()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
        # Khởi tạo controller cho "Tổng quan" và lưu vào biến instance
        self.statistical_controller = StatisticalController(self.root)
        self.blood_inventory_controller = BloodInventoryController(self.root)
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
        # Frames cho từng giao diện
        self.frames = {
            "Tổng quan": self.statistical_controller.view.create_statistical_frame(),
            "Quản lý người hiến máu": DonorManagementView(self.root, DonorBloodController).create_frame(),
            "Quản lý kho máu": self.blood_inventory_controller.view.create_blood_storage_frame(),
            "Quản lý yêu cầu máu": BloodRequestManagementView(self.root,
                                                              BloodRequestController).create_request_management_frame(),
            "Quản lý bệnh nhân": StatisticsView(self.root).create_statistics_frame(),
        }
        self.frames["Quản lý kho máu"].statistical_view = self.frames["Tổng quan"]
        # Hiển thị frame mặc định
        self.active_tab = None
        self.current_frame = None
        self.show_frame("Tổng quan")

    def setup_header(self):
        header_frame = tk.Frame(self.root, bg="#610a0a", height=100)
        header_frame.pack(fill="x")
        header_text = tk.Label(header_frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter", 18), fg="#ffffff",
                               bg="#610a0a")
        header_text.pack(pady=30)

    def setup_buttons(self):
        buttons_frame = tk.Frame(self.root, bg="#610a0a")
        buttons_frame.pack(fill="x")

        self.buttons = {}  # Lưu trữ các nút để quản lý màu sắc

        button_names = [
            "Tổng quan",
            "Quản lý người hiến máu",
            "Quản lý kho máu",
            "Quản lý yêu cầu máu",
            "Quản lý bệnh nhân"
        ]

        for text in button_names:
            self.buttons[text] = self.create_button(buttons_frame, text, self.show_frame)

    def create_button(self, parent, text, command):
        """Tạo nút và thêm hiệu ứng hover, active."""
        button = tk.Button(
            parent,
            text=text,
            font=("Inter", 12, "bold"),
            fg="#000000",
            bg="#d9d9d9",  # Màu mặc định
            command=lambda t=text: command(t)
        )
        button.pack(side="left", padx=5, pady=10, expand=True, fill="both")

        # Thêm hiệu ứng hover
        button.bind("<Enter>", lambda event, b=button: self.on_hover(b))
        button.bind("<Leave>", lambda event, b=button, t=text: self.on_leave(b, t))

        return button

    def on_hover(self, button):
        """Hiệu ứng hover khi di chuột vào nút."""
        if button != self.buttons.get(self.active_tab):
            button.config(bg="#FFA07A")  # Màu cam nhạt khi hover

    def on_leave(self, button, text):
        if text == self.active_tab:
            button.config(bg="#FFDD57")  # Màu active
        else:
            button.config(bg="#d9d9d9")  # Màu mặc định

    def show_frame(self, frame_name):
        """Hiển thị frame tương ứng và ẩn frame hiện tại."""
        # Ẩn frame hiện tại nếu có
        if self.current_frame:
            self.current_frame.pack_forget()

        # Hiển thị frame mới
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill="both", expand=True)

        # Cập nhật giao diện khi chuyển tab
        if frame_name == "Tổng quan":
            self.statistical_controller.view.update_view()
        elif frame_name == "Quản lý kho máu":
            # Gọi phương thức cập nhật kho máu khi chuyển sang tab "Quản lý kho máu"
            self.blood_inventory_controller.view.update_inventory_display()

        # Cập nhật trạng thái active tab
        self.update_active_tab(frame_name)

    def update_active_tab(self, active_tab):
        """Cập nhật màu sắc cho tab đang active."""
        self.active_tab = active_tab
        for text, button in self.buttons.items():
            if text == active_tab:
                button.config(bg="#FFDD57")  # Màu vàng cho tab đang active
            else:
                button.config(bg="#d9d9d9")  # Màu xám cho tab không active

    #commit
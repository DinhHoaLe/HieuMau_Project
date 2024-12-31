import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatisticalView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root, bg="white")  # Frame chính của View
        self.setup_quick_stats_section()
        self.setup_chart_section()

    def create_statistical_frame(self):
        """Tạo giao diện chính của Dashboard."""

        return self.frame

    def setup_quick_stats_section(self):
        """Tạo phần thống kê nhanh trong Dashboard."""
        stats_frame = tk.Frame(self.frame, bg="#ffffff")
        stats_frame.pack(pady=5, fill="x")

        quick_stats_label = tk.Label(stats_frame, text="Thống kê nhanh", font=("Arial", 16, "bold"), bg="#ffffff")
        quick_stats_label.pack(pady=1)

        # Lấy thống kê từ controller
        quick_stats = self.controller.get_quick_stats_model()
        stats = [
            ("Tổng số máu trong kho (ml)", quick_stats["total_blood"]),
            ("Tổng số người hiến", quick_stats["total_donors"]),
            ("Yêu cầu chưa xử lý", quick_stats["pending_requests"]),
        ]

        # Tạo frame chính để chứa các ô vuông
        row_frame = tk.Frame(stats_frame, bg="#ffffff")
        row_frame.pack(pady=5)

        # Tạo các ô vuông cho từng thống kê
        for i, (label, value) in enumerate(stats):
            stat_frame = tk.Frame(row_frame, bg="#ffffff", width=150, height=150, relief="solid", borderwidth=2)
            stat_frame.grid(row=0, column=i, padx=15, pady=10)  # Sử dụng grid để đặt ô vuông

            # Thêm tên thống kê vào ô vuông
            stat_label = tk.Label(stat_frame, text=label, font=("Arial", 14, "bold"), bg="#ffffff")
            stat_label.pack(pady=10)

            # Thêm giá trị vào ô vuông
            value_label = tk.Label(stat_frame, text=str(value), font=("Arial", 16, "bold"), bg="#ffffff", fg="#007BFF")
            value_label.pack(pady=10)

        # Cấu hình grid để phân bổ đều các ô thống kê theo chiều ngang
        row_frame.grid_columnconfigure(0, weight=1)  # Give equal weight to each column
        row_frame.grid_columnconfigure(1, weight=1)
        row_frame.grid_columnconfigure(2, weight=1)

    def setup_chart_section(self):
        """Tạo biểu đồ tồn kho nhóm máu"""
        # Tạo frame chứa biểu đồ
        chart_frame = tk.Frame(self.frame, bg="#ffffff", pady=10)
        chart_frame.pack(pady=10, fill="x")  # Sử dụng pack cho phần biểu đồ, canh giữa với fill="x"

        # Tạo nhãn tiêu đề cho biểu đồ
        chart_label = tk.Label(chart_frame, text="Tồn kho theo nhóm máu", font=("Arial", 14, "bold"), bg="#ffffff")
        chart_label.pack(padx=5, pady=5, anchor="center")

        # Dữ liệu giả lập nhóm máu và tồn kho
        blood_groups = self.controller.get_blood_groups_stock()
        labels = [f"{group} {rh}" for group, rh, _ in blood_groups]  # Danh sách tên nhóm máu
        values = [stock for _, _, stock in blood_groups]  # Danh sách số lượng tồn kho

        # Vẽ biểu đồ cột (bar chart)
        fig, ax = plt.subplots(figsize=(6, 4))  # Tạo đối tượng figure và axes cho biểu đồ, thiết lập kích thước
        ax.bar(labels, values, color='#007BFF')  # Vẽ các cột với màu xanh dương
        ax.set_xlabel('Nhóm máu')  # Đặt nhãn trục X
        ax.set_ylabel('Tồn kho (ml)')  # Đặt nhãn trục Y
        plt.tight_layout()

        # Hiển thị biểu đồ trong giao diện Tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)  # Tạo đối tượng canvas để hiển thị biểu đồ
        canvas.get_tk_widget().pack(pady=10, expand=True)  # Sử dụng pack để đặt canvas vào frame biểu đồ
        canvas.draw()  # Vẽ biểu đồ trên canvas

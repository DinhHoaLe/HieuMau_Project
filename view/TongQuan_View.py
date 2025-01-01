import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model.TongQuan_Model import TongQuan_Model


class StatisticalView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root, bg="white")  # Frame chính của View

        self.total_blood_label = None
        self.total_donors_label = None
        self.pending_requests_label = None

        self.fig, self.ax = None, None

        # Setup UI components
        self.setup_quick_stats_section()
        self.setup_chart_section()


    def create_statistical_frame(self):
        """Trả về giao diện chính."""
        return self.frame

    def setup_quick_stats_section(self):
        """Tạo phần thống kê nhanh."""
        stats_frame = tk.Frame(self.frame, bg="#ffffff")
        stats_frame.pack(pady=5, fill="x")

        quick_stats_label = tk.Label(stats_frame, text="Thống kê nhanh", font=("Arial", 16, "bold"), bg="#ffffff")
        quick_stats_label.pack(pady=1)

        row_frame = tk.Frame(stats_frame, bg="#ffffff")
        row_frame.pack(pady=5)

        self.total_blood_label = self.create_stat_box(row_frame, 0, "Tổng số máu trong kho (ml)")
        self.total_donors_label = self.create_stat_box(row_frame, 1, "Tổng số người hiến")
        self.pending_requests_label = self.create_stat_box(row_frame, 2, "Yêu cầu chưa xử lý")

        row_frame.grid_columnconfigure(0, weight=1)
        row_frame.grid_columnconfigure(1, weight=1)
        row_frame.grid_columnconfigure(2, weight=1)


    def create_stat_box(self, parent, column, label_text):
        """Tạo ô vuông thống kê."""
        stat_frame = tk.Frame(parent, bg="#ffffff", width=150, height=150, relief="solid", borderwidth=2)
        stat_frame.grid(row=0, column=column, padx=15, pady=10)

        stat_label = tk.Label(stat_frame, text=label_text, font=("Arial", 14, "bold"), bg="#ffffff")
        stat_label.pack(pady=10)

        value_label = tk.Label(stat_frame, text="0", font=("Arial", 16, "bold"), bg="#ffffff", fg="#007BFF")
        value_label.pack(pady=10)

        return value_label


    def setup_chart_section(self):
        """Tạo biểu đồ tồn kho nhóm máu."""
        self.chart_frame = tk.Frame(self.frame, bg="#ffffff", pady=10)
        self.chart_frame.pack(pady=10, fill="x")

        chart_label = tk.Label(self.chart_frame, text="Tồn kho theo nhóm máu", font=("Arial", 14, "bold"), bg="#ffffff")
        chart_label.pack(padx=5, pady=5, anchor="center")

        self.fig, self.ax = plt.subplots(figsize=(6, 4))

    def update_view(self):
        """Cập nhật giao diện với dữ liệu mới."""
        try:
            # Lấy dữ liệu mới từ controller
            quick_stats = TongQuan_Model.get_quick_stats()
            blood_groups = TongQuan_Model.get_blood_groups_stock()

            # Cập nhật phần thống kê nhanh
            self.update_quick_stats(quick_stats)

            # Cập nhật biểu đồ nhóm máu
            self.plot_blood_stock_chart(blood_groups)
        except Exception as e:
            print(f"Lỗi khi cập nhật view: {e}")

    def update_quick_stats(self, quick_stats):
        """Cập nhật giá trị thống kê nhanh."""
        if quick_stats:
            self.total_blood_label.config(text=str(quick_stats.get("total_blood", 0)))
            self.total_donors_label.config(text=str(quick_stats.get("total_donors", 0)))
            self.pending_requests_label.config(text=str(quick_stats.get("pending_requests", 0)))

            # Đảm bảo các label được vẽ lại
            self.total_blood_label.update_idletasks()
            self.total_donors_label.update_idletasks()
            self.pending_requests_label.update_idletasks()

    def plot_blood_stock_chart(self, blood_groups):
        """Vẽ biểu đồ nhóm máu và tồn kho."""
        self.ax.clear()  # Xóa biểu đồ cũ
        labels = [f"{group} {rh}" for group, rh, _ in blood_groups]
        values = [stock for _, _, stock in blood_groups]

        self.ax.bar(labels, values, color='#007BFF')
        self.ax.set_xlabel('Nhóm máu')
        self.ax.set_ylabel('Tồn kho (ml)')
        self.ax.set_title('Biểu đồ tồn kho nhóm máu')
        plt.tight_layout()

        # Hiển thị trên Tkinter
        for widget in self.chart_frame.winfo_children():
            widget.destroy()  # Xóa widget cũ trong chart_frame

        canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        canvas.get_tk_widget().pack(pady=10, expand=True)
        canvas.draw()
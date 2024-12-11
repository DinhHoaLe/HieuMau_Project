import tkinter as tk
from tkinter import ttk, messagebox


class DashboardView:
    """Quản lý giao diện của dashboard."""

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("1200x700")

        # Sidebar
        self.sidebar = tk.Frame(root, bg="#0056b3", width=200)
        self.sidebar.pack(side="left", fill="y")

        self.menu_items = [
            ("Home", self.show_dashboard),
            ("Donor Management", self.manage_donors),
            ("Blood Sample Management", self.manage_blood_samples),
            ("Blood Requests", self.manage_blood_requests),
            ("Donation History", self.view_donor_history),
            ("Statistics", self.view_statistics),
            ("Settings", self.settings),
            ("Notifications", self.view_notifications),
            ("Logout", self.logout)
        ]

        for item in self.menu_items:
            btn = tk.Button(
                self.sidebar,
                text=item,
                bg="#0056b3",
                fg="white",
                font=("Arial", 12),
                relief="flat",
                anchor="w",
            )
            btn.pack(fill="x", padx=10, pady=5)

        # Header
        self.header = tk.Frame(root, bg="#f5f5f5", height=50)
        self.header.pack(side="top", fill="x")

        self.btn_export = tk.Button(
            self.header,
            text="EXPORT EXCEL",
            bg="#007bff",
            fg="white",
            font=("Arial", 10),
            relief="flat",
        )
        self.btn_export.pack(side="left", padx=10, pady=5)

        self.btn_refresh = tk.Button(
            self.header,
            text="REFRESH",
            bg="#007bff",
            fg="white",
            font=("Arial", 10),
            relief="flat",
        )
        self.btn_refresh.pack(side="left", padx=10, pady=5)

        self.btn_home = tk.Button(
            self.header,
            text="HOME",
            bg="#007bff",
            fg="white",
            font=("Arial", 10),
            relief="flat",
        )
        self.btn_home.pack(side="left", padx=10, pady=5)

        self.entry_search = tk.Entry(self.header, font=("Arial", 12))
        self.entry_search.pack(side="right", padx=10, pady=5)

        self.btn_search = tk.Button(
            self.header,
            text="Search",
            bg="#007bff",
            fg="white",
            font=("Arial", 10),
            relief="flat",
        )
        self.btn_search.pack(side="right", padx=5, pady=5)

        # Main Table
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        columns = [
            "Order ID",
            "Quantity",
            "Price",
            "Total Bill",
            "Delivery Infor",
            "Consignee Infor",
            "Delivery Status",
            "Status",
            "Action",
        ]

        self.tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=True)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

    def populate_table(self, data):
        """Điền dữ liệu vào bảng."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for record in data:
            self.tree.insert("", "end", values=list(record.values()))

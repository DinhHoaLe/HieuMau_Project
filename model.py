class DashboardModel:
    """Quản lý dữ liệu của dashboard."""

    def __init__(self):
        # Dữ liệu mẫu ban đầu
        self.data = [
            {
                "Order ID": "001",
                "Quantity": 10,
                "Price": 100,
                "Total Bill": 1000,
                "Delivery Infor": "Address 1",
                "Consignee Infor": "John Doe",
                "Delivery Status": "Pending",
                "Status": "In Progress",
                "Action": "View",
            },
            {
                "Order ID": "002",
                "Quantity": 5,
                "Price": 200,
                "Total Bill": 1000,
                "Delivery Infor": "Address 2",
                "Consignee Infor": "Jane Doe",
                "Delivery Status": "Completed",
                "Status": "Delivered",
                "Action": "View",
            },
        ]

    def get_data(self):
        """Lấy dữ liệu hiện tại."""
        return self.data

    def add_order(self, order):
        """Thêm một đơn hàng mới."""
        self.data.append(order)

    def delete_order(self, order_id):
        """Xóa đơn hàng theo ID."""
        self.data = [order for order in self.data if order["Order ID"] != order_id]

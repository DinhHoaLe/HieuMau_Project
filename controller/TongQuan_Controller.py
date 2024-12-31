from tkinter import messagebox
from model.TongQuan_Model import TongQuan_Model
from model.QuanLyKhoMau_Model import BloodInventory
from view.TongQuan_View import StatisticalView


class StatisticalController:
    def __init__(self, root):
        self.root = root
        self.view = None

    def get_quick_stats_model(self):
        """Lấy các thống kê nhanh từ model."""
        return TongQuan_Model.get_quick_stats()

    def get_blood_groups_stock(self):
        return BloodInventory.get_blood_groups_stock()

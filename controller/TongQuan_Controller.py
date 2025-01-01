from model.TongQuan_Model import TongQuan_Model
from view.TongQuan_View import StatisticalView

class StatisticalController:
    def __init__(self,root):
        self.model = TongQuan_Model()
        self.view = StatisticalView(root,self.model)

    def get_quick_stats_model(self):
        """
        Lấy dữ liệu thống kê nhanh từ model.
        """
        return self.model.get_quick_stats()

    def get_blood_groups_stock(self):
        """
        Lấy dữ liệu tồn kho nhóm máu từ model.
        """
        return self.model.get_blood_groups_stock()
    def refresh_view(self):
        self.view.update_view()
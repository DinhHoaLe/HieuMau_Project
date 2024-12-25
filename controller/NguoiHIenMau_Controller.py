from model.NguoiHienMau_Model import DonorModel
from view.NguoiHienMau_View import DonorManagementView


class DonorBloodController:
    def __init__(self, root):
        self.view = DonorManagementView(root, self)  # Truyền root và self làm controller
        self.load_donor()

    def load_donor(self):
        data = DonorModel.get_all_donor()
        self.view.update_donor_table(data)

    def get_info_donor(self, donor_id):
        donor_data = self.view.treeview.item(donor_id)
        return donor_data

    def search_donor(self):
        search_term = self.view.search_entry.get()
        requests = DonorModel.search_donor(search_term)
        self.view.update_donor_table(requests)

    def add_donor(self):
        pass

    def edit_donor(self):
        pass

    def view_donor(self):
        pass

    def delete_donor(self, request_id):
        """Xóa người hiến máu."""
        try:
            DonorModel.delete_donor(request_id)
            self.view.show_message("✅ Người hiến máu đã được xóa thành công!")
            self.load_donor()  # Tải lại danh sách sau khi xóa
        except Exception as e:
            print(f"❌ Lỗi khi xóa người hiến máu: {e}")
            self.view.show_message(f"❌ Lỗi: {e}")

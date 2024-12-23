from model.YeuCauMau_Model import BloodRequest
from view.App_View import AppView


class AppController:
    def __init__(self, root):
        self.view = AppView(root, self)
        # self.load_blood_requests()

    # def load_blood_requests(self):
    #     # Lấy tất cả yêu cầu máu từ model
    #     requests = BloodRequest.get_all_requests()
    #     # Cập nhật bảng với dữ liệu nhận được từ model
    #     self.view.update_request_table(requests)

    # def search_blood_requests(self):
    #     # Lấy từ view từ ô tìm kiếm
    #     search_term = self.view.search_entry.get()
    #     # Tìm kiếm yêu cầu máu từ model
    #     requests = BloodRequest.search_requests(search_term)
    #     # Cập nhật bảng kết quả tìm kiếm vào view
    #     self.view.update_request_table(requests)

    def add_blood_request(self):
        # Xử lý thêm yêu cầu máu (Có thể mở form nhập liệu mới)
        pass

    # def delete_blood_request(self, request_id):
    #     # Xóa yêu cầu máu trong model
    #     BloodRequest.delete_request(request_id)
    #     # Cập nhật lại bảng sau khi xóa
    #     self.view.show_message("Yêu cầu máu đã được xóa.")
    #     self.load_blood_requests()  # Tải lại danh sách yêu cầu máu sau khi xóa

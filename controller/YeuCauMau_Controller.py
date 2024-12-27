from model.YeuCauMau_Model import BloodRequest
from view.YeuCauMau_View import BloodRequestManagementView
from tkinter import messagebox
from datetime import datetime


class BloodRequestController:
    def __init__(self, root):
        self.view = BloodRequestManagementView(root, self)
        self.load_blood_requests()

    def load_blood_requests(self):
        requests = BloodRequest.get_all_requests()
        self.view.update_request_table(requests)

    def search_blood_requests(self):
        # Lấy từ view từ ô tìm kiếm
        search_term = self.view.search_entry.get()
        # Tìm kiếm yêu cầu máu từ model
        requests = BloodRequest.search_requests(search_term)
        # Cập nhật bảng kết quả tìm kiếm vào view
        self.view.update_request_table(requests)

    def add_blood_request(self, requets_data):
        print(requets_data)
        if requets_data:
            try:
                # Gọi model để thêm dữ liệu vào CSDL
                BloodRequest.add_request(requets_data)
                messagebox.showinfo("Thành công", "Thêm người hiến máu thành công!")
                self.load_blood_requests()  # Cập nhật lại bảng
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể thêm người hiến máu: {e}")

    @staticmethod
    def get_info_request(request_id):
        """Lấy thông tin chi tiết người hiến máu."""
        data = BloodRequest.get_request_by_id(request_id)
        if data:
            return {
                "Mã bệnh nhân": data[0],
                "Khoa yêu cầu": data[1],
                "Nhóm máu": data[2],
                "Yếu tố Rh": data[3],
                "Lượng máu": data[4],
                "Ngày yêu cầu": data[5],
                "Trạng thái": data[6],
                "Ghi chú": data[7]
            }
        return None

    def update_request(self, request_id, request_data):
        """Xử lý cập nhật thông tin người hiến máu từ View."""
        print("📝 ID người hiến máu:", request_id)
        print("📝 Dữ liệu nhận từ View:", request_data)

        # Xử lý và chuyển đổi ngày tháng nếu có
        for key in ["Ngày yêu cầu"]:
            if key in request_data and request_data[key]:
                try:
                    request_data[key] = datetime.strptime(request_data[key], "%Y-%m-%d").date()
                except ValueError:
                    messagebox.showerror("Lỗi", f"Ngày không đúng định dạng (YYYY-MM-DD): {request_data[key]}")
                    return

        try:
            BloodRequest.update_request_by_id(request_id, request_data)
            self.load_blood_requests()
            messagebox.showinfo("Thành công", "Cập nhật thông tin người hiến máu thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật thông tin: {e}")
            messagebox.showerror("Lỗi", f"Không thể cập nhật thông tin: {e}")

    def delete_request_by_id(self, request_id):
        # Xóa yêu cầu máu trong model
        BloodRequest.delete_request(request_id)
        # Cập nhật lại bảng sau khi xóa
        messagebox.showinfo("Thành công", "Xóa yêu cầu hiến máu thành công!")
        self.load_blood_requests()  # Tải lại danh sách yêu cầu máu sau khi xóa

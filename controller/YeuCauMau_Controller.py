from model.YeuCauMau_Model import BloodRequest
from model.QuanLyKhoMau_Model import BloodInventory
from controller.KhoMau_Controller import BloodInventoryController
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
        # Tìm kiếm yêu cầu máu từ model theo mã bệnh nhân hoặc tên bệnh nhân
        result = BloodRequest.search_requests_by_patient(self.search_entry.get())
        self.update_request_table_for_search(result)

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
    def get_info_request(request_code):
        """Lấy thông tin chi tiết người hiến máu."""
        data = BloodRequest.get_request_by_request_code(request_code)
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

    def update_request(self, request_code, request_data):
        """Xử lý cập nhật thông tin người hiến máu từ View."""

        # Xử lý và chuyển đổi ngày tháng nếu có
        for key in ["Ngày yêu cầu"]:
            if key in request_data and request_data[key]:
                try:
                    request_data[key] = datetime.strptime(request_data[key], "%Y-%m-%d").date()
                except ValueError:
                    messagebox.showerror("Lỗi", f"Ngày không đúng định dạng (YYYY-MM-DD): {request_data[key]}")
                    return

        try:
            BloodRequest.update_request_by_request_code(request_code, request_data)
            self.load_blood_requests()
            messagebox.showinfo("Thành công", "Cập nhật thông tin người hiến máu thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật thông tin: {e}")
            messagebox.showerror("Lỗi", f"Không thể cập nhật thông tin: {e}")

    def delete_request_by_request_code(self, request_code):
        print(request_code)
        BloodRequest.delete_request(request_code)
        # Cập nhật lại bảng sau khi xóa
        messagebox.showinfo("Thành công", "Xóa yêu cầu hiến máu thành công!")
        self.load_blood_requests()  # Tải lại danh sách yêu cầu máu sau khi xóa

    def confirm_request_by_id(self,request_code,blood_type,rf_factor,volume):
        blood_id = BloodInventory.get_blood_id_by_type_and_rh(blood_type,rf_factor)
        current_volume = BloodInventory.check_blood_inventory(blood_id)
        if current_volume < volume:
            messagebox.showinfo("Thất bại", "Lượng máu tồn trong kho không đủ cung cấp")
        else:
            BloodRequest.update_status_request_by_request_code(request_code)
            BloodInventory.update_blood_volume_by_type(blood_type,rf_factor,-volume)
            messagebox.showinfo("Thành công", "Xác nhận đã yêu cầu hoàn thành!")
            self.load_blood_requests()  # Tải lại danh sách yêu cầu máu sau khi xác nhận
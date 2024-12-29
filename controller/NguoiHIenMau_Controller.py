from model.NguoiHienMau_Model import DonorModel
from view.NguoiHienMau_View import DonorManagementView
from datetime import datetime
from tkinter import messagebox


class DonorBloodController:
    def __init__(self, root):
        self.view = DonorManagementView(root, self)  # Truyền root và self làm controller
        self.load_donor()

    def load_donor(self):
        data = DonorModel.get_all_donor()
        self.view.update_donor_table(data)

    @staticmethod
    def get_info_donor(donor_id):
        """Lấy thông tin chi tiết người hiến máu."""
        data = DonorModel.get_donor_by_id(donor_id)
        if data:
            return {
                "Họ và tên": data[0],
                "Sinh nhật": data[1],
                "Giới tính": data[2],
                "Nhóm máu": data[3],
                "Yếu tố Rh": data[4],
                "Ngày hiến gần nhất": data[5],
                "Điện thoại": data[6],
                "Địa chỉ": data[7]
            }
        return None

    # @staticmethod
    def update_donor(self, donor_id, donor_data):
        # Xử lý và chuyển đổi ngày tháng nếu có
        for key in ["Sinh nhật", "Ngày hiến gần nhất"]:
            if key in donor_data and donor_data[key]:
                try:
                    donor_data[key] = datetime.strptime(donor_data[key], "%Y-%m-%d").date()
                except ValueError:
                    messagebox.showerror("Lỗi", f"Ngày không đúng định dạng (YYYY-MM-DD): {donor_data[key]}")
                    return

        try:
            DonorModel.update_donor_by_id(donor_id, donor_data)
            self.load_donor()
            messagebox.showinfo("Thành công", "Cập nhật thông tin người hiến máu thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật thông tin: {e}")
            messagebox.showerror("Lỗi", f"Không thể cập nhật thông tin: {e}")

    def search_donor(self, search_term):
        requests = DonorModel.search_donor_by_id(search_term)
        self.view.update_donor_table(requests)

    def add_donor(self, donor_data):
        if donor_data:
            try:
                # Gọi model để thêm dữ liệu vào CSDL
                DonorModel.add_donor(donor_data)
                messagebox.showinfo("Thành công", "Thêm người hiến máu thành công!")
                self.load_donor()  # Cập nhật lại bảng
            except Exception as e:
                print(f"❌ Lỗi khi thêm người hiến máu: {e}")
                messagebox.showerror("Lỗi", f"Không thể thêm người hiến máu: {e}")

    @staticmethod
    def view_donor(donor_id):
        data = DonorModel.view_history(donor_id)
        return data

    def delete_donor(self, request_id):
        """Xóa người hiến máu."""
        try:
            DonorModel.delete_donor_by_id(request_id)
            messagebox.showinfo("Thành công", "Xóa người hiến máu thành công!")
            self.load_donor()  # Tải lại danh sách sau khi xóa
        except Exception as e:
            print(f"❌ Lỗi khi xóa người hiến máu: {e}")
            messagebox.showerror("Lỗi", f"Không thể xóa người hiến máu: {e}")

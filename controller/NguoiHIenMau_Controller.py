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
                "Mã định danh": data[0],
                "Mã máu": data[1],
                "Họ và tên": data[2],
                "Sinh nhật": data[3],
                "Giới tính": data[4],
                "Nhóm máu": data[5],
                "Yếu tố Rh": data[6],
                "Ngày hiến gần nhất": data[7],
                "Điện thoại": data[8],
                "Địa chỉ": data[9]
            }
        return None

    # @staticmethod
    def update_donor(self, donor_id, donor_data):
        """Xử lý cập nhật thông tin người hiến máu từ View."""
        print("📝 ID người hiến máu:", donor_id)
        print("📝 Dữ liệu nhận từ View:", donor_data)

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

    def search_donor(self):
        search_term = self.view.search_entry.get()
        requests = DonorModel.search_donor(search_term)
        self.view.update_donor_table(requests)

    def add_donor(self, donor_data):
        """Thêm người hiến máu mới."""
        print(donor_data)
        if donor_data:
            print("📝 Dữ liệu người hiến máu mới:", donor_data)
            try:
                # Gọi model để thêm dữ liệu vào CSDL
                DonorModel.add_donor(donor_data)
                messagebox.showinfo("Thành công", "Thêm người hiến máu thành công!")
                self.load_donor()  # Cập nhật lại bảng
            except Exception as e:
                print(f"❌ Lỗi khi thêm người hiến máu: {e}")
                messagebox.showerror("Lỗi", f"Không thể thêm người hiến máu: {e}")

    def view_donor(self):
        pass

    def delete_donor(self, request_id):
        """Xóa người hiến máu."""
        try:
            DonorModel.delete_donor_by_id(request_id)
            messagebox.showinfo("Thành công", "Xóa người hiến máu thành công!")
            self.load_donor()  # Tải lại danh sách sau khi xóa
        except Exception as e:
            print(f"❌ Lỗi khi xóa người hiến máu: {e}")
            messagebox.showerror("Lỗi", f"Không thể xóa người hiến máu: {e}")

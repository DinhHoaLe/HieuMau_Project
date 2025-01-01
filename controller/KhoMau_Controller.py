from datetime import datetime
from tkinter import messagebox
import re
from model.QuanLyKhoMau_Model import ImportInventory,BloodInventory,DonationRecords
from model.NguoiHienMau_Model import DonorModel
from view.KhoMau_View import BloodStorageView

class BloodInventoryController:
    def __init__(self, root):
        self.view = BloodStorageView(root,self)


    def add_blood_entry(self, volume, source, blood_type, rh_factor):
        import_date = datetime.now().strftime('%Y-%m-%d')  # Lấy ngày hiện tại theo định dạng YYYY-MM-DD
        blood_id = BloodInventory.get_blood_id_by_type_and_rh(blood_type, rh_factor)

        # Cập nhật dữ liệu nhập kho
        import_code = ImportInventory.add_import(volume, import_date, source, blood_id)

        # Cập nhật tồn kho (cộng vào kho)
        BloodInventory.update_blood_volume(blood_id, volume)



        # Thêm lịch sử người hiến máu (nếu có)
        if "Người hiến" in source:
            match = re.match(r"Người hiến: \[([A-Za-z0-9\-]+)\]", source)
            if match:
                donor_code = match.group(1)
                donor_id = DonationRecords.get_donor_id_by_code(donor_code)
                if donor_id:
                    DonationRecords.add_record(donor_id, import_code, import_date, volume)
                else:
                    messagebox.showerror("Lỗi", "Không tìm thấy thông tin người hiến máu với mã đã cung cấp.")
            else:
                messagebox.showerror("Lỗi", "Không tìm thấy mã người hiến trong nguồn.")

        # Hiển thị thông báo thành công
        messagebox.showinfo("Nhập kho thành công", "Thông tin nhập kho đã được lưu.")

        # Gọi phương thức cập nhật giao diện
        #self.statistical_controller.refresh_view()
    def update_inventory_info(self):
        """
        Update thong tin ton kho trong view
        """
        self.view.setup_inventory_info_section()

    def get_blood_groups_stock(self):
        """Lay thong tin kho mau"""
        blood_groups = BloodInventory.get_blood_groups_stock()
        print("Dữ liệu kho máu:", blood_groups)
        return blood_groups

    def get_list_load_blood_entry_inf(self):
        """Lay thong tin load vao bang thong tin nhap kho"""
        return ImportInventory.get_list_load_blood_entry_info()

    def fetch_donors_for_dropdown(self):
        """Lấy danh sách người hiến máu để hiển thị trong combobox"""
        donors = DonorModel.get_all_donor()  # Gọi phương thức tĩnh
        # Định dạng [Mã người hiến] Tên người hiến
        return [f"[{donor[1]}] {donor[2]}" for donor in donors]

    def get_blood_info(self, donor_code):
        """Lấy thông tin nhóm máu và yếu tố Rh từ mã người hiến"""
        return DonationRecords.get_blood_info(donor_code)




import tkinter as tk
from controller.NguoiHIenMau_Controller import DonorBloodController


def test_controller():
    # Tạo cửa sổ Tkinter
    root = tk.Tk()
    root.title("Test DonorBloodController")
    root.geometry("1200x700")

    try:
        print("🛠️ Khởi tạo Controller...")
        controller = DonorBloodController(root)
        print("✅ Controller khởi tạo thành công!")

        # Test load_donor
        print("🔄 Kiểm tra load_donor...")
        controller.load_donor()

        # Test search_donor
        print("🔍 Kiểm tra search_donor với từ khóa 'A'...")
        controller.view.search_entry.insert(0, 'A')
        controller.search_donor()

        # Test add_donor (giả lập thêm người hiến máu)
        print("➕ Kiểm tra add_donor (chưa thực hiện cụ thể)...")
        controller.add_donor()

        # Test delete_donor (giả lập xóa người hiến máu ID=1)
        print("🗑️ Kiểm tra delete_donor với ID=1...")
        controller.delete_donor(1)

        print("✅ Tất cả các phương thức đã được kiểm tra thành công!")

    except Exception as e:
        print(f"❌ Lỗi trong quá trình test: {e}")

    finally:
        print("🔌 Đóng cửa sổ Tkinter.")
        root.mainloop()


if __name__ == "__main__":
    test_controller()

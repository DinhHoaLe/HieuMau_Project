import tkinter as tk
from pygubu.builder import Builder
from tkinter import messagebox


class BloodBankApp:
    def __init__(self, root):
        # Khởi tạo Builder để nạp giao diện
        self.builder = Builder()
        
        try:
            # Nạp file giao diện Pygubu (.ui)
            self.builder.add_from_file('test.ui')
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'interface.ui' không tìm thấy. Vui lòng kiểm tra lại!")
            root.destroy()
            return
        
        # Lấy Frame chính từ file giao diện
        self.mainframe = self.builder.get_object('frame1', root)
        
        # Kết nối các hành động với hàm trong lớp
        self.builder.connect_callbacks(self)

    def on_button_click(self):
        """Hành động khi nhấn nút button1."""
        print("Button clicked!")
        messagebox.showinfo("Thông báo", "Button đã được nhấn!")


if __name__ == '__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Blood Bank Management")
    
    # Khởi tạo ứng dụng
    app = BloodBankApp(root)
    
    # Chạy vòng lặp giao diện
    root.mainloop()

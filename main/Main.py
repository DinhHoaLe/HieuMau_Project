import tkinter as tk
from controller.YeuCauMau_Controller import BloodRequestController

if __name__ == "__main__":
    root = tk.Tk()
    controller = BloodRequestController(root)
    root.mainloop()

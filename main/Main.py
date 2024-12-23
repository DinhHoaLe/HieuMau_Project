import tkinter as tk
from controller.App_Controller import AppController

if __name__ == "__main__":
    root = tk.Tk()
    controller = AppController(root)
    root.mainloop()

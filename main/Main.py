import tkinter as tk
from controller.App_Controller import AppController
from view.Login_View import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    controller = LoginView(root)
    root.mainloop()

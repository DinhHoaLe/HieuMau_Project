import tkinter as tk
from view import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()

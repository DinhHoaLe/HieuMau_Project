import tkinter as tk

def on_button_click(text):
    print(f"Button clicked: {text}")

# Create the main window
root = tk.Tk()
root.title("Quản lý Ngân hàng Máu")
root.geometry("1000x700")
root.configure(bg="#ffffff")

# Create the header frame
header_frame = tk.Frame(root, bg="#610a0a", height=119)
header_frame.pack(fill="x")  # Header luôn giãn theo chiều ngang

# Add the header text
header_text = tk.Label(header_frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter", 18), fg="#ffffff", bg="#610a0a")
header_text.pack(pady=30)  # Khoảng cách padding trong header

# Define a function to create buttons
def create_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        font=("Inter", 10, "bold"),
        fg="#000000",
        bg="#d9d9d9",
        command=lambda: command(text)
    )
    button.pack(side="left", padx=5, pady=10, expand=True, fill="both")  # Các nút trải đều trong khung

# Create the buttons frame
buttons_frame = tk.Frame(root, bg="#ffffff")
buttons_frame.pack(fill="x")  # Nút trải ngang theo cửa sổ

# Create the buttons
create_button(buttons_frame, "Quản lý yêu cầu máu", on_button_click)
create_button(buttons_frame, "Quản lý kho máu", on_button_click)
create_button(buttons_frame, "Quản lý bệnh nhân", on_button_click)
create_button(buttons_frame, "Quản lý người hiến máu", on_button_click)
create_button(buttons_frame, "Quản lý lịch hiến máu", on_button_click)
create_button(buttons_frame, "Thống kê kho máu", on_button_click)

# Run the main loop
root.mainloop()

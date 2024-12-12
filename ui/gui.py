import tkinter as tk

def on_button_click(text):
    print(f"Button clicked: {text}")

# Create the main window
root = tk.Tk()
root.title("Quản lý Ngân hàng Máu")
root.geometry("1000x700")
root.configure(bg="#ffffff")

# Create the header frame
header_frame = tk.Frame(root, bg="#610a0a", height=119, width=1000)
header_frame.pack_propagate(False)
header_frame.pack()

# Add the header text
header_text = tk.Label(header_frame, text="QUẢN LÝ NGÂN HÀNG MÁU", font=("Inter",18 ), fg="#ffffff", bg="#610a0a")
header_text.place(relx=0.5, rely=0.15, anchor="center")


# Define a function to create buttons
def create_button(parent, text, x, y, command):
    button_frame = tk.Frame(parent, width=160, height=48, bg="#d9d9d9", bd=0, relief="flat")
    button_frame.place(x=x, y=y)

    button_label = tk.Label(button_frame, text=text, font=("Inter", 10, "bold"), fg="#000000", bg="#d9d9d9")
    button_label.place(relx=0.5, rely=0.5, anchor="center")

    button_frame.bind("<Button-1>", lambda e: command(text))


# Create the buttons
create_button(root, "Quản lý yêu cầu máu", 3, 58, on_button_click)
create_button(root, "Quản lý kho máu", 170, 58, on_button_click)
create_button(root, "Quản lý bệnh nhân", 337, 58, on_button_click)
create_button(root, "Quản lý người hiến máu", 504, 58, on_button_click)
create_button(root, "Quản lý lịch hiến máu", 837, 58, on_button_click)
create_button(root, "Thống kê kho máu", 670, 58, on_button_click)

# Run the main loop
root.mainloop()

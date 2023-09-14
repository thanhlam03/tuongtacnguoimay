import tkinter as tk

# Hàm xử lý sự kiện khi nút được nhấn
def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Tính toán biểu thức và hiển thị kết quả
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            # Xử lý lỗi nếu có
            screen.set("Lỗi")
    elif text == "C":
        # Xóa màn hình
        screen.set("")
    else:
        # Thêm ký tự vào màn hình
        screen.set(screen.get() + text)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.geometry("400x600")
root.title("Máy tính đơn giản")

# Hiển thị màn hình tính toán
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Arial", 40, "bold"))
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Tạo các nút số và phép tính
button_frame = tk.Frame(root)
button_frame.pack()

# Danh sách các nút và phép tính
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "", "", "", "",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0
for button_text in buttons:
    if button_text:
        # Tạo nút và đặt sự kiện khi nhấn
        button = tk.Button(
            button_frame, text=button_text, font=("Arial", 25, "bold"), padx=20, pady=20
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind("<Button-1>", button_click)
    else:
        # Thêm dòng trống
        label_frame = tk.Frame(button_frame)
        label_frame.grid(row=3, column=1, columnspan=2)

        # Đặt tiêu đề
        tk.Label(label_frame, text=" HoànG Thanh Lâm ", font=("Arial", 16, "bold")).pack(fill="both", expand=True)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Khởi chạy ứng dụng
root.mainloop()

import tkinter as tk

def chose(x):
    if x == 1:
        result_label.config(text="1")
    else:
        result_label.config(text="2")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Simple Graphic Library")

# Tạo các thành phần trong cửa sổ
label = tk.Label(root, text="Choose a number:")
label.pack()

button_1 = tk.Button(root, text="1", command=lambda: chose(1))
button_1.pack()

button_2 = tk.Button(root, text="2", command=lambda: chose(2))
button_2.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Hiển thị cửa sổ
root.mainloop()

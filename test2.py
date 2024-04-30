import tkinter as tk

def open_new_window():
    global new_window
    if not new_window or not new_window.winfo_exists():
        new_window = tk.Toplevel(root)
        new_window.title("Cửa sổ mới")
        new_window.geometry("200x100")
        tk.Label(new_window, text="Đây là cửa sổ mới").pack()
    else:
        new_window.lift()  # Nếu đã mở, nâng cấp cửa sổ lên trên cùng

root = tk.Tk()
root.title("Giao diện đồ họa")

new_window = None

button = tk.Button(root, text="Mở cửa sổ mới", command=open_new_window)
button.pack()

root.mainloop()

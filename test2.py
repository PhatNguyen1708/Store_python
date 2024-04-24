import tkinter as tk
from tkinter import ttk

def add_to_treeview():
    # Lấy số từ Entry 1
    number = entry1.get()
    
    # Thêm số vào Treeview dưới dạng chuỗi
    tree.insert("", "end", values=(number,))
    
    # Xóa dữ liệu trong Entry 1 sau khi thêm vào Treeview
    entry1.delete(0, tk.END)

def get_from_treeview(event=None):
    # Xác định dòng được chọn trong Treeview
    selected_row = tree.identify_row(event.y)
    
    # Nếu có dòng được chọn
    if selected_row:
        # Lấy thông tin từ dòng đó
        item = tree.item(selected_row)
        value = item['values'][0]
        
        # Hiển thị giá trị trong Entry 2
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, value)

# Tạo cửa sổ
root = tk.Tk()
root.title("Entry, Treeview, và chuyển giữa chúng")

# Tạo Entry 1
entry1 = tk.Entry(root, width=40)
entry1.pack(padx=20, pady=10)

# Tạo nút để thêm số từ Entry 1 vào Treeview
add_button = tk.Button(root, text="Thêm vào Treeview", command=add_to_treeview)
add_button.pack()

# Tạo Treeview
tree = ttk.Treeview(root, columns=("Number",), show="headings")
tree.heading("Number", text="Number")
tree.pack(padx=20, pady=10)

# Binding sự kiện click chuột vào Treeview để lấy dữ liệu từ dòng được chọn
tree.bind("<ButtonRelease-1>", get_from_treeview)

# Tạo Entry 2
entry2 = tk.Entry(root, width=40)
entry2.pack(padx=20, pady=10)

# Chạy vòng lặp chờ sự kiện
root.mainloop()

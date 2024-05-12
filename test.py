import tkinter as tk
from tkinter import ttk

# Dữ liệu của bạn
data = [
    {
        "username": "halogira",
        "cart": [
            {"name": "Bánh"},
            {"name": "Kẹo"}
        ]
    },
       {
        "username": "halogira",
        "cart": [
            {"name": "Bánh"},
            {"name": "Kẹo"}
        ]
    }
]

def populate_tree(tree, data):
    for user in data:
        username = user["username"]
        cart_items = user["cart"]
        user_node = tree.insert("", "end", text=username)

        for item in cart_items:
            item_name = item["name"]
            tree.insert(user_node, "end", text=item_name)

# Tạo cửa sổ
root = tk.Tk()
root.title("TreeView Example")

# Tạo một TreeView
tree = ttk.Treeview(root)
tree["columns"] = ("Name")
tree.column("#0", width=120, minwidth=120, stretch=tk.NO)
tree.column("Name", width=120, minwidth=120, stretch=tk.NO)
tree.heading("#0", text="Username", anchor=tk.W)
tree.heading("Name", text="Cart Item", anchor=tk.W)

# Hiển thị dữ liệu trên TreeView
populate_tree(tree, data)

# Đặt TreeView vào cửa sổ
tree.pack(expand=True, fill=tk.BOTH)

# Chạy ứng dụng
root.mainloop()

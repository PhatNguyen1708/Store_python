import tkinter as tk

def clear_text():
    text_widget.delete('1.0', tk.END)

root = tk.Tk()
root.title("Xóa dữ liệu trong Text Widget")

text_widget = tk.Text(root)
text_widget.pack()

clear_button = tk.Button(root, text="Xóa", command=clear_text)
clear_button.pack()

root.mainloop()

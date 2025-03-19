import tkinter as tk
from tkinter import ttk

def binary_decoder():
    G1 = int(entry_G1.get())
    G2A_L = int(entry_G2A_L.get())
    G2B_L = int(entry_G2B_L.get())

    if G1 != 1 or G2A_L != 0 or G2B_L != 0:
        result_label.config(text="Decoder is off.", foreground="red")
        update_table([1] * 8, G1, G2A_L, G2B_L)
        return

    C = int(entry_C.get())
    B = int(entry_B.get())
    A = int(entry_A.get())

    output_index = (C << 2) | (B << 1) | A

    outputs = [1] * 8
    outputs[output_index] = 0 

    result_label.config(text=f"Active Output: Y{output_index}_L", foreground="green")
    update_table(outputs, G1, G2A_L, G2B_L, C, B, A)

def update_table(outputs, G1, G2A_L, G2B_L, C=None, B=None, A=None):
    for i in range(8):
        tree.item(f"Y{i}_L", values=(f"Y{i}_L", outputs[i]))

root = tk.Tk()
root.title("Decoder 3:8")

ttk.Label(root, text="G1:").grid(row=0, column=0)
entry_G1 = ttk.Entry(root, width=5)
entry_G1.grid(row=0, column=1)
entry_G1.insert(0, "1")

ttk.Label(root, text="G2A_L:").grid(row=0, column=2)
entry_G2A_L = ttk.Entry(root, width=5)
entry_G2A_L.grid(row=0, column=3)
entry_G2A_L.insert(0, "0")

ttk.Label(root, text="G2B_L:").grid(row=0, column=4)
entry_G2B_L = ttk.Entry(root, width=5)
entry_G2B_L.grid(row=0, column=5)
entry_G2B_L.insert(0, "0")

ttk.Label(root, text="C:").grid(row=1, column=0)
entry_C = ttk.Entry(root, width=5)
entry_C.grid(row=1, column=1)

ttk.Label(root, text="B:").grid(row=1, column=2)
entry_B = ttk.Entry(root, width=5)
entry_B.grid(row=1, column=3)

ttk.Label(root, text="A:").grid(row=1, column=4)
entry_A = ttk.Entry(root, width=5)
entry_A.grid(row=1, column=5)

calculate_button = ttk.Button(root, text="Decode", command=binary_decoder)
calculate_button.grid(row=2, column=0, columnspan=6, pady=10)

result_label = ttk.Label(root, text="Feel free to test every input...", foreground="green")
result_label.grid(row=3, column=0, columnspan=6)


columns = ("Έξοδος", "Τιμή")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
tree.heading("Έξοδος", text="Έξοδος")
tree.heading("Τιμή", text="Τιμή")

for i in range(8):
    tree.insert("", "end", iid=f"Y{i}_L", values=(f"Y{i}_L", "1"))

tree.grid(row=5, column=0, columnspan=6, pady=10)

root.mainloop()
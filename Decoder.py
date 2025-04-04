import tkinter as tk
from tkinter import ttk

def binary_decoder():
    G1    = int(entry_G1.get())		        #get Enablers
    G2A_L = int(entry_G2A_L.get())          
    G2B_L = int(entry_G2B_L.get())

    if G1 != 1 or G2A_L != 0 or G2B_L != 0:
        result_label.config(text="Decoder is off.", foreground="red")
        update_table([1] * 8, G1, G2A_L, G2B_L)
        return

    C = int(entry_C.get())			        #get Entries
    B = int(entry_B.get())
    A = int(entry_A.get())

    if A!=0 or A!=1 or B!=0 or B!=1 or C!=0 or C!=1:
        result_label.config(text=f"Invalid inputs. Please only type 1 or 0",foreground="red")

    output_index = (C << 2) | (B << 1) | A 	#Bitwise OR of C,B,A (C shifted 2 times, B 1 time) 
	                                        #e.g. CBA=111, C=100, B=010, A=001, so C|B|A = 111 = 7 so output index is 7

    outputs = [1] * 8						#8 elements list, all initialized to 1
    outputs[output_index] = 0 				#from the previous example outputs(7) = 0 and the others remain 1 (Y7)
    
    result_label.config(text=f"Active Output: Y{output_index}_L", foreground="green")
    update_table(outputs, G1, G2A_L, G2B_L, C, B, A)

def update_table(outputs, G1, G2A_L, G2B_L, C=None, B=None, A=None):
    for i in range(8):
        tree.item(f"Y{i}_L", values=(f"Y{i}_L", outputs[i]))

#tkinter boring stuff:
root = tk.Tk()
root.title("Decoder 3:8")

ttk.Label(root, text="G1:").grid(row=0, column=0)
entry_G1 = ttk.Entry(root, width=5)
entry_G1.grid(row=0, column=1)
entry_G1.insert(0, "1")                     #initial value for G1

ttk.Label(root, text="G2A_L:").grid(row=0, column=2)
entry_G2A_L = ttk.Entry(root, width=5)
entry_G2A_L.grid(row=0, column=3)
entry_G2A_L.insert(0, "0")                  #initial value for G2A_L

ttk.Label(root, text="G2B_L:").grid(row=0, column=4)
entry_G2B_L = ttk.Entry(root, width=5)
entry_G2B_L.grid(row=0, column=5)
entry_G2B_L.insert(0, "0")                  #initial value for G2B_L

ttk.Label(root, text="C:").grid(row=1, column=0)
entry_C = ttk.Entry(root, width=5)
entry_C.grid(row=1, column=1)  
entry_C.insert(0, "0")                      #initial value for C

ttk.Label(root, text="B:").grid(row=1, column=2)
entry_B = ttk.Entry(root, width=5)
entry_B.grid(row=1, column=3)
entry_B.insert(0,"0")                       #initial value for B

ttk.Label(root, text="A:").grid(row=1, column=4)
entry_A = ttk.Entry(root, width=5)
entry_A.grid(row=1, column=5)
entry_A.insert(0,"1")                       #initial value for A

calculate_button = ttk.Button(root, text="Decode", command=binary_decoder)
calculate_button.grid(row=2, column=0, columnspan=6, pady=10)

result_label = ttk.Label(root, text="Feel free to test every input...", foreground="green")
result_label.grid(row=3, column=0, columnspan=6)

columns = ("Output", "Value")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
tree.heading("Output", text="Output")
tree.heading("Value", text="Value")

for i in range(8):
    tree.insert("", "end", iid=f"Y{i}_L", values=(f"Y{i}_L", "1"))

tree.grid(row=5, column=0, columnspan=6, pady=10)

root.mainloop()

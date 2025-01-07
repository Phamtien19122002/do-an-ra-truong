import tkinter as tk
from tkinter import ttk
from src.main_create import *
from src.main_tkinter import *

def button_spec_handler():
    title_spec.pack_forget()
    tree_spec.pack_forget()
    slip_spec.pack_forget()
    txt_spec.config(text="Loading...", font=("Arial", 50))
    txt_spec.pack(pady=20)
    root.update()
    try:
        button_spec(entry_name.get("1.0", tk.END).strip(), entry_spec.get("1.0", tk.END).strip(), 
                    entry_code.get("1.0", tk.END).strip(), tree_spec, slip_spec)
        title_spec.pack(pady=(15,0))
        tree_spec.pack()
        slip_spec.pack()
    finally:
        txt_spec.pack_forget()

def button_code_handler():
    title_code.pack_forget()
    tree_code.pack_forget()
    slip_code.pack_forget()
    txt_code.config(text="Loading...", font=("Arial", 50))
    txt_code.pack(pady=20)
    root.update()
    try:
        button_code(entry_name.get("1.0", tk.END).strip(), entry_code.get("1.0", tk.END).strip(), tree_code, slip_code)
        title_code.pack(pady=(15,0))
        tree_code.pack()
        slip_code.pack() 
    finally:
        txt_code.pack_forget()   

def button_merge_handler():
    title_merge.pack_forget()
    tree_merge.pack_forget()
    slip_merge.pack_forget() 
    txt_merge.config(text="Loading...", font=("Arial", 50))
    txt_merge.pack(pady=20)
    root.update()
    try:
        button_merge(entry_name.get("1.0", tk.END).strip(), tree_merge, slip_merge)
        title_merge.pack(pady=(15,0))
        tree_merge.pack()
        slip_merge.pack() 
    finally:
        txt_merge.pack_forget()  

root = tk.Tk()
root.geometry("1250x960")
root.title("Generate Unit test using LLM!")

path_frame = tk.Frame(root)
path_frame.pack(fill=tk.X, padx=80, pady=15)
tk.Label(path_frame, text="Name for save Test Cases' path: ", width=25).pack(side=tk.LEFT, padx=10)
entry_name = tk.Text(path_frame, height=1)
entry_name.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tc_frame = tk.Frame(root)
tc_frame.pack(fill=tk.X, pady=15)

left_frame = tk.Frame(tc_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame1 = tk.Frame(left_frame)
frame1.pack()
entry_spec = tk.Text(left_frame, height=12, width=75)
entry_spec.pack()
tk.Label(frame1, text="Specifications:", width=15).pack(side=tk.LEFT)
tk.Button(frame1, text="Import file", command=lambda: open_file(entry_spec)).pack(side=tk.RIGHT)
tk.Button(left_frame, text="Generate specifications' test cases", command=lambda: button_spec_handler()).pack()
txt_spec = tk.Label(left_frame, text="Specification test suite will be displayed here.")
txt_spec.pack(pady=100)
title_spec = tk.Label(left_frame, text="Generated test cases from specifications")
columns_spec = ("data", "expected", "result")
tree_spec = ttk.Treeview(left_frame, columns=columns_spec, show="headings")
tree_spec.heading("data", text="Input data")
tree_spec.heading("expected", text="Computed output")
tree_spec.heading("result", text="Test result")
slip_spec = tk.Label(left_frame, text="")

right_frame = tk.Frame(tc_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame2 = tk.Frame(right_frame)
frame2.pack()
entry_code = tk.Text(right_frame, height=12, width=75)
entry_code.pack(padx=5)
tk.Label(frame2, text="Source code:", width=15).pack(side=tk.LEFT)
tk.Button(frame2, text="Import file", command=lambda: open_file(entry_code)).pack(side=tk.RIGHT)
tk.Button(right_frame, text="Generate code's test cases", command=lambda: button_code_handler()).pack()
txt_code = tk.Label(right_frame, text="Code test suite will be displayed here.")
txt_code.pack(pady=100)
title_code = tk.Label(right_frame, text="Generated test cases from source code")
columns_code = ("data", "expected", "result")
tree_code = ttk.Treeview(right_frame, columns=columns_code, show="headings")
tree_code.heading("data", text="Input data")
tree_code.heading("expected", text="Computed output")
tree_code.heading("result", text="Test result")
slip_code = tk.Label(right_frame, text="")

selected_frame = tk.Frame(root)
selected_frame.pack(fill=tk.X, pady=10)

tk.Button(selected_frame, text="Merge test cases", command=lambda: button_merge_handler()).pack()
txt_merge =  tk.Label(selected_frame, text="Selected Test Cases will be displayed here.")
txt_merge.pack(pady=100)
title_merge = tk.Label(selected_frame, text="Selected Test Cases")
columns_merge = ("data", "expected", "result")
tree_merge = ttk.Treeview(selected_frame, columns=columns_merge, show="headings")
tree_merge.heading("data", text="Input data")
tree_merge.heading("expected", text="Computed Output")
tree_merge.heading("result", text="Test result")
slip_merge = tk.Label(selected_frame, text="")

root.mainloop()
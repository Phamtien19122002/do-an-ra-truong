import tkinter as tk
from tkinter import ttk
from main_create import *
from main_merge import *
from main_tkinter import *

root = tk.Tk()
root.geometry("1250x960")
root.title("Generate Unit test using LLM!")

path_frame = tk.Frame(root)
path_frame.pack(fill=tk.X, padx=80, pady=10)
tk.Label(path_frame, text="Name for save TCs' file: ", width=20).pack(side=tk.LEFT, padx=10)
entry_name = tk.Text(path_frame, height=1)
entry_name.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tc_frame = tk.Frame(root)
tc_frame.pack(fill=tk.X, pady=10)

left_frame = tk.Frame(tc_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame1 = tk.Frame(left_frame)
frame1.pack()
entry_spec = tk.Text(left_frame, height=15, width=75)
entry_spec.pack(padx=5)
tk.Label(frame1, text="Spec:", width=15).pack(side=tk.LEFT)
tk.Button(frame1, text="Open file", command=lambda: open_file(entry_spec)).pack(side=tk.RIGHT)
button1 = tk.Button(left_frame, text="Generate spec's TCs", command=lambda: spec_button(entry_name.get("1.0", tk.END).strip(), entry_spec.get("1.0", tk.END).strip(), entry_code.get("1.0", tk.END).strip(), tree_spec))
button1.pack()
tk.Label(left_frame, text="Generated TCs table from Spec").pack(pady=10)
columns_spec = ("data", "actual", "expected")
tree_spec = ttk.Treeview(left_frame, columns=columns_spec, show="headings")
tree_spec.heading("data", text="Data Test")
tree_spec.heading("actual", text="Actual Output")
tree_spec.heading("expected", text="Expected Output")
tree_spec.pack(padx=10)

right_frame = tk.Frame(tc_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame2 = tk.Frame(right_frame)
frame2.pack()
entry_code = tk.Text(right_frame, height=15, width=75)
entry_code.pack(padx=5)
tk.Label(frame2, text="Code:", width=15).pack(side=tk.LEFT)
tk.Button(frame2, text="Open file", command=lambda: open_file(entry_code)).pack(side=tk.RIGHT)
tk.Button(right_frame, text="Generate code's TCs", command=lambda: code_button(entry_name.get("1.0", tk.END).strip(), entry_code.get("1.0", tk.END).strip(), tree_code)).pack()
tk.Label(right_frame, text="Generated TCs table from Code").pack(pady=10)
columns_code = ("data", "actual", "expected")
tree_code = ttk.Treeview(right_frame, columns=columns_code, show="headings")
tree_code.heading("data", text="Data Test")
tree_code.heading("actual", text="Actual Output")
tree_code.heading("expected", text="Expected Output")
tree_code.pack(padx=10)

selected_frame = tk.Frame(root)
selected_frame.pack(fill=tk.X, pady=10)

tk.Button(selected_frame, text="Merge TCs").pack(pady=5)
tk.Label(selected_frame, text="Selected TCs table").pack(pady=5)
columns_merge = ("data", "actual", "expected")
tree_merge = ttk.Treeview(selected_frame, columns=columns_merge, show="headings")
tree_merge.heading("data", text="Data Test")
tree_merge.heading("actual", text="Actual Output")
tree_merge.heading("expected", text="Expected Output")
tree_merge.pack(padx=10)

root.mainloop()
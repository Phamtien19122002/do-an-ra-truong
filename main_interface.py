import tkinter as tk
from tkinter import ttk
from main_create import *
from main_merge import *
from main_tkinter import *

root = tk.Tk()
root.geometry("1250x990")
root.title("Generate Unit test using LLM!")

path_frame = tk.Frame(root)
path_frame.pack(fill=tk.X, padx=80, pady=15)
tk.Label(path_frame, text="Name for save TCs' file: ", width=20).pack(side=tk.LEFT, padx=10)
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
tk.Label(frame1, text="Spec:", width=15).pack(side=tk.LEFT)
tk.Button(frame1, text="Import file", command=lambda: open_file(entry_spec)).pack(side=tk.RIGHT)
button1 = tk.Button(left_frame, text="Generate spec's TCs", command=lambda: button_spec(entry_name.get("1.0", tk.END).strip(), entry_spec.get("1.0", tk.END).strip(), entry_code.get("1.0", tk.END).strip(), tree_spec, slip_spec))
button1.pack()
tk.Label(left_frame, text="Generated TCs table from Spec").pack(pady=(15,0))
columns_spec = ("data", "expected", "result")
tree_spec = ttk.Treeview(left_frame, columns=columns_spec, show="headings")
tree_spec.heading("data", text="Data test")
tree_spec.heading("expected", text="Expected output")
tree_spec.heading("result", text="Result")
tree_spec.pack(padx=5)
slip_spec = tk.Label(left_frame, text="")
slip_spec.pack()

right_frame = tk.Frame(tc_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame2 = tk.Frame(right_frame)
frame2.pack()
entry_code = tk.Text(right_frame, height=12, width=75)
entry_code.pack(padx=5)
tk.Label(frame2, text="Code:", width=15).pack(side=tk.LEFT)
tk.Button(frame2, text="Import file", command=lambda: open_file(entry_code)).pack(side=tk.RIGHT)
tk.Button(right_frame, text="Generate code's TCs", command=lambda: button_code(entry_name.get("1.0", tk.END).strip(), entry_code.get("1.0", tk.END).strip(), tree_code, slip_code)).pack()
tk.Label(right_frame, text="Generated TCs table from Code").pack(pady=(15,0))
columns_code = ("data", "expected", "result")
tree_code = ttk.Treeview(right_frame, columns=columns_code, show="headings")
tree_code.heading("data", text="Data test")
tree_code.heading("expected", text="Expected output")
tree_code.heading("result", text="Result")
tree_code.pack(padx=5)
slip_code = tk.Label(right_frame, text="")
slip_code.pack()

selected_frame = tk.Frame(root)
selected_frame.pack(fill=tk.X, pady=10)

tk.Button(selected_frame, text="Merge TCs", command=lambda: merge_button(entry_name.get("1.0", tk.END).strip(), tree_merge, slip_merge)).pack()
tk.Label(selected_frame, text="Selected TCs table").pack(pady=(15,0))
columns_merge = ("data", "expected", "result")
tree_merge = ttk.Treeview(selected_frame, columns=columns_merge, show="headings")
tree_merge.heading("data", text="Data Test")
tree_merge.heading("expected", text="Expected Output")
tree_merge.heading("result", text="Result")
tree_merge.pack()
slip_merge = tk.Label(selected_frame, text="")
slip_merge.pack()

root.mainloop()
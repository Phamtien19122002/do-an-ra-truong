import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from main_create import *
from main_merge import *

def generate_from_spec(entry):
    spec = entry.get("1.0", tk.END).strip()
    if not spec:
        messagebox.showwarning("Warning", "Please enter the spec.")
        return
    try:
        function_name = get_function_name_from_code(spec)  
        import_function = convert_function_path(entry_spec_name)
        test_spec = generate_test(prompt_spec(function_name, import_function, spec))
        missed_spec = estimate(test_spec, spec)
        if missed_spec:
            test_spec += generate_test(prompt_miss(function_name, import_function, missed_spec, spec))
        display_test_cases(test_spec, tree_spec)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_from_code(entry):
    code = entry.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Warning", "Please enter the code.")
        return
    try:
        function_name = get_function_name_from_code(code) 
        import_function = convert_function_path(entry_code_name) 
        save_code()
        test_code = generate_test(prompt_code(function_name, import_function, code))
        missed_code = estimate(test_code, code)
        if missed_code:
            test_code += generate_test(prompt_miss(function_name, import_function, missed_code, code))
        display_test_cases(test_code, tree_code)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def display_test_cases(test_cases, tree):
    for row in tree.get_children():
        tree.delete(row)

    for tc in test_cases:
        tree.insert("", "end", values=(tc['data'], tc['output'], tc['expected']))

def save_spec(entry):
    spec = entry.get("1.0", tk.END).strip()
    if not spec:
        messagebox.showwarning("Warning", "Please enter the spec.")
        return
    default_filename = f"spec_{entry_spec_name}.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_filename, filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(spec)
        messagebox.showinfo("Success", f"Spec saved to {file_path}")
        return file_path

def save_code(entry):
    code = entry.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Warning", "Please enter the code.")
        return
    default_filename = f"code_{entry_code_name}.py"
    file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=default_filename, filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)
        messagebox.showinfo("Success", f"Code saved to {file_path}")
        return file_path

# Tạo giao diện
root = tk.Tk()
root.geometry("1800x1000")
root.title("Generate Unit test using LLM!")

# Spec
frame_spec = tk.Frame(root)
frame_spec.pack(fill=tk.BOTH, expand=True)

frame_left1 = tk.Frame(frame_spec)
frame_left1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_right1 = tk.Frame(frame_spec)
frame_right1.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frame1 = tk.Frame(frame_left1)
frame1.pack(fill=tk.X, pady=10)
tk.Label(frame1, text="Spec name:", width=20).pack(side=tk.LEFT)
entry_spec_name = tk.Text(frame1, height=1, width=100)
entry_spec_name.pack(side=tk.LEFT, padx=5)

frame2 = tk.Frame(frame_left1)
frame2.pack(fill=tk.X, pady=5)
tk.Label(frame2, text="Spec:", width=20).pack(side=tk.LEFT)
entry_spec = tk.Text(frame2, height=15, width=100)
entry_spec.pack(side=tk.LEFT, padx=5)

frame3 = tk.Frame(frame_right1)
frame3.pack(fill=tk.X, pady=10)
columns_spec = ("data", "output", "expected")
tree_spec = ttk.Treeview(frame3, columns=columns_spec, show="headings")
tree_spec.heading("data", text="Data Test")
tree_spec.heading("output", text="Actual Output")
tree_spec.heading("expected", text="Expected Output")
tree_spec.pack(fill=tk.X)
tk.Button(root, text="Generate TC from Spec", command=generate_from_spec(entry_spec)).pack()

# Code
frame_code = tk.Frame(root)
frame_code.pack(fill=tk.BOTH, expand=True)

frame_left2 = tk.Frame(frame_code)
frame_left2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_right2 = tk.Frame(frame_code)
frame_right2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frame4 = tk.Frame(frame_left2)
frame4.pack(fill=tk.X, pady=10)
tk.Label(frame4, text="Function name:", width=20).pack(side=tk.LEFT)
entry_code_name = tk.Text(frame4, height=1, width=100)
entry_code_name.pack(side=tk.LEFT, padx=5)

frame5 = tk.Frame(frame_left2)
frame5.pack(fill=tk.X, pady=5)
tk.Label(frame5, text="Function:", width=20).pack(side=tk.LEFT)
entry_code = tk.Text(frame5, height=15, width=100)
entry_code.pack(side=tk.LEFT, padx=5)

frame6 = tk.Frame(frame_right2)
frame6.pack(fill=tk.X, pady=10)
columns_code = ("data", "actual", "expected")
tree_code = ttk.Treeview(frame6, columns=columns_code, show="headings")
tree_code.heading("data", text="Data Test")
tree_code.heading("actual", text="Actual Output")
tree_code.heading("expected", text="Expected Output")
tree_code.pack(fill=tk.X)
tk.Button(root, text="Generate TC from Code", command=generate_from_code(entry_code)).pack()

root.mainloop()
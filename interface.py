import tkinter as tk
from tkinter import messagebox
from main_1 import generate_and_run_tests

def run_tests_gui():
    function_path = entry_function_path.get()
    spec_path = entry_spec_path.get()
    merge_path = entry_merge_path.get()
    try:
        generate_and_run_tests(function_path, spec_path, merge_path)
        messagebox.showinfo("Success", "Tests generated and run successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tạo giao diện
root = tk.Tk()
root.title("Test Suite Generator")

tk.Label(root, text="Function Path:").pack()
entry_function_path = tk.Entry(root)
entry_function_path.pack()

tk.Label(root, text="Spec Path:").pack()
entry_spec_path = tk.Entry(root)
entry_spec_path.pack()

tk.Label(root, text="Merge Path:").pack()
entry_merge_path = tk.Entry(root)
entry_merge_path.pack()

tk.Button(root, text="Generate and Run Tests", command=run_tests_gui).pack()

root.mainloop()
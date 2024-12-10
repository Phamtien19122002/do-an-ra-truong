import tkinter as tk
from tkinter import messagebox, filedialog
import importlib
from main_create import *
from main_merge import *

def open_file(text_widget):
    file_path = filedialog.askopenfilename(
        title="Chọn tệp",
        filetypes=(("Tất cả các tệp", "*.*"), ("Tệp văn bản", "*.txt"))
    )
    if file_path:
        print(f"Tệp đã chọn: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)  
            text_widget.insert(tk.END, content) 

def save_spec(name, spec):
    filename = f"spec_{name}.txt"
    # file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=filename, filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(spec)
        return filename

def save_code(name, code):
    filename = f"code_{name}.py"
    # file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=filename, filetypes=[("Python files", "*.py")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(code)
        return filename

def button_spec(name, spec, code, tree, slip):
    if not name or not spec or not code:
        messagebox.showwarning("Warning", "Please input all above fields.")
        return
    try:
        save_spec(name, spec)
        function_name = get_function_name_from_code(code)
        tc = generate_test(prompt_speci(name, spec, function_name))
        missed_code = estimate(tc, code)
        if missed_code:
            tc += generate_test(prompt_miss(function_name, f"{name}", missed_code, code))
        save_tc_spec(name, tc, tree)
        display_pass_fail(f"TC_spec/spec_{name}_tc.py", slip)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def button_code(name, code, tree, slip):
    if not name or not code:
        messagebox.showwarning("Warning", "Please input both above fields: \n - name, \n - code.")
        return
    try:
        save_code(name, code)
        tc = generate_test(prompt_codei(name, code))
        missed_code = estimate(tc, code)
        if missed_code:
            tc += generate_test(prompt_miss(get_function_name_from_code(code), f"{name}", missed_code, code))
        save_tc_code(name, tc, tree)
        display_pass_fail(f"TC_function/code_{name}_tc.py", slip)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_tc_spec(name, tc, tree_spec):
    filename = f"TC_spec/spec_{name}_tc.py"
    # file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=filename, filetypes=[("Python files", "*.py")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(tc)
        display_test_cases(filename, tree_spec)
        return filename

def save_tc_code(name, tc, tree_code):
    filename = f"TC_function/code_{name}_tc.py"
    # file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=filename, filetypes=[("Python files", "*.py")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(tc)
        display_test_cases(filename, tree_code)
        return filename

def display_test_cases(file_path, tree):
    test_cases = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        module_name = ""
        function_name = ""
        for line in lines:
            if "from" in line:
                module_name = line.split("from")[1].split("import")[0].strip()
                function_name = line.split("import")[1].strip()
                module = importlib.import_module(module_name)
                globals()[function_name] =  getattr(module, function_name)
            if "assert" in line:
                data = line.split("(")[1].split(")")[0].strip()
                expected = line.split("==")[1].strip()
                try:
                    result = eval(line.split("assert")[1].strip(), globals())
                except AssertionError: 
                    result = "Fail"
                test_cases.append({'data': data, 'expected': expected, 'result': result})
    for row in tree.get_children():
        tree.delete(row)
    for tc in test_cases:
        tree.insert("", "end", values=(tc['data'], tc['expected'], tc['result']))

def display_pass_fail(test_file, label):
    output = ""
    try:
        result = subprocess.run(
            ["python3", "-m", "slipcover", "-m", "pytest", test_file], check=True, text=True, capture_output=True
        )
        output = result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        output = e.stdout.splitlines()
    for line in output:
        if ("failed" in line or "passed" in line) and "in" in line:
            label.config(text=line.split("= ")[1].split(" in")[0].strip())

def spec_button(name, spec, code, tree_spec, slip):
    if not name or not spec or not code:
        messagebox.showwarning("Warning", "Hãy nhập đủ 3 trường trên: \n - name, \n - spec, \n - code.")
        return 
    save_spec(name, spec)
    tc = generate_test(prompt_speci(name, spec, code))
    save_tc_spec(name, tc, tree_spec)
    display_pass_fail(f"spec_{name}_tc.py", slip)

def code_button(name, code, tree, slip):
    if not name or not code:
        messagebox.showwarning("Warning", "Please input both above fields: \n - name, \n - code.")
        return 
    save_code(name, code)
    tc = generate_test(prompt_codei(name, code))
    save_tc_code(name, tc, tree)
    display_pass_fail(f"TC_function/code_{name}_tc.py", slip)

def merge_button(name, merge_tree):
    merge(f"TC_spec/spec_{name}_tc.py", f"TC_function/code_{name}_tc.py", f"TC_merge/merge_{name}_tc.py")
    display_test_cases(f"TC_merge/merge_{name}_tc.py", merge_tree)
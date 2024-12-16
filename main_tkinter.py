import tkinter as tk
import importlib
from tkinter import messagebox, filedialog
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

def extract_report_table(output):
    lines = output.splitlines()
    report_lines = []
    start_recording = False
    for line in lines:
        if line.startswith("File"):
            start_recording = True
        if start_recording:
            if line.strip():  # Nếu dòng không rỗng
                report_lines.append(line)
            else:  # Dừng khi gặp dòng rỗng
                break

    return "\n".join(report_lines)

def save_tc_spec(filename, tc):
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(tc)
        return filename

def save_tc_code(filename, tc):
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(tc)
        return filename

def display_test_case(file_path, tree):
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

def display_pass_fail(path, label):
    output = slipcover(path).splitlines()
    for line in output:
        if ("failed" in line or "passed" in line) and "in" in line:
            label.config(text=line.split("= ")[1].split(" in")[0].strip())

def button_spec(name, spec, code, tree, slip):
    if not name or not spec or not code:
        messagebox.showwarning("Warning", "Please input all above fields.")
        return
    try:
        save_spec(name, spec)
        tc_path = f"TC_spec/spec_{name}_tc.py"
        tc = generate_test(prompt_spec(name, spec, get_function_name_from_code(code)))
        save_tc_spec(tc_path, tc)
        missed_code = find_miss(tc_path, f"code_{name}.py")
        if missed_code:
            tc += generate_test(prompt_miss(get_function_name_from_code(code), f"code_{name}", missed_code, code))
        save_tc_spec(tc_path, tc)
        count = 3
        while count > 0:
            failure = extract_wrong(tc_path)
            if failure:
                tc = generate_test(prompt_wrong(read_file(f"spec_{name}.txt"), failure, read_file(tc_path)))
                update_wrong(tc, tc_path)
            else:
                count = 0
            count -= 1
        display_test_case(tc_path, tree)
        display_pass_fail(tc_path, slip)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def button_code(name, code, tree, slip):
    if not name or not code:
        messagebox.showwarning("Warning", "Please input both above fields: \n - name, \n - code.")
        return
    try:
        save_code(name, code)
        tc_path = f"TC_function/code_{name}_tc.py"
        tc = generate_test(prompt_code(name, code))
        save_tc_code(tc_path, tc)
        missed_code = find_miss(tc_path, f"code_{name}.py")
        if missed_code:
            tc += generate_test(prompt_miss(get_function_name_from_code(code), f"code_{name}", missed_code, code))
        save_tc_code(tc_path, tc)
        count = 3
        while count > 0:
            failure = extract_wrong(tc_path)
            if failure:
                tc = generate_test(prompt_wrong(read_file(f"spec_{name}.txt"), failure, read_file(tc_path)))
                update_wrong(tc, tc_path)
            else:
                count = 0
            count -= 1
        display_test_case(tc_path, tree)
        display_pass_fail(tc_path, slip)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def merge_button(name, tree, slip):
    tc_path = f"TC_merge/merge_{name}_tc.py"
    merge(f"TC_spec/spec_{name}_tc.py", f"TC_function/code_{name}_tc.py", tc_path)
    display_test_case(tc_path, tree)
    display_pass_fail(tc_path, slip)
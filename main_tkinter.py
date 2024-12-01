import tkinter as tk
from tkinter import messagebox, filedialog
from main_create import *
from main_merge import *

def generate_from_spec(entry_spec_name, entry_spec, tree_spec):
    spec = entry_spec.get("1.0", tk.END).strip()
    if not spec:
        messagebox.showwarning("Warning", "Please enter the spec.")
        return
    else:
        save_spec
    try:
        function_name = get_function_name_from_code(spec)  
        print(function_name)
        import_function = convert_function_path(entry_spec_name)
        test_spec = generate_test(prompt_spec(function_name, import_function, spec))
        missed_spec = estimate(test_spec, spec)
        if missed_spec:
            test_spec += generate_test(prompt_miss(function_name, import_function, missed_spec, spec))
        display_test_cases(test_spec, tree_spec)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_from_code(entry_code_name, entry_code, tree_code):
    code = entry_code.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Warning", "Please enter the code.")
        return
    try:
        function_name = get_function_name_from_code(code) 
        import_function = convert_function_path(entry_code_name) 
        save_code
        test_code = generate_test(prompt_code(function_name, import_function, code))
        missed_code = estimate(test_code, code)
        if missed_code:
            test_code += generate_test(prompt_miss(function_name, import_function, missed_code, code))
        display_test_cases(test_code, tree_code)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def display_test_cases(file_path, tree_spec):
    test_cases = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if "assert" in line:
                data = line.split("(")[1].split(")")[0].strip()
                actual = line.split("==")[1].strip()
                # try:
                #     exec(line.strip(), globals())
                #     expected = "same"
                # except AssertionError:
                #     expected = "not same"
                test_cases.append({'data': data, 'actual': actual, 'expected': "expected"})
    for row in tree_spec.get_children():
        tree_spec.delete(row)
    for tc in test_cases:
        tree_spec.insert("", "end", values=(tc['data'], tc['actual'], tc['expected']))

def save_spec(spec_name, spec):
    if not spec:
        messagebox.showwarning("Warning", "Please enter the spec.")
        return
    default_filename = f"spec_{spec_name}.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_filename, filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(spec)
        return file_path

def save_code(code_name, code):
    if not code:
        messagebox.showwarning("Warning", "Please enter the code.")
        return
    default_filename = f"code_{code_name}.py"
    file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=default_filename, filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)
        return file_path

def save_tc_spec(name, tc, tree_spec):
    default_filename = f"spec_{name}_tc.py"
    file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=default_filename, filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(tc)
        display_test_cases(file_path, tree_spec)
        return file_path

def save_tc_code(name, tc, tree_code):
    default_filename = f"code_{name}_tc.py"
    file_path = filedialog.asksaveasfilename(defaultextension=".py", initialfile=default_filename, filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(tc)
        display_test_cases(file_path, tree_code)
        return file_path

def show_mess(title, message):
    messagebox.showinfo(title, message)

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

def spec_button(spec_name, spec, code, tree_spec):
    if not spec_name or not spec or not code:
        show_mess("Warning!", "Hãy nhập đủ 3 trường trên: \n - name, \n - spec, \n - code.")
        return 
    save_spec(spec_name, spec)
    tc = generate_test(prompt_speci(spec_name, spec, code))
    save_tc_spec(spec_name, tc, tree_spec)
    show_mess("Test case suite generated from Spec automatically", generate_test(tc))

def code_button(code_name, code, tree_code):
    if not code_name or not code:
        show_mess("Warning!", "Hãy nhập đủ 2 trường trên: \n - name, \n - code.")
        return 
    save_code(code_name, code)
    tc = generate_test(prompt_codei(code_name, code))
    save_tc_code(code_name, tc, tree_code)
    show_mess("Test case suite generated from Code automatically", generate_test(tc))
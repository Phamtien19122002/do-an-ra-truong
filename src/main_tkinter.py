import tkinter as tk
import importlib, time
from tkinter import messagebox, filedialog
from src.main_create import *
from src.main_merge import *

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
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(spec)
        return filename

def save_code(name, code):
    filename = f"code_{name}.py"
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(code)
        return filename

def save_tc(filename, tc):
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(tc)
        return filename

def display_test_case(file_path, tree):
    test_cases = []
    lines = read_file(file_path).splitlines()
    module_name = ""
    function_name = ""
    for line in lines:
        if "from" in line and "import" in line:
            parts = line.split("from")
            if len(parts) > 1 and "import" in parts[1]:
                module_name = parts[1].split("import")[0].strip()
                function_name = line.split("import")[1].strip()
                module = importlib.import_module(module_name)
                globals()[function_name] = getattr(module, function_name)
        if "assert" in line:
            try:
                if "(" in line and ")" in line and "==" in line:
                    data = line.split("(")[1].split(")")[0].strip()
                    expected = line.split("==")[1].split("#")[0].strip()
                    try:
                        result = eval(line.split("assert")[1].strip(), globals())
                    except AssertionError: 
                        result = "Fail"
                    test_cases.append({'data': data, 'expected': expected, 'result': result})
            except IndexError:
                continue
    for row in tree.get_children():
        tree.delete(row)    
    for tc in test_cases:
        tree.insert("", "end", values=(tc['data'], tc['expected'], tc['result']))

def display_pass_fail(path, label, tg):
    lines = slipcover(path).splitlines()
    output = ""
    for line in lines:
        if ("failed" in line or "passed" in line) and "in" in line:
            output += line.split("= ")[1].split(" in")[0].strip()
        if line.strip().startswith("code_") and ".py" in line:
            parts = line.split()
            if len(parts)>=3:
                try:
                    output += (" / " + parts[3] + "%")
                except (ValueError, IndexError):
                    print_red("Not find coverage.")
    output += " / " + tg
    label.config(text=output)

def button_spec(name, spec, code, tree, slip):
    if not name or not spec or not code:
        messagebox.showwarning("Warning", "Please input all above fields.")
        return
    try:
        start = time.time()
        save_spec(name, spec)
        tc_path = f"TC_spec/spec_{name}_tc.py"
        tc = generate_test(prompt_spec(name, spec, code))
        save_tc(tc_path, tc)
        count = 3
        missed_code = missed_lines(tc_path, f"code_{name}.py")
        while missed_code and count > 0:
            news = generate_test(prompt_miss(get_function_name_from_code(code), f"code_{name}", missed_code, code))
            append_test_cases(tc_path, news) 
            missed_code = missed_lines(tc_path, f"code_{name}.py")
            count -= 1
        if count!=3: 
            print("Added test case missed!")
            count = 3        
        while count > 0:
            failure = extract_wrong(tc_path)
            if failure:
                tc = generate_test(prompt_wrong(read_file(f"spec_{name}.txt"), failure, read_file(tc_path)))
                update_wrong(tc, tc_path)
            else:
                count = 0
            count -= 1
        tg = f"{(time.time()-start):.2f}s"
        display_test_case(tc_path, tree)
        display_pass_fail(tc_path, slip, tg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def button_code(name, code, tree, slip):
    if not name or not code:
        messagebox.showwarning("Warning", "Please input both above fields:\n - name, \n - code.")
        return
    try:
        start = time.time()
        save_code(name, code)
        tc_path = f"TC_function/code_{name}_tc.py"
        tc = generate_test(prompt_code(name, code))
        save_tc(tc_path, tc)
        count = 3
        missed_code = missed_lines(tc_path, f"code_{name}.py")
        while missed_code and count > 0:
            news = generate_test(prompt_miss(get_function_name_from_code(code), f"code_{name}", missed_code, code))
            append_test_cases(tc_path, news) 
            missed_code = missed_lines(tc_path, f"code_{name}.py")
            count -= 1
        if count!=3: 
            print("Added test case missed!")
            count = 3
        while count > 0 and os.path.exists(f"spec_{name}.txt"):
            failure = extract_wrong(tc_path)
            if failure:
                tc = generate_test(prompt_wrong(read_file(f"spec_{name}.txt"), failure, read_file(tc_path)))
                update_wrong(tc, tc_path)
            else:
                count = 0
            count -= 1
        tg = f"{(time.time()-start):.2f}s"
        display_test_case(tc_path, tree)
        display_pass_fail(tc_path, slip, tg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def button_merge(name, tree, slip):
    start = time.time()
    tc_path = f"TC_merge/merge_{name}_tc.py"
    merge(f"TC_spec/spec_{name}_tc.py", f"TC_function/code_{name}_tc.py", tc_path)
    tg = f"{(time.time()-start):.2f}s"
    display_test_case(tc_path, tree)
    display_pass_fail(tc_path, slip, tg)

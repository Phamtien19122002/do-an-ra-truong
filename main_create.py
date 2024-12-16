import re, os, subprocess
from openai import OpenAI
from main_merge import *

OPENAI_API_KEY = "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"
client = OpenAI(api_key = OPENAI_API_KEY)

def prompt_code(function_path, code):
    function_name = get_function_name_from_code(code)
    return ("You are a professional Python developer. "
        "Create pytest test functions for a specific functionality based on the code below.\n"
        "Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' "
        f"that imported from 'code_{function_path}'.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code"
        " calling into pytest.main or the test itself.\n"
        "- Ensure that each test function contains only 1 test case.\n"
        f"{code}")

def prompt_spec(name, spec, function_name):
    return (
        "You are a professional Python tester. Create pytest test functions for a specific "
        "functionality based on the specification. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' "
        f"that imported from 'code_{name}'.\n- Each test function have only 1 test case.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code"
        " calling into pytest.main or the test itself.\n"
        f"For spec below:\n {spec}"
    )

def prompt_miss(function_name, import_function, missed_lines, code):
    return (
        "You are a professional Python tester. Your task is to create pytest test functions "
        "specifically targeting the lines of code that have been missed in the coverage report.\n"
        f"Function name is '{function_name}' imported from '{import_function}' have missed lines: {missed_lines}\n"
        f"in the code below:\n{code}\n"
        "Each test function should:\n"
        "- Focus on a specific scenario that exercises the missed lines.\n"
        "- Use boundary analysis and equivalence partitioning techniques.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, WITHOUT explanation.\n"
        "- Ensure that each test function contains only 1 test case.\n"
    )

def prompt_wrong(spec, wrong, tc):
    return (
        f"Với spec như này: '{spec}' \n và mình có bộ test case dưới đây: \n{tc}" 
        f"và sau khi chạy test thì có một vài test failed như dưới đây: \n {wrong} \n" 
        "bạn có thể xem lại các case fail xem 'expected output' của của case đúng hay sai theo spec?, "
        "nếu các case fail mà 'expected output' theo spec đúng, hoặc case pass thì giữ nguyên, "
        "còn các case fail mà 'expected output' theo spec bị sai thì update 'expected output' "
        "cho mình vào bộ test đó nhé, rồi gủi lại cho mình bộ test, " 
        "nhớ chỉ thay đổi expected output của các test bị sai so với spec thôi nhé "
        "chứ đừng thay đổi bất cứ thứ gì khác, với lại không cần giải thích, chỗ nào update thì "
        "'#update' bên cạnh tên hàm test."
        )

def extract_wrong(path):
    output = slipcover(path)
    start_index = output.find("==== FAILURES ===")
    end_index = output.find("=== short test summary info ===")
    if start_index == -1 or end_index == -1:
        print_red("No failed tests found.")
        return None  
    failures_section = output[start_index:end_index].strip()
    return failures_section

#SlipCover
def slipcover(tc_path):
    try:
        output = subprocess.run(
            ["python3", "-m", "slipcover", "-m", "pytest", tc_path],
            check=True,
            text=True,
            capture_output=True
        )
        output = output.stdout
    except subprocess.CalledProcessError as e:
        output = e.stdout
    return output

def missed_lines(output, search_line):
    missed_lines = []
    for line in output.splitlines():
        if line.startswith(search_line):
            parts = line.split(maxsplit=4)
            if len(parts) == 5:
                missing_column = parts[-1]
                for part in missing_column.split(', '):
                    if '-' in part:
                        start, end = map(int, part.split('-'))
                        missed_lines.extend(range(start, end + 1))
                    else:
                        missed_lines.append(int(part.strip()))
    return missed_lines

def find_miss(test_path, seach_line):
    return missed_lines(slipcover(test_path), seach_line)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_code(content):
    code_block = re.search(r'```(?:python)?\s*\n(.*?)\n```', content, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()
    else:
        raise ValueError("No Python code block found in the response.")
        
def generate_test(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return extract_code(completion.choices[0].message.content)
    
def convert_function_paths(function_path):
    directory, file_name = os.path.split(function_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    function_name = directory.replace('/', '.') + file_name_without_extension
    return function_name

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def append_test_cases(file_path, new_test_cases):
    filtered_lines = [
        line for line in new_test_cases.splitlines()
        if not line.strip().startswith(("from", "import"))
    ]
    filtered = "\n".join(filtered_lines)
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(filtered)
            print(f"===> New test cases have been appended to {file_path}.")
    except Exception as e:
        print(f"An error occurred while appending test cases: {e}")

def update_wrong(tc, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(tc + "\n")
    print_red(f"Test cases have been updated in {path}.")
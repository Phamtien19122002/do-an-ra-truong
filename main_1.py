import os
from src.create import *
from src.merge import *
from src.estimate import *

def convert_function_path(function_path):
    directory, file_name = os.path.split(function_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    function_name = directory.replace('/', '.') + '.' + file_name_without_extension
    return function_name

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def generate_and_estimate(function_path, spec_path, merge_path):
    code = read_file(function_path)
    spec = read_file(spec_path)

    function_name = get_function_name_from_code(code)
    import_function = convert_function_path(function_path)

    prompt_code = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the code below.\n"
        "Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' that imported from {import_function}.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n"
        "- Ensure that each test function contains only one test case.\n"
        f"{code}"
    )
    prompt_spec = (
        "You are a professional Python tester. Create pytest test functions for a specific functionality based on the specification.\n"
        "Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' that imported from {import_function}.\n"
        "- Each test function have a test case.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n"
        f"For spec below:\n {spec}"
    )

    try:
        print_red("The function's test suite is generating.....")
        test_code = generate_test(prompt_code)
        extracted_code = extract_code(test_code.content)
        with open(f"TC_{function_path}", "w", encoding="utf-8") as file:
            file.write(extracted_code)
            print("===> Tests from function has successfully written to TC_function folder.")
        estimate(f"TC_{function_path}")

        print_red("The specification's test suite is generating.....")
        test_spec = generate_test(prompt_spec)
        extracted_spec = extract_code(test_spec.content)
        with open(f"TC_{spec_path}.py", "w", encoding="utf-8") as file:
            file.write(extracted_spec)
            print("===> Tests from spec has successfully written to TC_spec folder.")
        estimate(f"TC_{spec_path}.py")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    print_red("The merge test suite is processing.....")
    merge(f"TC_{spec_path}.py", f"TC_{function_path}", f"{merge_path}")
    estimate(f"{merge_path}")

if __name__ == "__main__":
    function_path = "function/function_0107.py"
    spec_path = "spec/spec_0107"
    merge_path = "TC_merge/merge_0107.py"

    generate_and_estimate(function_path, spec_path, merge_path)
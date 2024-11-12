from src.create import *
from src.merge import *
from src.measuring_cover import *

function_path = "function/function_0104.py"
spec_path = "spec/spec_0104"
merge_path = "TC_merge/merge_0104.py"

code = read_file(function_path)
spec = read_file(spec_path)

function_name = get_function_name_from_code(code)

prompt_code = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the code below.\n"
        "Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' that imported from function.function_0104.\n"
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
        f"- Include assert statements to verify the conditions with exist function name is '{function_name}' that imported from function.function_0104.\n"
        "- Each test function have a test case.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n"
        f"For spec below:\n {spec}"
    )

try:
    print("-------------------------------------------")
    test_code = generate_test(prompt_code)
    # print(prompt_code)
    # print(test_code.content)
    extracted_code = extract_code(test_code.content)
    with open(f"TC_{function_path}", "w", encoding="utf-8") as file:
        # file.write(f"{text}")
        file.write(extracted_code)
        print("===> Test script has successfully written to TC_function")
    run_tests(f"TC_{function_path}")
    time.sleep(10)
    print("-------------------------------------------")
    test_spec = generate_test(prompt_spec)
    # print(prompt_spec)
    # print(test_spec.content)
    extracted_spec = extract_code(test_spec.content)
    with open(f"TC_{spec_path}.py", "w", encoding="utf-8") as file:
        # file.write(f"{text}")
        file.write(extracted_spec)
        print("===> Test script has successfully written to TC_spec")
    run_tests(f"TC_{spec_path}.py")
    time.sleep(10)
except Exception as e:
    print(f"An error occurred: {e}")

print("-------------------------------------------")
merge(f"TC_{spec_path}.py", f"TC_{function_path}", f"{merge_path}")
run_tests(f"{merge_path}")
import re, subprocess
from openai import OpenAI
from src.main_merge import *

OPENAI_API_KEY = "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"
client = OpenAI(api_key = OPENAI_API_KEY)

def prompt_code(name, code):
    function_name = get_function_name_from_code(code)
    return (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the provided code. Each test function must adhere to the following criteria:"
        "- Focus on a specific scenario and have a descriptive name reflecting its objective."
        "- Employ boundary analysis and equivalence partitioning techniques to maximize test coverage."
        "- Respond only with the Python code enclosed in backticks, without any explanation or additional commentary."
        "- Avoid top-level code wherever possible, particularly code calling pytest.main or executing the test directly."
        "- Ensure each test function contains only one test case and is self-contained."
        f"- Include assert statements to verify the conditions, using the existing function '{function_name}', which is imported from 'code_{name}'."
        f"Here is the code for reference: \n{code}"
    )

def prompt_spec(name, spec, code):
    function_name = get_function_name_from_code(code)
    return (
        "You are a professional Python tester. Create pytest test functions for a specific functionality based on the specification. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        "- Each test function have only 1 test case.\n"
        "- Respond only with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code  calling into pytest.main or the test itself.\n"
        f"- Include assert statements to verify the conditions using the existing function '{function_name}', which is imported from 'code_{name}'.\n"
        f"For spec below:\n {spec}"
    )

def prompt_miss(function_name, import_function, missed_lines, code):
    return (
        "You are a professional Python tester. Your task is to create pytest test functions specifically targeting the lines of code that have been missed in the coverage report.\n"
        f"Function name is '{function_name}' imported from '{import_function}' have missed lines: {missed_lines}\n in the code below:\n{code}\n"
        "Each test function should:\n"
        "- Focus on a specific scenario that exercises the missed lines.\n"
        "- Use boundary analysis and equivalence partitioning techniques.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, WITHOUT explanation.\n"
        "- Ensure that each test function contains only 1 test case.\n"
    )

# def prompt_wrong(spec, wrong, tc):
#     return (
#         f"Given the following spec: '{spec}'\n and the test cases below: \n{tc} and after running the tests, there are some failed cases as shown below: \n{wrong} \n" 
#         "Can you review the failed cases to check if the 'expected output' of each case aligns with the spec? "
#         "If the 'expected output' of the failed cases is correct according to the specifications, or the case passed, leave it unchanged. "
#         "If the 'expected output' of the failed cases is incorrect according to the spec, update the 'expected output' for those cases in the test suite and send back the updated test suite to me. "
#         "Please only modify the 'expected output' for the failed cases that are incorrect according to the spec, and don't change anything else. Additionally, mark each updated test case with '#update' next to the test function name."
#     )

def prompt_wrong(spec, wrong, tc):
    return (
        f"Given the following specification: '{spec}' and the test cases below: \n{tc}\n"
        f"After running the tests, the following test cases failed: \n{wrong}\n"
        "Please review the failed test cases to determine if their 'expected output' aligns with the specification provided.\n"
        "Your task:\n"
        "1. If the 'expected output' of a failed test case is correct according to the specification, or if the test case passed, leave it unchanged.\n"
        "2. If the 'expected output' of a failed test case is incorrect according to the specification, update the 'expected output' for that specific case in the test suite.\n"
        "3. Keep the position and structure of all test cases exactly as they are in the provided test suite.\n"
        "When updating a failed test case:\n"
        "- Only modify the 'expected output' if it is incorrect according to the specification.\n"
        "- Add the comment '#update' next to the test function name to indicate the modification.\n"
        "Please return the full, updated test suite with only the necessary changes applied, while preserving the original structure and position of all test cases."
    )

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

def missed_lines(test_path, search_line):
    output = slipcover(test_path)
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
            print(f"===> Appended to {file_path}.")
    except Exception as e:
        print(f"An error occurred while appending test cases: {e}")

def extract_wrong(path):
    output = slipcover(path)
    start_index = output.find("==== FAILURES ===")
    end_index = output.find("=== short test summary info ===")
    if start_index == -1 or end_index == -1:
        print_red("No failed tests found.")
        return None  
    failures_section = output[start_index:end_index].strip()
    return failures_section

def update_wrong(tc, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(tc + "\n")
    print_red(f"===> Updated in {path}.")
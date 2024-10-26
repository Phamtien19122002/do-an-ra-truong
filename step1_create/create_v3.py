import re, time
from openai import OpenAI

client = OpenAI(api_key = "")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def generate_test(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message

def extract_code(content):
    code_block = re.search(r'```python\s*\n(.*?)\n```', content, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()
    else:
        raise ValueError("No Python code block found in the response.")

spec_path = 'spec/spec_0104'
code_path = 'function/function_0104.py'

spec = read_file(spec_path)
code = read_file(code_path)

prompt_spec = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the specification below. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n"
        f"{spec}"
    )

prompt_code = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the code below. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n"
        "- Ensure that each test function contains only one test case.\n"
        "- Include the function being tested within the test itself to avoid errors.\n"
        f"{code}"
    )

if __name__ == "__main__":
    try:
        print("-------------------------------------------")
        print(prompt_spec)
        test_spec = generate_test(prompt_spec)
        print(test_spec.content)
        extracted_spec = extract_code(test_spec.content)
        with open("TC_spec/test_0104.py", "w", encoding="utf-8") as file:
            file.write(extracted_spec)
            print("===> Test script has successfully written to TC_spec")

        time.sleep(15)

        print("-------------------------------------------")
        print(prompt_code)
        test_code = generate_test(prompt_code)
        print(test_code.content)
        extracted_code = extract_code(test_code.content)
        with open("TC_function/test_0104.py", "w", encoding="utf-8") as file:
            file.write(extracted_code)
            print("===> Test script has successfully written to TC_function")

    except Exception as e:
        print(f"An error occurred: {e}")

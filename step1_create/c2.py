import re
from openai import OpenAI
from code.code0101 import remaining_elements_count

OPENAI_API_KEY = "sk-VejmkyzPYfciV99g9Mkr2Ihq4LEnXNA3gmMJLE-Jc9T3BlbkFJFQtfBgdCs5BpJYzFiOI3hZbT_BDAebratkSa2MW6sA"
client = OpenAI(api_key=OPENAI_API_KEY)

spec = (
    "Cho dãy số A[] chỉ bao gồm các số nguyên dương. Người ta thu gọn dần dãy số bằng cách loại "
    "bỏ các cặp phần tử kề nhau mà có tổng là chẵn. Sau khi cặp phần tử đó bị loại ra thì dã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y "
    "số được dồn lại. Cứ tiếp tục như vậy cho đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa. "
    "Hãy tính xem cuối cùng dãy A[] còn bao nhiêu phần tử. \n"
    "Input N số của dãy A (1 ≤ A[i] ≤ 100, 1 ≤ N ≤ 10^5). \n"
    "Output Ghi ra trên một dòng số phần tử còn lại trong dãy A[]."
)

code = ()

def generate_test_from_spec(spec):
    prompt = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the specification below. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n\n"
        f"{spec}"
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message

def generate_test_from_code(code):
    prompt = (
        "You are a professional Python developer. Create pytest test functions for a specific functionality based on the specification below. Each test function should:\n"
        "- Focus on a specific scenario and have a name that reflects its objective.\n"
        "- Utilize boundary analysis and equivalence partitioning techniques to ensure high coverage.\n"
        "- Include assert statements to verify the conditions.\n"
        "- Respond ONLY with the Python code enclosed in backticks, without any explanation.\n"
        "- Write as little top-level code as possible, and in particular do not include any top-level code calling into pytest.main or the test itself.\n\n"
        f"{code}"
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message

def extract_code(content):
    """
    Extracts Python code enclosed within ```python and ``` from the content.
    """
    code_block = re.search(r'```python\s*\n(.*?)\n```', content, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()
    else:
        raise ValueError("No Python code block found in the response.")

if __name__ == "__main__":
    try:
        test_message = generate_test_from_spec(spec)
        extracted_code = extract_code(test_message.content)
        
        with open("promptOpenAI/test_spec/test_spec.py", "w", encoding="utf-8") as file:
            file.write(extracted_code)
        
        print("Test script successfully written to test_spec.py")
    except Exception as e:
        print(f"An error occurred: {e}")

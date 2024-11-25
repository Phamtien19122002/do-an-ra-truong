import re, time
from openai import OpenAI

OPENAI_API_KEY = "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"
client = OpenAI(api_key = OPENAI_API_KEY)

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
    code_block = re.search(r'```(?:python)?\s*\n(.*?)\n```', content, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()
    else:
        raise ValueError("No Python code block found in the response.")
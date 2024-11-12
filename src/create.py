import re, time
from openai import OpenAI
from merge.merge_v2 import merge_v2

OPENAI_API_KEY = "sk-y-T1H3b8mBrjD_k-jyA6f0EuA_r7daKye1SM5bSB5XT3BlbkFJkBt0I3GYSMYXoViQCV91L4eZzvlDmlfIIdd9OB1Z8A"
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
import ast
import os

def extract_test_functions(file_path):
    """
    Extracts all test functions from a pytest test file.
    Returns a dictionary with function names as keys and their AST nodes as values.
    """
    with open(file_path, 'r') as file:
        file_content = file.read()
        tree = ast.parse(file_content)

    test_functions = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
            test_functions[node.name] = node

    return test_functions

def extract_imports(file_path):
    """
    Extracts all import statements from a Python file.
    Returns a list of import statements as strings.
    """
    with open(file_path, 'r') as file:
        file_content = file.read()
        tree = ast.parse(file_content)

    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(file_content, node))
    
    return imports

def merge_imports(imports_a, imports_b):
    """
    Merges two lists of import statements, removing duplicates.
    """
    return list(dict.fromkeys(imports_a + imports_b))

def write_merged_tests(imports, test_functions, output_file):
    """
    Writes the merged imports and test functions to the output file.
    """
    with open(output_file, 'w') as file:
        # Write imports
        for imp in imports:
            file.write(f"{imp}\n")
        file.write("\n")

        # Write test functions
        for func in test_functions.values():
            func_code = ast.unparse(func)
            file.write(f"{func_code}\n\n")

def main():
    # Define file paths
    test_spec_file = 'test_spec.py'
    test_code_file = 'test_code.py'
    output_file = 'test_merged.py'

    # Check if input files exist
    if not os.path.exists(test_spec_file):
        print(f"File {test_spec_file} does not exist.")
        return
    if not os.path.exists(test_code_file):
        print(f"File {test_code_file} does not exist.")
        return

    # Extract test functions
    tests_spec = extract_test_functions(test_spec_file)
    tests_code = extract_test_functions(test_code_file)

    # Identify duplicates by function name
    merged_tests = tests_spec.copy()
    duplicates = []
    for name, func in tests_code.items():
        if name in merged_tests:
            duplicates.append(name)
        else:
            merged_tests[name] = func

    if duplicates:
        print(f"Found duplicate test functions: {duplicates}")
    else:
        print("No duplicate test functions found.")

    # Extract imports
    imports_spec = extract_imports(test_spec_file)
    imports_code = extract_imports(test_code_file)
    merged_imports = merge_imports(imports_spec, imports_code)

    # Write merged tests to output file
    write_merged_tests(merged_imports, merged_tests, output_file)
    print(f"Merged test suite saved to {output_file}")

if __name__ == "__main__":
    main()

import ast
import os
import hashlib

def extract_test_functions(file_path):
    """
    Extracts test functions from the provided file.
    Returns a list of dictionaries containing function names, assertion statements, and the full function code.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        tree = ast.parse(file_content)

    test_functions = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test'):
            # Extract assertion statements
            assertions = []
            for stmt in ast.walk(node):
                if isinstance(stmt, ast.Assert):
                    # Convert assertion to a canonical string representation
                    assertion_code = ast.unparse(stmt.test)
                    assertions.append(assertion_code.strip())
            # Generate a hash of the combined assertions
            assertions_sorted = sorted(assertions)
            assertions_str = '\n'.join(assertions_sorted)
            assertions_hash = hashlib.md5(assertions_str.encode('utf-8')).hexdigest()

            test_functions.append({
                'name': node.name,
                'assertions': assertions_sorted,
                'hash': assertions_hash,
                'code': ast.get_source_segment(file_content, node)
            })
    return test_functions

def merge_test_functions(tests1, tests2):
    """
    Merges two lists of test functions, removing duplicates based on the hash of their assertion statements.
    Returns a list of merged test functions.
    """
    merged_tests = tests1.copy()
    existing_hashes = {test['hash'] for test in merged_tests}
    duplicates = []
    for test2 in tests2:
        if test2['hash'] in existing_hashes:
            duplicates.append(test2['name'])
        else:
            merged_tests.append(test2)
            existing_hashes.add(test2['hash'])
    if duplicates:
        print(f"Found duplicate test functions based on purpose: {duplicates}")
    else:
        print("No duplicate test functions found based on purpose.")
    return merged_tests

def extract_imports(file_path):
    """
    Extracts all import statements from a Python file.
    Returns a list of import statements as strings.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
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
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write imports
        for imp in imports:
            file.write(f"{imp}\n")
        file.write("\n")

        # Write test functions
        for test in test_functions:
            file.write(f"{test['code']}\n\n")

def main():
    # Define file paths
    test_file1 = 'I_code_test.py'
    test_file2 = 'I_spec_test.py'
    output_file = 'merged_tests.py'

    # Check if input files exist
    if not os.path.exists(test_file1):
        print(f"File {test_file1} does not exist.")
        return
    if not os.path.exists(test_file2):
        print(f"File {test_file2} does not exist.")
        return

    # Extract test functions
    tests1 = extract_test_functions(test_file1)
    tests2 = extract_test_functions(test_file2)

    # Merge test functions based on assertion hashes
    merged_tests = merge_test_functions(tests1, tests2)

    # Extract and merge imports
    imports1 = extract_imports(test_file1)
    imports2 = extract_imports(test_file2)
    merged_imports = merge_imports(imports1, imports2)

    # Write merged tests to output file
    write_merged_tests(merged_imports, merged_tests, output_file)
    print(f"Merged test suite saved to {output_file}")

if __name__ == "__main__":
    main()

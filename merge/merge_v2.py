import ast, os, hashlib

# Normalizes an assertion node by replacing numeric and string literals with placeholders. Returns the normalized assertion code as a string.
def normalize_assertion(node):
    class LiteralReplacer(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)):
                return ast.copy_location(ast.Name(id='NUM', ctx=ast.Load()), node)
            elif isinstance(node.value, str):
                return ast.copy_location(ast.Name(id='STR', ctx=ast.Load()), node)
            else:
                return node
        def visit_Num(self, node):  # For Python versions < 3.8
            return ast.copy_location(ast.Name(id='NUM', ctx=ast.Load()), node)
        def visit_Str(self, node):  # For Python versions < 3.8
            return ast.copy_location(ast.Name(id='STR', ctx=ast.Load()), node)
    replacer = LiteralReplacer()
    normalized_node = replacer.visit(node)
    ast.fix_missing_locations(normalized_node)
    return ast.unparse(normalized_node)

# Extracts test functions from the provided file. Returns a list of dictionaries containing function names, normalized assertions, and the full function code.
def extract_test_functions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        tree = ast.parse(file_content)
    test_functions = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test'):
            # Extract assertion statements
            normalized_assertions = []
            for stmt in ast.walk(node):
                if isinstance(stmt, ast.Assert):
                    # Normalize the assertion by replacing literals
                    normalized_assertion = normalize_assertion(stmt.test)
                    normalized_assertions.append(normalized_assertion.strip())
            # Generate a hash of the combined normalized assertions
            assertions_sorted = sorted(normalized_assertions)
            assertions_str = '\n'.join(assertions_sorted)
            assertions_hash = hashlib.md5(assertions_str.encode('utf-8')).hexdigest()
            test_functions.append({
                'name': node.name,
                'assertions': assertions_sorted,
                'hash': assertions_hash,
                'code': ast.get_source_segment(file_content, node)
            })
    return test_functions

# Merges two lists of test functions, removing duplicates based on the hash of their normalized assertion statements. Returns a list of merged test functions.
def merge_test_functions(tests1, tests2):
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
        print(f"Found duplicate test functions based on purpose: \n{duplicates}")
    else:
        print("No duplicate test functions found based on purpose.")
    return merged_tests

# Extracts all import statements from a Python file. Returns a list of import statements as strings.
def extract_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        tree = ast.parse(file_content)
    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(file_content, node))
    return imports

# Merges two lists of import statements, removing duplicates.
def merge_imports(imports_a, imports_b):
    return list(dict.fromkeys(imports_a + imports_b))

# Writes the merged imports and test functions to the output file.
def write_merged_tests(imports, test_functions, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write imports
        for imp in imports:
            file.write(f"{imp}\n")
        file.write("\n")
        # Write test functions
        for test in test_functions:
            file.write(f"{test['code']}\n\n")

def merge_v2(test_file1, test_file2, output_file):
    # Define file paths
    # test_file1 = 'TC_code/test_0101_code.py'
    # test_file2 = 'TC_spec/test_0101_spec.py'
    # output_file = 'TC_merge/test_0101_merge.py'
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
    # Merge test functions based on normalized assertion hashes
    merged_tests = merge_test_functions(tests1, tests2)
    # Extract and merge imports
    imports1 = extract_imports(test_file1)
    imports2 = extract_imports(test_file2)
    merged_imports = merge_imports(imports1, imports2)
    # Write merged tests to output file
    write_merged_tests(merged_imports, merged_tests, output_file)
    print(f"Merged test suite saved to {output_file}")

import ast, os, hashlib

def normalize_assertion(node):
    class LiteralReplacer(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)):
                return ast.copy_location(ast.Name(id='NUM', ctx=ast.Load()), node)
            elif isinstance(node.value, str):
                return ast.copy_location(ast.Name(id='STR', ctx=ast.Load()), node)
            else:
                return node
        def visit_Num(self, node):  
            return ast.copy_location(ast.Name(id='NUM', ctx=ast.Load()), node)
        def visit_Str(self, node):  
            return ast.copy_location(ast.Name(id='STR', ctx=ast.Load()), node)
    replacer = LiteralReplacer()
    normalized_node = replacer.visit(node)
    ast.fix_missing_locations(normalized_node)
    return ast.unparse(normalized_node)

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

def extract_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        tree = ast.parse(file_content)
    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.get_source_segment(file_content, node))
    return imports

def merge_imports(imports_a, imports_b):
    return list(dict.fromkeys(imports_a + imports_b))

def write_merged_tests(imports, test_functions, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for imp in imports:
            file.write(f"{imp}\n")    
        for test in test_functions:
            file.write(f"{test['code']}\n\n")

def get_function_name_from_code(code):
    tree = ast.parse(code)
    function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return function_names[0] if function_names else None

def merge(test_file1, test_file2, output_file):
    if not os.path.exists(test_file1):
        print(f"File {test_file1} does not exist.")
        return
    if not os.path.exists(test_file2):
        print(f"File {test_file2} does not exist.")
        return
    tests1 = extract_test_functions(test_file1)
    tests2 = extract_test_functions(test_file2)
    merged_tests = merge_test_functions(tests1, tests2)
    imports1 = extract_imports(test_file1)
    imports2 = extract_imports(test_file2)
    merged_imports = merge_imports(imports1, imports2)
    write_merged_tests(merged_imports, merged_tests, output_file)
    print(f"Merged test suite saved to {output_file}")
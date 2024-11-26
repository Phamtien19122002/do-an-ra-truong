from main_create import *
from main_merge import *

def generate_and_estimate(function_path, spec_path, merge_path):
    code = read_file(function_path)
    spec = read_file(spec_path)
    function_name = get_function_name_from_code(code)
    import_function = convert_function_path(function_path)
    try:
        print_red("The function's test suite is generating.....")
        test_code = generate_test(prompt_code(function_name, import_function, code))
        with open(f"TC_{function_path}", "w", encoding="utf-8") as file:
            file.write(test_code)
            print("===> Tests from function has successfully written to TC_function folder.")
        missed_code = estimate(f"TC_{function_path}", function_path)
        if missed_code:
            test_code = generate_test(prompt_miss(function_name, import_function, missed_code, code))
            print(test_code)
            append_test_cases(f"TC_{function_path}", test_code)
            print(estimate(f"TC_{function_path}", function_path))

        print_red("The specification's test suite is generating.....")
        test_spec = generate_test(prompt_spec(function_name, import_function, spec))
        with open(f"TC_{spec_path}.py", "w", encoding="utf-8") as file:
            file.write(test_spec)
            print("===> Tests from spec has successfully written to TC_spec folder.")
        missed_spec = estimate(f"TC_{spec_path}.py", function_path)
        n=1
        while missed_spec and n<5:
            test_spec = generate_test(prompt_miss(function_name, import_function, missed_spec, code))
            print(test_code)
            append_test_cases(f"TC_{function_path}", test_spec)
            print(estimate(f"TC_{function_path}", function_path))
            n += 1
        
    except Exception as e:
        print(f"An error occurred: {e}")

    print_red("The merge test suite is processing.....")
    merge(f"TC_{spec_path}.py", f"TC_{function_path}", f"{merge_path}")
    estimate(f"{merge_path}", function_path)

if __name__ == "__main__":
    # function_path = "function/calculate_income_tax.py"
    # spec_path = "spec/calculate_income_tax"
    # merge_path = "TC_merge/calculate_income_tax.py"
    # code = read_file(function_path)
    # spec = read_file(spec_path)
    # function_name = get_function_name_from_code(code)
    # import_function = convert_function_path(function_path)
    # missed_lines = estimate(f"TC_{function_path}", function_path)
    # print(prompt_miss(function_name, import_function, missed_lines, code))
    # if missed_lines:
    #     add = generate_test(prompt_miss(function_name, import_function, missed_lines, code))
    #     print(add)
    #     append_test_cases(f"TC_{function_path}", add)
    #     print(estimate(f"TC_{function_path}", function_path))

    function_path = "function/function_0101.py"
    spec_path = "spec/spec_0101"
    merge_path = "TC_merge/merge_0101.py"
    generate_and_estimate(function_path, spec_path, merge_path)
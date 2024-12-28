from src.main_create import *
from src.main_tkinter import *

if __name__ == "__main__":
    file1 = "TC_function/code_0101_tc.py"
    file2 = "TC_spec/spec_0101_tc.py"
    output_file = "TC_merge/merge_0101_test.py"

    merge_tc(file1, file2, output_file)
    print(slipcover(output_file))
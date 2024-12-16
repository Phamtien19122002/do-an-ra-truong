from main_create import *

name = "0101"
failure = extract_wrong(f"TC_merge/merge_{name}_tc.py")
if failure != -1:
    tc = generate_test(prompt_wrong(read_file(f"spec_{name}.txt"), failure, read_file(f"TC_merge/merge_{name}_tc.py")))
    print(tc)
    update_wrong(tc, f"TC_merge/merge_{name}_tc.py")
else:
    print_red("No tests failed.")
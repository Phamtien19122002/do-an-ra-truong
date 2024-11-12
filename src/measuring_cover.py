import subprocess

def run_tests(test_file):
    try:
        result = subprocess.run(
            ["python3", "-m", "slipcover", "-m", "pytest", test_file],
            check=True,
            text=True,
            capture_output=True
        )
        print("Test run successful:")
        print(result.stdout)  # In ra kết quả stdout
    except subprocess.CalledProcessError as e:
        print("An error occurred while running tests:")
        print("Return code:", e.returncode)  # Mã trả về
        print("Standard Output:", e.stdout)  # Kết quả stdout
        # print("Standard Error:", e.stderr)  # Kết quả stderr
import subprocess
import os
import re

def run_tests_and_get_coverage(threshold=95):
    # Xóa dữ liệu độ bao phủ cũ nếu có
    if os.path.exists('.slipcover-coverage'):
        os.remove('.slipcover-coverage')

    # Chạy pytest với Slipcover để đo độ bao phủ
    print("Chạy pytest với Slipcover để đo độ bao phủ...")
    exit_code = subprocess.call(['python3', '-m', 'slipcover', '-m', 'pytest', 'test_module.py'])

    # Kiểm tra exit code của pytest
    if exit_code != 0:
        print("Có lỗi xảy ra khi chạy các bài kiểm thử.")
        return False

    print("Tạo báo cáo độ bao phủ bằng Slipcover...")
    result = subprocess.run(['slipcover', 'report', '-m'], capture_output=True, text=True)

    print(result.stdout)

    total_coverage = parse_total_coverage(result.stdout)

    if total_coverage is None:
        print("Không thể phân tích độ bao phủ tổng.")
        return False

    if total_coverage >= threshold:
        print(f"Độ bao phủ đã đạt {total_coverage:.2f}%, vượt ngưỡng {threshold}%")
        return True
    else:
        print(f"Độ bao phủ hiện tại là {total_coverage:.2f}%, chưa đạt ngưỡng {threshold}%")
        # Slipcover đã hiển thị các dòng chưa được bao phủ trong báo cáo
        return False

def parse_total_coverage(report_output):
    # Phân tích đầu ra của Slipcover để lấy phần trăm độ bao phủ tổng.
    lines = report_output.strip().split('\n')
    total_line = None
    for line in lines:
        if line.startswith('(summary)'):
            total_line = line
            break
    if total_line is None:
        return None

    # Sử dụng regex để lấy phần trăm độ bao phủ
    match = re.search(r'(\d+(?:\.\d+)?)%', total_line)
    if match:
        coverage_percent = float(match.group(1))
        return coverage_percent
    else:
        return None

if __name__ == '__main__':
    threshold = 95  # Ngưỡng độ bao phủ mong muốn
    max_iterations = 5  # Số lần lặp tối đa
    iteration = 0

    while iteration < max_iterations:
        print(f"\nLần chạy thứ {iteration + 1}:")
        success = run_tests_and_get_coverage(threshold=threshold)
        if success:
            break
        else:
            # Ở đây bạn có thể thêm phần gọi OpenAI API để sinh thêm test
            # Hiện tại, chúng ta sẽ giả lập bằng cách yêu cầu người dùng thêm test thủ công
            print("Vui lòng thêm các bài kiểm thử cho các dòng mã chưa được bao phủ.")
            # Chờ người dùng nhấn Enter sau khi đã thêm test
            input("Nhấn Enter sau khi đã thêm bài kiểm thử...")
            iteration += 1
    else:
        print("Không đạt được độ bao phủ mong muốn sau số lần lặp tối đa.")

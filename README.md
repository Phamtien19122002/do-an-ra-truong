Sinh unit test scripts tự động sử dụng LLM 

NỘI DUNG CHÍNH
- Tìm hiểu bài toán sinh unit test scripts tự động
- Tìm hiểu LLM và ứng dụng trong sinh unit test scripts 
- Xây dựng giải pháp sinh unit test scripts tự động sử dụng LLM 
- Thử nghiệm và đánh giá

Một số công nghệ được sử dụng:
- LLM API: OpenAI API có khả năng xử lý và hiểu các tài liệu có ngôn ngữ tự nhiên phức tạp, dùng để đọc hiểu tài liệu yêu cầu;
- Coverage tool: Cover-up giúp tăng cường việc bao phủ mã nguồn khi tạo test case, hướng dẫn tinh chỉnh test case, và hỗ trợ python;
- Framework unit test: PyTest dễ sử dụng và là một framework mạnh mẽ phổ biến, được sử dụng rộng rãi, tích hợp tốt với Cover-up.

2024/11/27
1. Selected test 						                => prompt để cải thiện test sai (nếu có)
2. Giao diện 
- Tùy chỉnh cho hợp lý (trái -> phải, trên - dưới)		=> Done
- Insert từ file 						                => Done
- Tree code: trường bắt buộc					        => Không cần thiết -> thông báo
- Input/generated input/generated ouput/ giống||khác 	=> Done
- Additional (thống kê tổng pass/fail - slipcover)		=> Done 
3. Viết documentation						            => 
4. Chạy độ phủ thử nghiệm					            => 

12/10/2024
1. Write function to update wrong TCs generated from step 2 with spec, and error message that I received after run slipcover technical.
2. After TCs merged from spec's TC and code's TC, then run the slipcover to measure the coverage of the TCs and display the statistics.
3. Redecorate the interface. 
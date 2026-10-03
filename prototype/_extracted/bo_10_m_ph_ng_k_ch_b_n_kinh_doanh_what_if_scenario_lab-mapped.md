# Phòng Thí Nghiệm Kịch Bản Kinh Doanh What-If (Scenario Lab) — đã đối chiếu ERD/FR

## Field GIỮ
- `simulations.name` → Tên kịch bản mô phỏng (Kịch bản A: Đẩy mạnh Livestream 11.11)
- `simulations.type` → Loại kịch bản (Kinh doanh / Dòng tiền / Stress-Test)
- `simulations.description` → Mô tả kịch bản
- `simulations.scenarioInput` → Tham số đầu vào (Doanh số target +35%, Ads 140M, Discount 15%, Lead-time T+45)
- `simulation_results.metricName` → Tên chỉ số kết quả (Doanh thu, Lợi nhuận ròng, Điểm hòa vốn, Đáy tiền mặt)
- `simulation_results.projectedValue` → Giá trị mô phỏng dự kiến (2.490.000.000 ₫)
- `simulation_results.baselineValue` → Giá trị cơ sở trước mô phỏng (1.845.200.000 ₫)
- `simulation_results.difference` → Chênh lệch tuyệt đối (+644.800.000 ₫)
- `simulation_results.differencePercent` → Tỷ lệ chênh lệch (+34.9%)

## Field LOẠI
- Đặt cược hợp đồng tương lai thị trường tài chính ngoài doanh nghiệp (ngoài scope FR)

## Field THIẾU - CẦN BỔ SUNG
- `simulations.baselineSnapshot`: Lưu lại snapshot số liệu thực tế tại thời điểm mô phỏng
- `simulation_results.differencePercent`: Phần trăm thay đổi tương quan để đánh giá ROI

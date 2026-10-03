# BO-02: Quản lý Chi phí & Tài chính Cơ bản
Nguồn: stitch_ai_business_copilot_platform/bo_02_qu_n_l_chi_ph_t_i_ch_nh_c_b_n/code.html

## Field đang hiển thị
- Tiêu đề màn hình: Quản lý Nhóm Chi Phí & Tài Chính Cơ Bản
- Mô tả: Thiết lập danh mục nhóm chi phí định phí/biến phí, ghi nhận khoản chi chi tiết, phân tích tỷ trọng cơ cấu chi phí và tự động tính toán P&L lợi nhuận ước tính.
- Thẻ KPI 1 - Tổng Doanh Thu Ghi Nhận: 1.845.200.000 ₫ (+18.4% so tháng trước, 4.280 đơn hàng)
- Thẻ KPI 2 - Giá Vốn Hàng Bán (COGS): 968.730.000 ₫ (Chiếm 52.5% doanh thu)
- Thẻ KPI 3 - Tổng Chi Phí Vận Hành (OPEX): 412.500.000 ₫ (+4.2% vs Định mức, 7 nhóm chi phí)
- Thẻ KPI 4 - Lợi Nhuận Ước Tính (EBT): 463.970.000 ₫ (Biên ròng: 25.15%, LN Gộp: 876.470.000 ₫)
- Danh mục nhóm chi phí & Ngân sách:
  - 01. Nguyên vật liệu & Bao bì đóng gói: Định mức 85.000.000 ₫, Đã chi 78.450.000 ₫ (92.3%)
  - 02. Tiền thuê mặt bằng & Showroom: Định mức 120.000.000 ₫, Đã chi 120.000.000 ₫ (100%)
  - 03. Điện nước, Internet & Tiện ích: Định mức 18.000.000 ₫, Đã chi 16.850.000 ₫ (93.6%)
  - 04. Lương & Phúc lợi nhân sự: Định mức 110.000.000 ₫, Đã chi 108.500.000 ₫ (98.6%)
  - 05. Marketing, Quảng cáo & Ads: Định mức 60.000.000 ₫, Đã chi 62.400.000 ₫ (104.0% - Cảnh báo vượt)
  - 06. Vận chuyển & Giao hàng (Logistics): Định mức 25.000.000 ₫, Đã chi 21.300.000 ₫ (85.2%)
  - 07. Chi phí khác & Dự phòng: Định mức 10.000.000 ₫, Đã chi 5.000.000 ₫ (50.0%)

## Action/Button
- `Ghi Nhận Khoản Chi Mới (+)`: Mở form/drawer ghi nhận khoản chi mới
- `Tạo Nhóm Chi Phí (+)`: Mở form tạo nhóm/hạng mục chi phí mới
- `Xuất Báo Cáo`: Xuất dữ liệu báo cáo chi phí và P&L
- `Cấu hình định mức`: Chỉnh sửa hạn mức ngân sách theo tháng
- `Chụp hóa đơn / Camera OCR` (từ bản Mobile delta): Nút scan nhanh chứng từ chi bằng camera
- `Sửa nhóm` / `Xóa nhóm`: Quản lý các nhóm chi phí

## Ghi chú UX
- Màn hình bao gồm 4 thẻ KPI tài chính quan trọng (Doanh thu, Giá vốn, OPEX, Lợi nhuận ròng).
- Bảng danh mục nhóm chi phí hiển thị tiến độ giải ngân ngân sách thực tế so với định mức (ProgressBar & Badge cảnh báo vượt).

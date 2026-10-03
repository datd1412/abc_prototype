# BO-03: Quản lý Sản phẩm & Bảng giá
Nguồn: stitch_ai_business_copilot_platform/bo_03_qu_n_l_s_n_ph_m_b_ng_gi/code.html

## Field đang hiển thị
- Tiêu đề màn hình: Quản lý Sản phẩm & Bảng Giá
- Mô tả màn hình: Phân loại danh mục, cấu hình giá bán, giá vốn (COGS), định mức tồn kho an toàn và tự động cập nhật biên độ lợi nhuận gộp theo từng SKU thời gian thực.
- Thẻ KPI 1 - Tổng SKU đang kinh doanh: 142 SKU (98 sản phẩm gốc, 44 biến thể)
- Thẻ KPI 2 - Biên Lợi Nhuận Gộp TB: 47.45% (Ngưỡng tối thiểu đề ra: 45.0%)
- Thẻ KPI 3 - Tổng Doanh Thu Tiềm Năng: 2.450.000.000 ₫ (Giá vốn: ~1.287 tỷ ₫)
- Thẻ KPI 4 - Chạm Ngưỡng Tồn Tối Thiểu: 6 SKU báo động (4 mã có nguy cơ đứt hàng)
- Chi nhánh cửa hàng: Chi nhánh Q.1, TP.HCM / Maison de Bloom
- Danh mục sản phẩm (Ma trận biên lợi nhuận):
  - Tên danh mục: Skincare & Serum Cao Cấp (48 SKU, Doanh thu TB: 820.000.000 ₫, COGS: 360.000.000 ₫, Lợi nhuận gộp: +460.000.000 ₫, Margin: 56.1%)
  - Tên danh mục: Kem Dưỡng & Phục Hồi (35 SKU, Doanh thu TB: 480.000.000 ₫, COGS: 245.000.000 ₫, Lợi nhuận gộp: +235.000.000 ₫, Margin: 49.0%)
  - Tên danh mục: Son & Trang Điểm Hữu Cơ (32 SKU, Doanh thu TB: 350.000.000 ₫, COGS: 195.000.000 ₫, Lợi nhuận gộp: +155.000.000 ₫, Margin: 44.3%)
  - Tên danh mục: Phụ Kiện & CS Cá Nhân (27 SKU, Doanh thu TB: 195.200.000 ₫, COGS: 168.730.000 ₫, Lợi nhuận gộp: +26.470.000 ₫, Margin: 13.6%)
- Mô phỏng biên giá nhanh (What-If Simulator):
  - Sản phẩm thử nghiệm: Tinh Chất Phục Hồi Bio-B5 Hydra 50ml
  - Giá vốn mới (COGS): 280.000 ₫
  - Giá bán đề xuất: 682.000 ₫
  - Lợi nhuận gộp đơn vị: +402.000 ₫/sp
  - Tỷ suất LN gộp mới: 58.94%
- Bảng danh mục sản phẩm chi tiết:
  - Mã SKU: SKU-SKN-001, SKU-CRM-012, SKU-LIP-004, SKU-SKN-009, SKU-ACC-021, SKU-OLD-003
  - Dung tích / Quy cách: 50ml, 60g, Màu #04 Đỏ Ruby, 30ml, 120 miếng, Bao bì 2023
  - Tên sản phẩm: Serum Phục Hồi Bio-B5 Hydra Max, Kem Dưỡng Tái Sinh Rosa Damascena, Son Lụa Dưỡng Ẩm Velvet Bloom, Tinh Chất Kháng Viêm Tea Tree SOS, Bông Tẩy Trang Pure Cotton Bloom, Xịt Khoáng Cúc La Mã Calming Mist
  - Barcode: 8936014298110, 8936014298240, 8936014298356, 8936014298670, 8936014298889, 8936014297123
  - Danh mục: Skincare Cao Cấp, Kem Dưỡng & Phục Hồi, Son & Trang Điểm, Phụ Kiện Cá Nhân
  - Giá vốn (COGS): 280.000 ₫ (FIFO Lot #24A), 340.000 ₫ (FIFO Lot #24B), 160.000 ₫ (FIFO Lot #24C), 185.000 ₫ (FIFO Lot #24A), 38.000 ₫ (FIFO Lot #24D), 110.000 ₫ (Tồn cuối kỳ)
  - Giá niêm yết (Giá bán lẻ): 650.000 ₫, 720.000 ₫, 290.000 ₫, 420.000 ₫, 45.000 ₫, 180.000 ₫
  - Giá sỉ (≥10): 520.000 ₫, 580.000 ₫, 235.000 ₫, 340.000 ₫, Không sỉ, Xả hàng
  - Lãi gộp / Đơn vị: +370.000 ₫/sp, +380.000 ₫/sp, +130.000 ₫/sp, +235.000 ₫/sp, +7.000 ₫/sp, +70.000 ₫/sp
  - Tỷ suất (%): 56.9%, 52.8%, 44.8%, 55.9%, 15.5%, 38.8%
  - Tồn / Tối thiểu: 85 / 30, 8 / 25 (Thiếu 17 hộp), 42 / 20, 58 / 20, 140 / 50, 0 / 0
  - Trạng thái: Đang bán, Tạm ẩn

## Action/Button
- `Xuất Excel Bảng Giá`: Xuất danh sách sản phẩm và bảng giá ra file Excel
- `Cấu hình Hàng Loạt`: Mở công cụ cấu hình giá/tồn kho hàng loạt cho nhiều sản phẩm
- `+ Thêm Sản Phẩm Mới`: Mở form/modal tạo mới sản phẩm và biến thể
- `Áp Dụng Giá Này Ngay`: Cập nhật ngay lập tức giá vốn/giá bán từ bộ mô phỏng vào sản phẩm
- `Xem chi tiết` (trên KPI 4): Mở danh sách lọc các SKU bị đứt hàng/thiếu hàng
- `Chỉnh sửa` (nút edit trên dòng): Mở form chỉnh sửa sản phẩm & giá
- `Ẩn/Hiện trên POS` (nút visibility trên dòng): Đổi trạng thái kinh doanh/hiển thị của sản phẩm trên POS
- `Lịch sử thay đổi giá` (nút history/more_vert trên dòng): Xem nhật ký biến động giá vốn và giá bán
- `Mở khóa kinh doanh` / `Xóa vĩnh viễn`: Quản lý trạng thái sản phẩm tạm ẩn/ngừng bán

## Ghi chú UX
- Tab lọc danh mục sản phẩm: Tất cả (142), Skincare (48), Kem dưỡng (35), Son môi (32), Phụ kiện (27)
- Dropdown lọc trạng thái: Tất cả, Đang kinh doanh, Báo động thiếu hàng, Tạm ẩn / Ngừng bán
- Dropdown lọc tỷ suất lợi nhuận: Tất cả, Biên cao (>50%), Tiêu chuẩn (40-50%), Biên thấp (<40%)
- Ô tìm kiếm nhanh: Tìm theo tên sản phẩm, mã barcode, SKU hoặc phân nhóm
- Phân trang (Pagination): Chuyển trang (Trước/Sau, 1, 2, 3... 15), chọn số lượng xem mỗi trang (10, 25, 50, Tất cả)
- AI Copilot Recommendation widget: Gợi ý tối ưu giá bán Bio-B5 dựa trên độ co giãn cầu

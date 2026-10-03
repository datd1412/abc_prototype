# Dự Báo Nhu Cầu & Kế Hoạch Nhập Hàng Tự Động (AI Demand Forecasting)
Nguồn: stitch_ai_business_copilot_platform/bo_09_ai_demand_forecasting_replenishment_planning/code.html

## Field đang hiển thị
- Tổng Nhu Cầu Dự Báo (30N): 14.280 SKU (+22.4%, 4.850.000.000 ₫)
- Nguy Cơ Đứt Hàng (Stock-Out): 06 SKU Báo Động (~68.400.000 ₫ thất thoát)
- Vốn Đề Xuất Nhập (Reorder): 412.000.000 ₫ (5 đơn PO)
- Độ Tin Cậy Mô Hình (WAPE): 93.8%
- Chi tiết sản phẩm dự báo & đề xuất nhập:
  - Tên sản phẩm: Serum Bio-B5 Hydra Max, Kem Dưỡng Đêm Ceramide, Toner BHA 2%, Lotion Rau Má...
  - SKU sản phẩm
  - Tồn kho khả dụng & Runway (số ngày còn lại)
  - Tốc độ bán (chai/ngày)
  - Dự báo nhu cầu 30 ngày (SKU)
  - Điểm đặt hàng ROP & Tồn an toàn SS
  - Lead-time nhà cung cấp (ngày)
  - Số lượng đề xuất nhập PO (EOQ)
  - Vốn dự kiến nhập (₫)
  - Phân bổ kho đề xuất (Kho Tân Bình / Showroom Q.1)
  - Mức độ ưu tiên (Nguy cấp / Cao / Trung bình)

## Action/Button
- Cấu hình Lead-time: Chỉnh sửa thời gian giao hàng nhà cung cấp
- Xuất Kế Hoạch PO: Xuất file CSV/Excel danh sách PO
- + Tạo Lô PO Tự Động: Tự động khởi tạo các đơn mua hàng draft
- Xem kịch bản hoãn PO: Phân tích mô phỏng kịch bản hoãn nhập
- Duyệt Nhập [X] Chai: Duyệt tạo PO trực tiếp cho từng SKU

## Ghi chú UX
- Chart Burn-down: Biểu đồ đường tiêu thụ thực tế vs Dự báo AI vs Dải tin cậy 95% vs Mức cạn kho
- Ma trận EOQ Replenishment Table
- Filter theo thời gian (14 ngày, 30 ngày, 60 ngày, Quý)
- Filter theo kho & danh mục

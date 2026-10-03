# Dự Báo Nhu Cầu & Kế Hoạch Nhập Hàng Tự Động (AI Demand Forecasting) — đã đối chiếu ERD/FR

## Field GIỮ
- `forecast_runs.forecastType` → Loại dự báo (Nhu cầu tiêu thụ / Replenishment)
- `forecast_runs.horizonDays` → Chu kỳ dự báo (14 ngày / 30 ngày / 60 ngày)
- `forecast_runs.modelName` → Mô hình AI (Prophet + LightGBM)
- `forecast_results.predictedValue` → Nhu cầu dự báo (14.280 SKU)
- `forecast_results.lowerBound` → Ngưỡng dưới dải tin cậy 95%
- `forecast_results.upperBound` → Ngưỡng trên dải tin cậy 95%
- `forecast_results.confidence` → Độ tin cậy mô hình WAPE (93.8%)
- `product_variants.sku` → Mã SKU sản phẩm
- `product_variants.name` → Tên biến thể sản phẩm
- `inventory.quantity` → Tồn kho khả dụng
- `inventory.lowStockThreshold` → Điểm đặt hàng ROP / Safety Stock
- `suppliers.name` → Tên nhà cung cấp (DermaLab VN)

## Field LOẠI
- Tự động thanh toán ngân hàng trực tiếp không qua xác nhận (ngoài scope FR)

## Field THIẾU - CẦN BỔ SUNG
- `forecast_results.lowerBound` & `upperBound`: Khoảng biến động dải tin cậy 95%
- `forecast_runs.completedAt`: Thời điểm mô hình hoàn tất huấn luyện lần gần nhất

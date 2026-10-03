# Trung Tâm Cảnh Báo Rủi Ro Thời Gian Thực (AI Anomaly Detection) — đã đối chiếu ERD/FR

## Field GIỮ
- `ai_insights.severity` → Mức độ cảnh báo (Nghiêm trọng / Cảnh báo / Tích cực)
- `ai_insights.title` → Tiêu đề cảnh báo (Đột biến tốc độ xuất bán & Nguy cơ cạn kho Serum Bio-B5)
- `ai_insights.summary` → Tóm tắt sự cố (Livestream TikTok Shop làm đơn tăng vọt, kho Tân Bình sắp cạn)
- `ai_insights.description` → Mô tả chi tiết cảnh báo
- `ai_insights.evidence` → Dữ liệu bằng chứng (Tồn kho 18 chai, Runway 2.9 ngày, Lead-time 5 ngày)
- `ai_insights.recommendation` → Gợi ý xử lý từ AI (Khuyến nghị điều chuyển 25 chai từ Q.1 & tạo PO khẩn 150 chai)
- `ai_insights.confidence` → Độ tin cậy / Tỷ lệ AI tự động xử lý (94.2%)
- `ai_insights.createdAt` → Thời điểm phát hiện (18 phút trước)
- `inventory.quantity` → Tồn kho khả dụng (18 chai)
- `inventory.lowStockThreshold` → Ngưỡng tồn kho tối thiểu
- `inventory_batches.expiresAt` → Hạn sử dụng lô (còn 14 ngày)
- `inventory_batches.quantity` → Số lượng lô (42 chai)

## Field LOẠI
- Camera livestream real-time OCR feed / Cảm biến vật lý IoT (Không có trong ERD, ngoài scope)

## Field THIẾU - CẦN BỔ SUNG
- `ai_insights.confidence`: Độ tin cậy dự báo AI Sentinel (%)
- `ai_insights.expiresAt`: Thời hạn cảnh báo tự động hết hiệu lực
- `inventory.lowStockThreshold`: Ngưỡng tồn thấp để kích hoạt cảnh báo tự động

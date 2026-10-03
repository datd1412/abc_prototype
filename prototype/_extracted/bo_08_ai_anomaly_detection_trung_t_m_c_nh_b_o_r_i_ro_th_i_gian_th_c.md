# Trung Tâm Cảnh Báo Rủi Ro Thời Gian Thực (AI Anomaly Detection)
Nguồn: stitch_ai_business_copilot_platform/bo_08_ai_anomaly_detection_trung_t_m_c_nh_b_o_r_i_ro_th_i_gian_th_c/code.html

## Field đang hiển thị
- Bất thường khẩn cấp: 3 vấn đề (ước tính thiệt hại ~48.200.000 ₫)
- Tỷ lệ tự động xử lý: 94.2% (+3.8%)
- Thất thoát ngăn chặn: 142.500.000 ₫
- Cảm biến Sentinel active: 100% (5/5 cụm active)
- Tên sản phẩm/lô cảnh báo: Serum Bio-B5 Hydra Max, Lotion Rau Má L-20240320
- Tồn kho khả dụng: 18 chai
- Tốc độ tiêu thụ: 6.2 chai/ngày (+140%)
- Runway còn lại: 2.9 ngày
- Lead-time nhà cung cấp: 5.0 ngày
- Hạn sử dụng lô: còn 14 ngày (42 chai, 8.400.000 ₫)

## Action/Button
- Cấu hình Ngưỡng AI: Mở modal/panel thiết lập ngưỡng rủi ro
- Xuất Audit Trail (CSV): Xuất nhật ký cảnh báo
- Quét Lại Ngay: Kích hoạt AI engine quét dữ liệu mới
- Tạo PO Khẩn Cấp: Khởi tạo đơn mua hàng bổ sung
- Điều chuyển kho: Lập phiếu chuyển hàng giữa các kho
- Bỏ qua / Đã xử lý: Xử lý hoặc đóng cảnh báo

## Ghi chú UX
- Filter theo Severity: Tất cả, Nghiêm trọng, Cảnh báo, Tích cực
- Filter theo Kênh & Kho
- Thẻ cảnh báo ưu tiên (Critical feed) kèm phân tích Root-Cause từ AI Sentinel
- Sentinel Real-time Indicator (Quét mỗi 60s)

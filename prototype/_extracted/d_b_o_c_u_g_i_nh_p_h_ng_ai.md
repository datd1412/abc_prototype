# Trích xuất Nội dung: AI Forecasting & Stock-out Risk Hub (Gợi Ý Nhập Hàng AI)
**Nguồn**: `stitch_ai_business_copilot_platform/d_b_o_c_u_g_i_nh_p_h_ng_ai/`

## 1. Tiêu đề & Thông tin tổng quát
- Tiêu đề: "AI Forecasting & Stock-out Risk Hub"
- Phụ đề: "Dự báo cầu tự động, tính toán điểm đặt hàng lại (ROP) & gợi ý tối ưu gộp đơn đặt hàng NCC"
- Actions chính:
  - "Tùy chỉnh thuật toán"
  - "Xuất Excel (.xlsx)"
  - "Phê duyệt & Tạo 2 PO Đề xuất (1-chạm)"

## 2. Bộ lọc & Phân đoạn SKU
- Lọc khung thời gian: 7 ngày tới (Gấp) | 30 ngày tới (Mega 11.11 & BF) | 60 ngày (Tết).
- Lọc trạng thái rủi ro tồn:
  - Tất cả (86 SKU)
  - Nguy cơ đứt hàng cao (3)
  - Cần nhập bổ sung (7)
  - Tồn kho an toàn (62)
  - Tồn đọng / Cận date (14)

## 3. Bảng Dự Báo Cầu & Đề Xuất PO
- Cột dữ liệu:
  1. Sản phẩm & SKU, Nhà cung cấp
  2. Tồn hiện tại (Số lượng, DOI ngày tồn, Lượng hàng đang về)
  3. Tốc độ tiêu thụ & Xu hướng (Burn rate/ngày, sự kiện kích cầu)
  4. Nhu cầu dự báo 30D (AI Forecast, Khoảng tin cậy CI, Mức đệm an toàn Safety stock)
  5. Mức độ rủi ro (Khẩn cấp hết hàng, Cảnh báo vàng, Lệch biến thể, An toàn)
  6. Đề xuất nhập PO (Số lượng gợi ý)
  7. Thao tác (Tạo PO, Xem biểu đồ ROP, Đặt may/Chuyển kho)

## 4. Bảng phân tích chi tiết bổ trợ
- **Panel Trái: Điểm Đặt Hàng Lại & Rủi Ro Cạn Kho (Klairs Midnight Serum)**:
  - Tồn hiện tại: 14 chai (Dự kiến cạn ngày 28/10)
  - ROP ngưỡng kích hoạt: 35 chai
  - Thời gian NCC giao hàng (Lead time): 4 ngày
  - Nút giải pháp khẩn: [Chuyển 25 chai từ Kho Tân Bình] | [Tạo PO Khẩn cấp 120 chai]
- **Panel Phải: Tối Ưu Vốn Lưu Động & Chiết Khấu Gộp Đơn (Order Bundling)**:
  - Gợi ý: Gộp chung Serum Klairs (120 chai) và Kem Dưỡng Phyto (90 hộp) vào 1 PO gửi Klairs VN.
  - Lợi ích: Đạt mốc giá trị 50M -> Hưởng chiết khấu 5% (tiết kiệm 4.200.000 ₫) và miễn phí vận chuyển.
  - Action: [Áp Dụng Gộp PO & Giữ Chiết Khấu] | [Xem trước 2 Phiếu Đặt Hàng (PO Draft)]

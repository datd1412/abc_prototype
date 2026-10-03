# Trích xuất Nội dung: Hub Đơn Hàng & POS Đa Kênh
**Nguồn**: `stitch_ai_business_copilot_platform/qu_n_l_n_h_ng_pos_b_n_l_a_k_nh/`

## 1. Tiêu đề & Ngữ cảnh
- Tiêu đề: "Hub Đơn hàng & POS Đa kênh"
- Mô tả: Giám sát toàn diện đơn hàng từ quầy POS Showroom, sàn TMĐT Shopee/TikTok và kênh bán buôn B2B theo thời gian thực.
- Actions trên đầu:
  - "Xuất Excel (.xlsx)"
  - "Đồng bộ sàn (API)"
  - "+ Tạo đơn B2B"
  - "+ Mở Quầy POS Nhanh"

## 2. Hàng chỉ số KPI chính
1. **Tổng đơn hàng hôm nay**: 248 đơn (+18.5%)
   - GMV: 62.450.000 ₫
   - Phân bổ: POS: 72 • Shopee: 94 • TikTok: 68 • B2B: 14
2. **Chờ đóng gói & Bàn giao**: 42 đơn
   - Cảnh báo: 8 đơn gấp cần bàn giao trước 16:00 SLA (Shopee: 26 • TikTok: 16)
3. **Tỷ lệ Hủy & Hoàn trả**: 2.1% (An toàn xanh, dưới mức ngành 4.8%)
   - 5 kiện hoàn chờ kiểm tra chất lượng kho
4. **Giá trị TB đơn (AOV)**: 251.800 ₫ (+12.4%)
   - Tăng trưởng nhờ combo AI gợi ý

## 3. AI Order Intelligence Strip
- Phát hiện xung đột tồn kho, trễ hạn đơn hàng sàn và rủi ro công nợ sỉ tức thời.
- Highlight 1: TikTok Shop bùng nổ 18 đơn Serum Klairs trong 45 phút -> Đề xuất điều phối 40 chai từ Showroom sang kho Fulfillment.
- Highlight 2: Đại lý 'An Nhiên Beauty' đặt thêm đơn B2B 28.5M -> Cảnh báo hạn mức công nợ vượt 50M.

## 4. Tabs & Filter kênh bán
- "Tất cả kênh (248)"
- "POS Showroom Q.1 (72)"
- "Shopee Mall (94)"
- "TikTok Shop (68)"
- "B2B / Đại lý (14)"
- Tìm kiếm mã đơn, khách hàng, SĐT...

## 5. Bảng dữ liệu Đơn hàng đa kênh
Cột: Mã đơn & Thời gian | Kênh bán | Khách hàng & Liên hệ | Sản phẩm & Chi tiết | Tổng tiền | Thanh toán | Vận chuyển / Trạng thái | Thao tác
- Dòng 1: `#POS-202410-142` - POS Showroom - Khách lẻ tại quầy - Đầm Dạ Hội Lụa Satin Bloom - 1.250.000 ₫ - VietQR MB Bank (Đã TT) - Hoàn thành tại quầy
- Dòng 2: `#SP-89210492` - Shopee Mall - Nguyễn Hoài Thương (Đà Nẵng) - Serum Klairs Midnight Blue 30ml (2 chai) - 780.000 ₫ - ShopeePay - Đang đóng gói (SPX Express - Giao trước 16:00)
- Dòng 3: `#TT-59021481` - TikTok Shop - Trần Minh Hoàng (TP.HCM) - Combo Son Kem + Phấn Phủ - 520.000 ₫ - COD - Chờ lấy hàng (J&T Express)
- Dòng 4: `#B2B-202410-08` - B2B Đại lý - Đại lý An Nhiên Beauty - 50 Hộp Kem Chống Nắng Phyto - 18.500.000 ₫ - Chờ chuyển khoản (Công nợ Net 15) - Chờ duyệt tín dụng
- Dòng 5: `#POS-202410-141` - POS Showroom - Chị Mai Lan (VIP Diamond) - Combo Skincare Bloom Trẻ Hóa - 2.890.000 ₫ - Tiền mặt - Hoàn thành tại quầy
- Dòng 6: `#SP-89194012` - Shopee Mall - Lê Quốc Anh (Hà Nội) - Nước Tẩy Trang Rau Má Centella - 340.000 ₫ - ShopeePay - Đang vận chuyển

## 6. Khối phân tích vận tốc & phương thức thanh toán
- **Nhịp độ Đơn hàng theo Giờ (Sales Velocity)**: Histogram phân bố lưu lượng theo khung giờ trong ngày, đánh dấu đỉnh Livestream (11h-13h) và đỉnh khách ghé quầy (18h-20h).
- **Phương thức thanh toán**: VietQR Chuyển khoản (52%) | Ví Sàn ShopeePay/TikTok (34%) | Tiền mặt quầy POS (14%).

# Trích xuất Nội dung: Retail Intelligence Pulse
**Nguồn**: `stitch_ai_business_copilot_platform/retail_intelligence_pulse/DESIGN.md`

## 1. Tiêu đề & Ngữ cảnh
- Tiêu đề: "Retail Intelligence Pulse — Nhịp Đập Vận Hành Bán Lẻ"
- Mô tả: Bảng điều hành nhịp đập kinh doanh đa kênh, giám sát tốc độ bán (SKU velocity), rủi ro đọng vốn lô date và hành động điều phối tức thời theo khuyến nghị AI Copilot.
- Actions:
  - "Xuất báo cáo điều hành"
  - "Đồng bộ dữ liệu Realtime"
  - "+ Cấu hình ngưỡng cảnh báo"

## 2. 4 Chỉ số Nhịp đập (Pulse KPIs)
1. **Doanh thu đa kênh hôm nay (GMV)**: 62.450.000 ₫ (+18.5% so với TB ngày)
   - Phân bổ: POS: 29% • Shopee: 38% • TikTok: 27% • B2B: 6%
2. **Vận tốc bán trung bình (Velocity)**: 18.2 đơn/giờ
   - Đỉnh điểm: 11:00 - 13:00 (TikTok Live) và 18:00 - 20:00 (Showroom)
3. **Sức khỏe tồn kho (Inventory Health)**: 94.2% An toàn
   - 3.420 món • 4 lô cận date (< 60 ngày) • 3 SKU chạm ngưỡng tái đặt
4. **Tỷ lệ hoàn tất & SLA**: 97.9%
   - Hoàn trả 2.1% • 42 đơn chờ đóng gói bàn giao trước 16:00

## 3. Khối Khuyến nghị Ưu tiên AI (Tri-part Advisory Action Cards)
1. **Khuyến nghị 1 (Cảnh báo cháy hàng)**: "Son kem lì Merzy Velvet Tint V6 dự kiến hết hàng trong 3 ngày tới"
   - Bằng chứng: Vận tốc bán tăng +34% cuối tuần, tồn kho chỉ còn 18 thỏi quầy POS.
   - Hành động đề xuất: Tạo PO nhập thêm 60 thỏi từ NPP Merzy.
2. **Khuyến nghị 2 (Rủi ro hạn dùng FEFO)**: "Lô LOT-202405-A của Serum Klairs B5 còn 45 ngày hạn sử dụng"
   - Bằng chứng: Tồn 18 hộp tại Showroom, tốc độ bán chậm hơn chu kỳ.
   - Hành động đề xuất: Tạo Flash Sale giảm 25% hoặc xuất đổi trả NCC.
3. **Khuyến nghị 3 (Tối ưu dòng tiền thanh toán)**: "Tất toán sớm đơn hàng Klairs PO-088 trước 5 ngày"
   - Bằng chứng: Nhận thêm chiết khấu 2.5% (tiết kiệm ~3.200.000 ₫), tài khoản MB Bank thặng dư đủ điều kiện.
   - Hành động đề xuất: Thanh toán qua VietQR B2B.

## 4. Ma trận SKU Velocity & Giám sát Luân chuyển Hàng hóa
Cột: Sản phẩm & Danh mục | Kênh bán chủ lực | Tồn khả dụng | Tốc độ bán (đơn/ngày) | Dự báo số ngày còn hàng | Trạng thái AI Pulse | Thao tác
1. **Serum Klairs Midnight Blue 30ml** (Shopee Mall / TikTok) - Tồn: 34 chai - Bán: 14 đơn/ngày - Còn: 2.4 ngày - Chạm ngưỡng tái đặt
2. **Son Kem Lì Merzy The First Velvet Tint V6** (POS Showroom) - Tồn: 18 thỏi - Bán: 8 đơn/ngày - Còn: 2.2 ngày - Cảnh báo cháy hàng
3. **Đầm Dạ Hội Lụa Satin Bloom** (POS Showroom) - Tồn: 14 cái - Bán: 3 cái/ngày - Còn: 4.6 ngày - Ổn định
4. **Kem Chống Nắng Phổ Rộng Phyto Shield SPF50+** (Đa kênh) - Tồn: 86 hộp - Bán: 6 hộp/ngày - Còn: 14.3 ngày - Tồn tối ưu
5. **Nước Tẩy Trang Centella Skin1004 210ml** (Shopee Mall) - Tồn: 45 chai - Bán: 5 chai/ngày - Còn: 9.0 ngày - Ổn định

# Trích xuất Nội dung: Quản Lý Sản Phẩm, Biến Thể & Kho Lô Mỹ Phẩm
**Nguồn**: `stitch_ai_business_copilot_platform/qu_n_l_s_n_ph_m_bi_n_th_kho_l_m_ph_m/`

## 1. Tiêu đề & Ngữ cảnh
- Tiêu đề: "Quản lý Sản phẩm, Biến thể & Kho Lô Mỹ Phẩm (FEFO)"
- Mục đích: Giám sát toàn diện danh mục sản phẩm, biến thể đa thuộc tính, giá vốn COGS, và theo dõi chặt chẽ hạn dùng từng lô date theo chuẩn FEFO.
- Actions:
  - "Xuất Excel / Kiot"
  - "Nhập kho / Lô Date (PO)"
  - "AI Quét rủi ro hạn dùng"
  - "+ Thêm sản phẩm"

## 2. 4 Thẻ KPI Tồn kho & Vận hành
1. **Tổng danh mục hoạt động**: 184 SKU đang bán (3.420 món tồn kho vật lý)
2. **Giá trị vốn lưu kho**: 418.900.000 ₫ (+5.4% so với tháng trước, quay vòng 4.2x)
3. **Lô cận date (< 60 ngày)**: 4 Lô hàng (32 hộp, rủi ro 8.5M ₫)
4. **Chạm ngưỡng tái đặt**: 3 SKU cháy hàng (hụt doanh số ~18M/tuần)

## 3. AI Copilot Strip: Khuyến nghị FEFO & Tái đặt
- Khuyến nghị FEFO: Lô `LOT-202405-A` của Serum Klairs B5 còn 45 ngày hạn sử dụng (18 hộp). Đề xuất tạo Flash Sale giảm 25% hoặc xuất đổi trả NCC theo chính sách hoàn cọc trước 30 ngày.
- Cảnh báo Stockout: Áo Blazer Linen Size S đã hết hàng tại Showroom, đề xuất tạo PO khẩn cấp 30 cái.

## 4. Tabs & Filter
- "Tất cả sản phẩm (184)"
- "Theo dõi Lô Date mỹ phẩm (42 lô)"
- "Cận date / Cháy hàng (7)"
- "Nguyên tắc xuất kho FEFO (First Expired, First Out)"

## 5. Bảng dữ liệu Sản phẩm & Biến thể Lô Date
Cột: Sản phẩm & Phân loại | SKU | Biến thể (Variants) | Giá bán & Giá vốn | Tồn khả dụng / Kệ | Quản lý Lô & Hạn dùng (FEFO) | Đánh giá AI Copilot | Thao tác
1. **Serum Phục Hồi B5 Klairs Rich Moist 35ml**
   - Phân loại: K-Beauty Skincare • NCC: Klairs VN
   - SKU: `KLAIRS-B5-35`
   - Giá: Bán 380.000 ₫ • Vốn: 220.000 ₫ (Lãi gộp 42%)
   - Tồn: 34 chai (Kệ A1-02)
   - Lô FEFO: `LOT-202405-A` (HSD: 12/11/2026, còn 45 ngày - Cận date)
   - AI: Cảnh báo đỏ - Flash sale giảm 25% hoặc đổi trả NCC
2. **Áo Blazer Linen Oversize Nữ Bloom**
   - Phân loại: Thời trang thiết kế • Xưởng May Bloom Studio
   - SKU: `BLM-BLAZ-OV`
   - Biến thể: Size S (Tồn 0 - Cháy), Size M (Tồn 8), Size L (Tồn 6)
   - Giá: Bán 850.000 ₫ • Vốn: 450.000 ₫
   - AI: Cháy hàng Size S - Cần tạo PO khẩn cấp
3. **Kem Chống Nắng Phổ Rộng Phyto Shield SPF50+**
   - Phân loại: Dược mỹ phẩm • Phyto Calming VN
   - SKU: `PHYTO-SUN-50`
   - Giá: Bán 420.000 ₫ • Vốn: 240.000 ₫
   - Tồn: 86 hộp (Kệ A2-05)
   - Lô FEFO: `LOT-202610-C` (HSD: 2029 - 1.095 ngày an toàn)
   - AI: Tồn kho tối ưu, tốc độ bán ổn định
4. **Son Kem Lì Merzy The First Velvet Tint**
   - Phân loại: Make-up trendy • NPP Merzy VN
   - SKU: `MRZ-TINT-V6`
   - Biến thể: Màu V6 (Tồn 28), Màu V8 (Tồn 12), Màu V11 (Tồn 8)
   - Giá: Bán 185.000 ₫ • Vốn: 105.000 ₫
   - AI: Top 1 GMV quầy POS
5. **Nước Tẩy Trang Centella Skin1004 210ml**
   - Phân loại: Skincare làm dịu • K-Beauty
   - SKU: `CENT-TONER-210`
   - Giá: Bán 340.000 ₫ • Vốn: 195.000 ₫
   - Tồn: 45 chai
   - Lô FEFO: `LOT-202608-SK` (HSD: 2028)
   - AI: An toàn

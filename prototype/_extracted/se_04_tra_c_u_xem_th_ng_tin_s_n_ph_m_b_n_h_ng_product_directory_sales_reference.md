# SE-04: Tra Cứu Thông Tin Sản Phẩm & Bảng Giá Bán Hàng (Product Directory & Sales Reference)
Nguồn: stitch_ai_business_copilot_platform/se_04_tra_c_u_xem_th_ng_tin_s_n_ph_m_b_n_h_ng_product_directory_sales_reference/code.html

## Field đang hiển thị
- Tiêu đề màn hình: Tra Cứu & Tham Chiếu Sản Phẩm Bán Hàng (Read-Only POS Reference)
- Tìm kiếm & quét Barcode: Quét mã vạch (Honeywell F1) hoặc nhập tên SKU, mã hàng, thành phần...
- Danh mục sản phẩm (Categories):
  + Tất cả (142)
  + Serum & Tinh chất (34)
  + Kem dưỡng & Phục hồi (28)
  + Son môi & Make-up (41)
  + Nước tẩy trang & Làm sạch (19)
  + Chống nắng (20)
- Bộ lọc nhanh (Quick Filters):
  + Còn hàng tại quầy (>0)
  + Tồn thấp (< 5)
  + Có mẫu thử Tester
  + Có CTKM Đang Chạy
- Danh sách thẻ / hàng sản phẩm:
  + Tên sản phẩm: Serum Bio-B5 Hydra Max 100ml, Kem Phục Hồi Ceramide Aura Care 50ml, Son Kem Nhung Lì Velvet #03, Nước Tẩy Trang Micellar Damask Rose 400ml, Kem Chống Nắng SunShield Tone-Up 50ml, Phấn Nước Cushion Tự Nhiên SPF50+
  + Mã SKU: MB-SER-B5-01, MB-CRM-02, MB-LIP-VL-03, MB-CLEAN-01, MB-SUN-04, MB-CUSH-21
  + Vị trí kệ quầy: Kệ A1-02, Kệ B2-01, Kệ Mặt Tiền T1, Kệ C1-03, Kệ A2-04, Kệ B1-01
  + Số lượng tồn quầy: 35, 18, 42, 24, 29, 14
  + Giá niêm yết & Giá bán lẻ: 420.000 ₫ (gốc 450.000 ₫), 485.000 ₫, 260.000 ₫, 290.000 ₫, 350.000 ₫, 390.000 ₫
  + Số lô & Hạn sử dụng (FEFO): LOT-202410-B5 (HSD: 10/2027)
  + Giá vốn nội bộ (COGS): Bị che •••••••••• ₫ (Không hiển thị cho nhân viên thu ngân SE theo RBAC)
  + Hướng dẫn tư vấn & Thành phần: Thành phần chính, đối tượng sử dụng, gợi ý upsell combo

## Action/Button
- Quét mã Barcode / SKU [F1]
- Chuyển chế độ xem: Lưới (Grid) / Bảng (Table List)
- Xem Chi Tiết [F4]: Mở modal / drawer xem chi tiết sản phẩm, hạn sử dụng FEFO
- + Đơn Bán Hàng [F1]: Chuyển sản phẩm sang màn hình bán hàng POS (`se-ban-hang.html`)
- In Tem Kệ K80: In nhãn giá dán kệ quầy
- Gửi Đề Xuất Cập Nhật Lên BO: Gửi thông báo đề xuất sửa thông tin lên Business Owner

## Ghi chú UX & RBAC
- Quyền truy cập Store Employee (SE): Chỉ xem (Read-only), không có quyền chỉnh sửa giá bán hay thông tin sản phẩm.
- Che giá vốn (`costPrice`): Bảo mật thông tin tài chính trước nhân viên bán lẻ.
- Tích hợp phím tắt F1 (chuyển sang bán hàng), F4 (xem chi tiết).

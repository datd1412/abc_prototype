# SE-04: Xử Lý Đổi Trả Hàng & Hoàn Tiền Tại Quầy POS
Nguồn: stitch_ai_business_copilot_platform/se_04_x_l_i_tr_h_ng_ho_n_ti_n_b_o_h_nh_t_i_qu_y_pos/code.html

## Field đang hiển thị
- Mã hóa đơn gốc cần tra cứu: #POS-20241023-042 (hoặc SĐT khách hàng: 0909 123 456)
- Thông tin khách hàng & ngày mua: Chị Lê Thu Thảo • Mua ngày 23/10/2024 (còn hạn đổi trả 7 ngày)
- Danh sách sản phẩm trong hóa đơn gốc:
  + Sản phẩm 1: Serum Bio-B5 Hydra Max 100ml | SKU: MB-SER-B5-01 | SL: 1 | Đơn giá: 420.000 ₫ | Hành động: Chọn đổi hàng | Tình trạng: Nguyên seal, chưa bóc tem phụ
  + Sản phẩm 2: Son Kem Nhung Lì Velvet #03 | SKU: MB-LIP-VL-03 | SL: 1 | Đơn giá: 260.000 ₫ | Hành động: Khách giữ lại dùng
- Sản phẩm chọn đổi mới:
  + Tên: Kem Phục Hồi Ceramide Aura Care 50ml | SKU: MB-CRM-02 | SL: 1 | Đơn giá bán lẻ: 485.000 ₫ | Tồn quầy khả dụng: 18 | Vị trí: Kệ B2-01
- Bảng quyết toán chênh lệch tài chính:
  + Giá trị hàng trả lại: 420.000 ₫
  + Giá trị hàng đổi mới: 485.000 ₫
  + Phí đổi trả: 0 ₫ (Miễn phí theo chính sách 7 ngày)
  + Chênh lệch thu thêm từ khách: +65.000 ₫
- Phương thức thanh toán thu thêm: VietQR Pro (quét mã 65.000 ₫) hoặc Tiền mặt
- Cân bằng kho: Tự động cộng tồn kho quầy +1 cho Serum Bio-B5 và trừ tồn quầy -1 cho Kem Ceramide
- Nhân viên xử lý: Nguyễn Thị Mai (#02)

## Action/Button
- Tra cứu hóa đơn / quét barcode đơn gốc [F1]
- Chọn món trả / Chọn lý do đổi trả
- Thêm sản phẩm đổi mới [F4]
- Chuyển đổi phương thức quyết toán (Thu thêm / Hoàn tiền / Đổi 1-1 lỗi NSX)
- In Tạm [F3]
- In Biên Bản Đổi Trả [F7]
- Hủy Bỏ [Esc]
- HOÀN TẤT ĐỔI TRẢ & XUẤT HÓA ĐƠN MỚI [F9]

## Ghi chú UX
- Màn hình nghiệp vụ đổi trả hàng chuyên nghiệp tại quầy POS dành cho nhân viên thu ngân.
- Hỗ trợ cả 3 kịch bản: Khách đổi sang món giá cao hơn (Thu thêm), món giá thấp hơn (Hoàn tiền), hoặc đổi cùng loại do lỗi (Đổi 1-1).

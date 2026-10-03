# SE-01 Ghi Nhận Giao Dịch Bán Hàng POS Terminal (Store Employee POS Terminal)
Nguồn: stitch_ai_business_copilot_platform/se_01_ghi_nh_n_giao_d_ch_b_n_h_ng_pos_store_employee_pos_terminal/code.html

## Field đang hiển thị
- Thông tin ca bán: Nhân viên thu ngân (Nguyễn Thị Mai), Cửa hàng (Flagship Q.1 • Quầy #01), Ca làm việc (Ca Sáng 08:00 - 16:00), Trạng thái ca (Online)
- Phím tắt nhanh (Hotkeys): F1 (Tìm kiếm SKU), F2 (Voice Order AI), F4 (Chọn Khách hàng), F8 (Thanh toán), F9 (In hóa đơn)
- Danh mục sản phẩm & Grid bán nhanh:
  - Barcode / SKU quét nhanh
  - Tên sản phẩm, hình ảnh, đơn giá, tồn kho khả dụng
  - Sản phẩm: Serum Bio-B5 Hydra Max, Kem Phục Hồi Ceramide, Son Kem Velvet Touch, Nước Tẩy Trang Micellar...
- Giỏ hàng & Thanh toán (Cart & Checkout):
  - Khách hàng (Khách lẻ / Khách thân thiết CRM)
  - Danh sách item trong giỏ (Tên, Số lượng, Đơn giá Snapshot, Chiết khấu, Thành tiền)
  - Tổng tiền hàng (Subtotal), Chiết khấu (Discount), Thuế VAT, Tổng thanh toán (Total)
  - Phương thức thanh toán: Tiền mặt, Chuyển khoản VietQR Dynamic, Thẻ POS Bank
  - Tiền khách đưa, Tiền thừa trả lại

## Action/Button
- Quét mã vạch (Barcode Scanner)
- Voice Order AI [F2]: Nhận diện giọng nói gán tự động giỏ hàng
- Thêm sản phẩm vào giỏ
- Lưu Giỏ / Tạm Tính đơn hàng [F3]
- Áp mã giảm giá / Voucher
- Thanh toán & In hóa đơn [F8 / F9]

## Ghi chú UX
- Layout tối ưu 2 cột cho Thu ngân POS Terminal (Cột trái: Catalog & Voice Search; Cột phải: Cart & VietQR Terminal)
- AI Copilot Smart Cross-Sell Suggestion Bar
- Menu Topbar dùng riêng cho Store Employee (`se-`)

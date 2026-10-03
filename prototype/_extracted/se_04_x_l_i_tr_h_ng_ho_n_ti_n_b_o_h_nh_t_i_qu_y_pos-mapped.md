# SE-04: Xử Lý Đổi Trả Hàng & Hoàn Tiền Tại Quầy POS — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.code` → Mã hóa đơn gốc (#POS-20241023-042) & Mã hóa đơn đổi hàng mới (#POS-EX-20241024-001)
- `orders.totalAmount` / `orders.finalAmount` → Giá trị đơn hàng gốc và giá trị đơn đổi mới
- `orders.paymentMethod` → Phương thức thu thêm hoặc hoàn tiền (VietQR, Tiền mặt)
- `orders.createdAt` → Ngày mua ban đầu & ngày thực hiện đổi trả
- `order_items.quantity` → Số lượng món trả và số lượng món đổi
- `order_items.price` → Đơn giá bán lẻ tại thời điểm mua
- `products.name` → Tên sản phẩm trả / Tên sản phẩm đổi
- `product_variants.sku` → Mã SKU sản phẩm
- `product_variants.retailPrice` → Đơn giá niêm yết hiện hành
- `inventory.quantity` → Tồn kho khả dụng quầy (cập nhật tự động)
- `inventory_transactions.type` → `in` (hàng trả lại kho), `out` (hàng đổi xuất đi)
- `inventory_transactions.reason` → Lý do giao dịch kho (Đổi trả hàng tại quầy POS)
- `users.fullName` → Nhân viên thu ngân xử lý nghiệp vụ

## Field LOẠI
- `phần cứng máy in Honeywell`: Thiết bị ngoài ERD.
- `camera thẩm định AI`: Tính năng phần cứng camera không thuộc ERD.

## Field THIẾU - CẦN BỔ SUNG
- `inventory_transactions.reason`: Bắt buộc ghi nhận lý do đổi trả vào transaction kho để phục vụ kiểm toán đối soát tồn kho cuối kỳ.
- `inventory.quantity`: Hiển thị tồn quầy trước/sau khi thực hiện cân bằng đổi trả.

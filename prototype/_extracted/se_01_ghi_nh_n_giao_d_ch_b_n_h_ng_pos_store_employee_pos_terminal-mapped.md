# SE-01 Ghi Nhận Giao Dịch Bán Hàng POS Terminal — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.orderNumber` → Mã đơn hàng POS
- `orders.status` → Trạng thái đơn hàng (Hoàn tất / Tạm giữ / Hủy)
- `orders.subtotal` → Tổng tiền hàng trước giảm giá
- `orders.discount` → Giảm giá đơn hàng
- `orders.tax` → Thuế GTGT VAT
- `orders.total` → Tổng tiền thanh toán
- `order_items.productNameSnapshot` → Tên sản phẩm trong giỏ
- `order_items.skuSnapshot` → Mã SKU trong giỏ
- `order_items.quantity` → Số lượng bán
- `order_items.unitPrice` → Đơn giá bán
- `order_items.subtotal` → Thành tiền từng món
- `payments.method` → Phương thức thanh toán (Tiền mặt / VietQR / Thẻ POS Bank)
- `payments.amount` → Số tiền thanh toán
- `customers.name` → Tên khách hàng thân thiết
- `customers.phone` → Số điện thoại khách hàng

## Field LOẠI
- Camera livestream nhận diện khuôn mặt khách hàng (ngoài scope FR)

## Field THIẾU - CẦN BỔ SUNG
- `order_items.unitCost`: Đơn giá vốn thời điểm bán để tính biên lợi nhuận ca POS
- `payments.transactionCode`: Mã giao dịch ngân hàng VietQR Dynamic

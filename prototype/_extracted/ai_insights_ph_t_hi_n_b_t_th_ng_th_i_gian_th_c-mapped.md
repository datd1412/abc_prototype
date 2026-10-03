# BO: Trung Tâm AI Insights & Phát Hiện Bất Thường Real-time — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.code` → Mã 6 đơn hoàn bị trừ phí kép & 14 đơn hàng trễ giao
- `orders.status` → Trạng thái đơn hàng (returned, shipping, delayed)
- `orders.totalAmount` / `orders.finalAmount` → Giá trị đơn hàng và doanh thu tiềm năng
- `orders.paymentMethod` → Hình thức thanh toán (COD, Shopee/Ví sàn)
- `order_items.quantity` / `order_items.price` → Số lượng và đơn giá sản phẩm
- `products.name` → Phyto Calming Cream, Đầm Lụa Maxi Ruby
- `product_variants.sku` → `MP-PHYTO-50`, `DR-RUBY-MAXI`
- `inventory.quantity` → Tồn kho thực tế (8 chiếc Size S, 0 chiếc Size M)
- `inventory.lowStockThreshold` → Ngưỡng cảnh báo đứt hàng
- `inventory_batches.batchNumber` → Số lô cận hạn (`LOT-202305`)
- `inventory_batches.expiresAt` → Hạn sử dụng lô (còn 42 ngày hết hạn)
- `inventory_batches.remainingQuantity` → Tồn lô cận date (45 hộp)
- `expenses.amount` / `expenses.category` → Chi phí quảng cáo (-8.5M), chi phí vận chuyển chênh lệch (-840k)
- `purchase_orders.code` → Mã PO đặt hàng khẩn cấp
- `users.fullName` → Người quản lý phê duyệt hành động

## Field LOẠI
- `tên các đơn vị vận chuyển ngoài (J&T, GHN, Shopee Xpress)`: Không có entity đơn vị vận chuyển trong ERD.
- `TikTok Ads / Shopee Mall API`: Kênh bên ngoài không có entity trong ERD. Biểu diễn qua `expenses` và `orders`.

## Field THIẾU - CẦN BỔ SUNG
- `inventory_batches.expiresAt`: Hiển thị ngày hết hạn chính xác theo chuẩn ISO bên cạnh số ngày còn lại (42 ngày).
- `inventory.lowStockThreshold`: Bổ sung chỉ số ngưỡng an toàn để cảnh báo đứt hàng kịp thời.

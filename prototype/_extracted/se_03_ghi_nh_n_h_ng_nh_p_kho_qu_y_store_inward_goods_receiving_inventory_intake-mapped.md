# SE-03: Ghi Nhận Hàng Nhập Kho Quầy — đã đối chiếu ERD/FR

## Field GIỮ
- `products.name` → Tên sản phẩm
- `product_variants.sku` → Mã SKU
- `inventory_batches.batchNumber` → Số lô nhập (Lot/Batch)
- `inventory_batches.expiresAt` → Hạn sử dụng lô (FEFO)
- `inventory_batches.quantity` → Số lượng nhập theo lô
- `inventory_batches.remainingQuantity` → Tồn lô sau nhập
- `inventory_batches.receivedAt` → Thời điểm nhận hàng vào kho
- `inventory_transactions.referenceId` → Mã chứng từ GRN (#GRN-20241024-003)
- `inventory_transactions.type` → Loại giao dịch (`in` / Nhập kho)
- `inventory_transactions.quantity` → Số lượng thực nhập
- `inventory_transactions.beforeQuantity` → Tồn kho trước nhập
- `inventory_transactions.afterQuantity` → Tồn kho sau nhập
- `inventory_transactions.unitCost` → Đơn giá vốn điều chuyển
- `inventory_transactions.reason` → Lý do nhập (Điều chuyển nội bộ từ kho tổng)
- `inventory_transactions.createdAt` → Thời điểm ghi nhận
- `inventory.quantity` → Tồn kho hiện thời
- `inventory.reservedQty` → Tồn tạm giữ
- `inventory.lowStockThreshold` → Ngưỡng tồn thấp
- `users.fullName` → Nhân viên kiểm nhận / Quản lý duyệt

## Field LOẠI
- `phương tiện xe tải / biển số xe tải`: Không có entity quản lý đội xe/vận chuyển trong ERD.
- `camera nhận diện kiện AI`: Tính năng phần cứng camera không có entity lưu trữ trong ERD.
- `trạng thái phần cứng máy quét`: Không thuộc ERD.

## Field THIẾU - CẦN BỔ SUNG
- `inventory.lowStockThreshold`: Bổ sung để hiển thị sản phẩm sau khi nhập đã vượt qua ngưỡng an toàn hay chưa.
- `inventory_batches.receivedAt`: Lưu thời điểm nhập hàng chính xác theo NTP.

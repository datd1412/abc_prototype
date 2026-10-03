# SE-02: Kiểm Kê Tồn Kho Quầy & Quản Lý Lô Hạn Dùng FEFO — đã đối chiếu ERD/FR

## Field GIỮ
- `products.name` → Tên sản phẩm
- `product_variants.name` → Tên biến thể sản phẩm
- `product_variants.sku` → Mã SKU
- `inventory.quantity` → Tồn sổ sách (Số lượng hệ thống ghi nhận)
- `inventory.reservedQty` → Số lượng tạm giữ đơn hàng
- `inventory.lowStockThreshold` → Ngưỡng tồn thấp
- `inventory_batches.batchNumber` → Số lô hàng (Lot/Batch)
- `inventory_batches.expiresAt` → Hạn sử dụng lô (FEFO)
- `inventory_batches.remainingQuantity` → Số lượng tồn theo lô
- `inventory_batches.manufactureDate` → Ngày sản xuất
- `inventory_transactions.beforeQuantity` → Tồn trước kiểm (Tồn sổ sách)
- `inventory_transactions.afterQuantity` → Tồn sau kiểm (Thực đếm)
- `inventory_transactions.quantity` → Số lượng chênh lệch (afterQuantity - beforeQuantity)
- `inventory_transactions.type` → Loại giao dịch kho (`adjustment`)
- `inventory_transactions.reason` → Lý do lệch / điều chỉnh (Tester, hư hỏng, chưa nhập đơn chuyển...)
- `product_variants.sellingPrice` → Đơn giá bán
- `product_variants.costPrice` → Đơn giá vốn
- `users.fullName` → Nhân viên thực hiện kiểm kê
- `inventory_transactions.createdAt` → Thời gian ghi nhận kiểm kê

## Field LOẠI
- `chi nhánh riêng / đa chi nhánh`: Trong ERD chỉ có `businesses`, không có entity chi nhánh / store location riêng. Gộp quầy thành khu vực vị trí metadata trong business.
- `trạng thái máy quét Barcode Honeywell`: Trạng thái phần cứng thiết bị scanner không thuộc ERD.
- `camera quét QR`: Phụ thuộc phần cứng client, không có field trong ERD.
- `tạo tem giảm 20%`: Tính năng dynamic pricing voucher không nằm trong scope kiểm kê kho của Store Employee (FR 2.2).

## Field THIẾU - CẦN BỔ SUNG
- `inventory.lowStockThreshold`: Có trong entity `inventory` nhưng Stitch gốc chưa gắn nhãn cảnh báo trực tiếp trong từng dòng kiểm kê.
- `inventory.reservedQty`: Có trong entity `inventory`, bổ sung để nhân viên phân biệt tồn thực tế trên kệ vs hàng đang tạm giữ cho đơn online/POS khác.

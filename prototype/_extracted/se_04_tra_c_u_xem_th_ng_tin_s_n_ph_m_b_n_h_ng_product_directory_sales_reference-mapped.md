# SE-04: Tra Cứu Thông Tin Sản Phẩm & Bảng Giá Bán Hàng — đã đối chiếu ERD/FR

## Field GIỮ
- `products.name` → Tên sản phẩm
- `products.description` → Mô tả sản phẩm, thành phần tư vấn
- `categories.name` → Tên danh mục (Serum, Kem dưỡng, Son môi, v.v.)
- `product_variants.sku` → Mã SKU sản phẩm
- `product_variants.barcode` → Mã vạch quét
- `product_variants.retailPrice` → Giá bán lẻ niêm yết
- `product_variants.wholesalePrice` → Giá bán sỉ (nếu có)
- `product_variants.costPrice` → Giá vốn (ẨN / CHE với nhân viên thu ngân SE theo ma trận phân quyền RBAC)
- `product_variants.isActive` → Trạng thái kinh doanh
- `inventory.quantity` → Tồn kho khả dụng tại quầy
- `inventory.reservedQty` → Tồn tạm giữ
- `inventory.lowStockThreshold` → Ngưỡng cảnh báo tồn thấp (< 5 hoặc cấu hình)
- `inventory_batches.batchNumber` → Số lô đang lưu kho quầy (LOT)
- `inventory_batches.expiresAt` → Hạn dùng lô gần nhất (FEFO)
- `inventory_batches.remainingQuantity` → Tồn theo từng lô hạn dùng

## Field LOẠI
- `chi nhánh khác / tồn liên chi nhánh`: Không có entity đa chi nhánh trong ERD.
- `máy in tem / phần cứng honeywell`: Không thuộc ERD.
- `hồ sơ công bố bộ y tế`: Không có entity quản lý giấy tờ bộ y tế trong ERD.

## Field THIẾU - CẦN BỔ SUNG
- `inventory.lowStockThreshold`: Hiển thị chỉ báo khi tồn quầy chạm ngưỡng tối thiểu để nhân viên kịp yêu cầu bổ sung hàng từ kho.
- `product_variants.barcode`: Hiển thị mã barcode 13 số bên cạnh SKU để đối soát quét máy đọc.

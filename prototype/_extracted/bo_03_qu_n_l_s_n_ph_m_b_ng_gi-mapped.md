# BO-03: Quản lý Sản phẩm & Bảng giá — đã đối chiếu ERD/FR & Content Density

Nguồn: `abc-prototype/prototype/_extracted/bo_03_qu_n_l_s_n_ph_m_b_ng_gi.md`

## 1. Field GIỮ (Phân loại theo Content Density Rule)

### Primary Fields (Hiển thị trực tiếp trên List View — tối đa 6 cột):
- `products.name` → Tên sản phẩm
- `product_variants.sku` → Mã SKU
- `categories.name` → Danh mục sản phẩm
- `product_variants.sellingPrice` → Giá bán
- `inventory.quantity` → Số lượng tồn kho
- `products.status` / `product_variants.status` → Trạng thái (Đang bán / Tạm ẩn)

### Secondary Fields (CHỈ hiển thị trong Form Panel / Drawer khi click mở record cụ thể):
- `product_variants.costPrice` → Giá vốn (COGS)
- `product_variants.name` → Tên biến thể (màu sắc, dung tích)
- `products.productType` → Loại sản phẩm
- `products.description` → Mô tả sản phẩm
- `product_variants.attributes` → Thuộc tính biến thể (JSON)
- `inventory.reservedQty` → Số lượng tạm giữ
- `inventory.lowStockThreshold` → Ngưỡng tồn thấp
- `inventory_batches.batchNumber` → Số lô nhập (FIFO Lot)
- `inventory_batches.expiresAt` → Hạn sử dụng lô

---

## 2. Field LOẠI
- `Barcode` (`8936014298110`): LOẠI — Không có field barcode trong ERD (chỉ dùng `product_variants.sku`).
- `Giá sỉ (≥10)` (`520.000 ₫`): LOẠI — Không có bảng giá sỉ/nhiều cấp trong ERD (chỉ có `sellingPrice`).
- `Chi nhánh cửa hàng` (`Chi nhánh Q.1`): LOẠI — Không có entity/field chi nhánh trong ERD (chỉ dùng `businessId`).
- `Ma trận biên lợi nhuận danh mục`: LOẠI khỏi màn CRUD này — Khối phân tích không thuộc khuôn CRUD danh sách sản phẩm (Quy tắc 2: Content Density).
- `Mô phỏng biên giá nhanh (Simulator)`: LOẠI khỏi màn CRUD này — Khối mô phỏng thuộc màn Simulation riêng (Quy tắc 2: Content Density).

---

## 3. Navigation Placement
- Vị trí IA: Menu **Sản phẩm** ▾ → Dropdown item: **Danh sách sản phẩm**.

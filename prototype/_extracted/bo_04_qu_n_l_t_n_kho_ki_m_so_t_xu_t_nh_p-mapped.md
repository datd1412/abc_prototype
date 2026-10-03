# ERD Mapping & Data Contract — BO-04: Quản lý Tồn kho & Kiểm soát Xuất Nhập Tồn

**Slug:** `bo-kho-ton-kho`  
**Nguồn ERD:** `erd/SEP490_entities_fields.txt` (Entities: `inventory`, `inventory_batches`, `inventory_transactions`, `product_variants`)

---

## 1. Phân loại Field (Primary vs Secondary Content Density Rule)

### Primary Fields (Bảng danh sách - Tối đa 6 cột):
| Cột | Entity & Field trong ERD | Kiểu hiển thị / Quy tắc |
|---|---|---|
| 1. Sản phẩm & SKU | `product_variants.name`, `product_variants.sku` | Tên SP + Mã SKU + Ảnh thumbnail |
| 2. Lô hàng & FEFO | `inventory_batches.batchNumber`, `inventory_batches.expiresAt` | Mã lô + Hạn sử dụng FEFO |
| 3. Tồn thực tế | `inventory.quantity` | Số lượng tồn kho hiện tại (Sp/Hộp) |
| 4. Tồn tối thiểu | `inventory.lowStockThreshold` | Mức cảnh báo tồn an toàn tối thiểu |
| 5. Giá trị tồn (FIFO) | `inventory.quantity` * `inventory_batches.unitCost` | Thành tiền giá trị tồn kho (VND) |
| 6. Trạng thái | Căn cứ `quantity` vs `lowStockThreshold` & `expiresAt` | Badge: An toàn / Dưới Min Stock / Nguy cơ đứt hàng / Cận hạn FEFO |

### Secondary Fields (Bảng chi tiết Drawer / Slide-over Modal):
| Entity & Field trong ERD | Nhãn Tiếng Việt | Vị trí hiển thị |
|---|---|---|
| `inventory.reservedQty` | Tồn tạm giữ (đơn chờ xuất) | Form Drawer / Thẻ chi tiết SKU |
| `inventory_batches.supplierId` | Nhà cung cấp lô hàng | Drawer Lô hàng & Hạn dùng |
| `inventory_batches.manufactureDate` | Ngày sản xuất | Drawer Lô hàng FEFO |
| `inventory_batches.receivedAt` | Ngày nhập kho | Drawer Lô hàng FEFO |
| `inventory_batches.remainingQuantity` | Số lượng còn lại trong lô | Drawer Lô hàng FEFO |
| `inventory_batches.unitCost` | Đơn giá vốn lô (VNĐ) | Drawer & Chi tiết FIFO |
| `inventory_transactions.type` | Loại giao dịch (IN/OUT/ADJUSTMENT) | Tab Lịch sử biến động |
| `inventory_transactions.reason` | Lý do nhập/xuất/điều chỉnh | Tab Lịch sử biến động |
| `inventory_transactions.createdBy` | Người thực hiện | Tab Lịch sử biến động |

---

## 2. Kiểm tra Field không thuộc ERD (Xử lý theo Rule 3)
- **Kệ / Vị trí kho (Rack A2-04):** Không có entity Rack riêng trong ERD. Map thành thuộc tính ghi chú trong `inventory_transactions.reason` hoặc `metadata`.
- **Velocity Burn-rate / Runway days:** Chỉ số tính toán động từ AI/đơn hàng, không lưu cứng field. Giữ lại dưới dạng AI Insight / chỉ số phân tích.

---

## 3. Cập nhật Field Labels Matrix
- `quantity` → Tồn thực tế
- `reservedQty` → Tồn tạm giữ
- `lowStockThreshold` → Mức tồn tối thiểu (Min Stock)
- `batchNumber` → Mã lô hàng
- `expiresAt` → Hạn sử dụng (FEFO)
- `manufactureDate` → Ngày sản xuất
- `unitCost` → Giá vốn nhập

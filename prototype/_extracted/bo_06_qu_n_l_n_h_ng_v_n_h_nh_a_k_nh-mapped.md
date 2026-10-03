# ERD Mapping & Data Contract — BO-06: Quản lý Đơn hàng & Vận hành Đa kênh

**Slug:** `bo-don-hang`  
**Nguồn ERD:** `erd/SEP490_entities_fields.txt` (Entities: `orders`, `order_items`, `customers`, `payments`, `inventory`)

---

## 1. Phân loại Field (Primary vs Secondary Content Density Rule)

### Primary Fields (Bảng danh sách List View - 6 cột chuẩn):
| Cột | Entity & Field trong ERD | Kiểu hiển thị / Quy tắc |
|---|---|---|
| 1. Mã Đơn & Kênh | `orders.orderNumber`, `orders.createdAt` | Mã đơn `orderNumber` (ORD-...) + Kênh bán + Ngày tạo |
| 2. Khách hàng | `customers.name`, `customers.phone` | Tên KH + Số điện thoại |
| 3. Chi tiết SP | `order_items.productNameSnapshot`, `order_items.quantity` | Ảnh SP + Tên SP + Mã SKU + Số lượng |
| 4. Tổng tiền & TT | `orders.total`, `payments.method` | Tổng tiền thanh toán (VNĐ) + Phương thức thanh toán |
| 5. Tác động tồn kho | `inventory.reservedQty`, `inventory.quantity` | Badge: Giữ chỗ (Hold) / Đã trừ kho / Hoàn kho |
| 6. Trạng thái | `orders.status` | Badge: Chờ đóng gói / Đang giao / Hoàn thành / Đã hủy |

### Secondary Fields (Bảng chi tiết Slide-Over Form Drawer):
| Entity & Field trong ERD | Nhãn Tiếng Việt | Vị trí hiển thị |
|---|---|---|
| `orders.subtotal` | Tiền hàng chưa giảm | Drawer Chi tiết đơn hàng |
| `orders.discount` | Tổng chiết khấu / Giảm giá | Drawer Chi tiết đơn hàng |
| `orders.tax` | Thuế VAT | Drawer Chi tiết đơn hàng |
| `orders.cancellationReason` | Lý do hủy đơn hàng | Drawer Chi tiết đơn hàng / Modal Hủy |
| `order_items.unitCost` | Đơn giá vốn SP | Drawer Chi tiết đơn hàng |
| `payments.transactionCode` | Mã giao dịch ngân hàng / ví | Drawer Chi tiết thanh toán |
| `payments.paidAt` | Thời gian thanh toán thực tế | Drawer Chi tiết thanh toán |
| `orders.createdById` | Nhân viên tạo / Xử lý đơn | Drawer Chi tiết đơn hàng |

---

## 2. Kiểm tra Field không thuộc ERD (Xử lý theo Rule 3)
- **Tùy chọn tự chế không có trong ERD:** Đã kiểm tra 100% field hiển thị đều khớp với `orders`, `order_items`, `customers`, `payments`, `inventory`.

---

## 3. Cập nhật Field Labels Matrix
- `orders.orderNumber` → Mã đơn hàng
- `orders.status` → Trạng thái đơn hàng
- `orders.subtotal` → Tiền hàng chưa giảm
- `orders.discount` → Giảm giá
- `orders.tax` → Thuế VAT
- `orders.total` → Tổng tiền thanh toán
- `orders.cancellationReason` → Lý do hủy đơn
- `order_items.productNameSnapshot` → Tên sản phẩm
- `order_items.skuSnapshot` → Mã SKU
- `order_items.quantity` → Số lượng mua
- `order_items.unitPrice` → Đơn giá bán
- `order_items.unitCost` → Đơn giá vốn
- `payments.method` → Phương thức thanh toán
- `payments.transactionCode` → Mã giao dịch thanh toán

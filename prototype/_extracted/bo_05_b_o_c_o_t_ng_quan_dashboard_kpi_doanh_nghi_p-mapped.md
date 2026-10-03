# ERD Mapping & Data Contract — BO-05: Executive Dashboard & KPI

**Slug:** `bo-tong-quan`  
**Nguồn ERD:** `erd/SEP490_entities_fields.txt` (Entities: `orders`, `order_items`, `product_variants`, `categories`, `inventory`, `inventory_batches`)

---

## 1. Phân loại Field & Chỉ số KPI (Content Density Rule)

### Primary KPI Metrics (Executive Cards & Overview):
| Thẻ chỉ số | Entity & Field tính toán từ ERD | Công thức / Quy tắc hiển thị |
|---|---|---|
| 1. Doanh Thu Hôm Nay / Tháng | `orders.totalAmount` (Status = COMPLETED) | Sum(`totalAmount`) theo khoảng thời gian |
| 2. Lợi Nhuận Gộp | `orders.totalAmount` - Sum(`order_items.quantity` * `order_items.costPrice`) | Doanh Thu thuần - COGS |
| 3. Lợi Nhuận Ròng Ước Tính | Lợi nhuận gộp - OPEX (`expenses.amount`) | Lợi Nhuận Ròng (VNĐ) & % Tỷ suất |
| 4. Tổng Đơn Hàng | Count(`orders.id`) | Tổng số lượng đơn hàng (Đã hoàn tất / Hủy) |
| 5. Giá Trị Đơn (AOV) | Sum(`orders.totalAmount`) / Count(`orders.id`) | Giá trị đơn hàng trung bình |
| 6. Giá Trị Tồn Kho | Sum(`inventory.quantity` * `product_variants.costPrice`) | Giá trị tài sản tồn kho hiện tại |

### Primary Table (Top 5 Sản Phẩm Bán Chạy):
| Cột | Entity & Field trong ERD | Kiểu hiển thị |
|---|---|---|
| 1. Sản phẩm & SKU | `product_variants.name`, `product_variants.sku` | Tên SP + Mã SKU |
| 2. Số lượng đã bán | Sum(`order_items.quantity`) | Tổng sản lượng tiêu thụ |
| 3. Doanh thu tổng | Sum(`order_items.quantity` * `order_items.unitPrice`) | Thành tiền doanh số (VNĐ) |
| 4. Biên Lợi Nhuận | (`unitPrice` - `costPrice`) / `unitPrice` | Tỷ lệ % lợi nhuận |
| 5. Tình trạng Tồn kho | `inventory.quantity` vs `inventory.lowStockThreshold` | Badge: An toàn / Cảnh báo / Đứt hàng |

---

## 2. AI Insight Strip & Executive Analysis Mapping
- **AI Priority Insight Banner:** Cảnh báo SKU có nguy cơ đứt hàng và tác động doanh thu, trỏ sang `bo-kho-ton-kho.html`.
- **AI Executive Analysis Strip:** Phân tích điểm bùng nổ doanh số và biên lợi nhuận, trỏ sang `bo-ai-phan-tich.html`.

---

## 3. Cập nhật Field Labels Matrix
- `orders.totalAmount` → Tổng doanh thu
- `order_items.quantity` → Số lượng bán
- `order_items.unitPrice` → Giá bán đơn
- `order_items.costPrice` → Giá vốn đơn

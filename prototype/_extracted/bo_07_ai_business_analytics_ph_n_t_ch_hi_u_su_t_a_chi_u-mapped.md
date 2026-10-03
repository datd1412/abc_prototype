# ERD Mapping & Data Contract — BO-07: AI Business Analytics & Phân Tích Đa Chiều

**Slug:** `bo-ai-phan-tich`  
**Nguồn ERD:** `erd/SEP490_entities_fields.txt` (Entities: `orders`, `order_items`, `product_variants`, `categories`, `expenses`, `inventory`)

---

## 1. Phân loại Field & Chỉ số Phân Tích (Content Density Rule)

### Primary Analytics Metrics (4 Thẻ trụ cột & Root-Cause):
| Chỉ số / Thẻ | Entity & Field trong ERD | Công thức / Quy tắc tính toán |
|---|---|---|
| 1. Tăng Trưởng Thực (Real Growth) | `orders.totalAmount` (Status = COMPLETED) | Sum(`totalAmount`) vs Target |
| 2. Hiệu Suất Lợi Nhuận Gộp | (`totalAmount` - `cogs`) / `totalAmount` | Doanh thu - Giá vốn / Doanh thu |
| 3. OPEX Ratio (Tỷ lệ chi phí) | `expenses.amount` / `orders.totalAmount` | Tổng chi phí vận hành / Doanh thu |
| 4. Chu Kỳ Tiền Mặt (CCC) | Kho `inventory.quantity` & Công nợ | Số ngày quay vòng kho & thu hồi nợ |

### Primary Table (Ma Trận BCG Danh Mục 142 SKU):
| Nhóm Ma Trận | Entity & Field trong ERD | Tiêu chí phân loại |
|---|---|---|
| Ngôi sao (Stars) | `product_variants.name`, `order_items.quantity`, `order_items.unitPrice` | Tăng trưởng cao + Biên LN > 45% |
| Bò sữa (Cash Cows) | `product_variants.name`, `order_items.quantity` | Doanh số ổn định + Dòng tiền đều |
| Dấu hỏi (Questions) | `product_variants.name`, `order_items.unitCost` | Tăng trưởng nhanh + Biên LN mỏng < 25% |
| Chó cưng (Dogs) | `inventory.quantity`, `inventory_batches.receivedAt` | Tồn kho > 120 ngày + Doanh số chậm |

---

## 2. AI Root-Cause Analysis Mapping
- **Positive Anomaly (15/10 - 20/10):** Phân tích đột biến doanh thu Skincare TikTok Shop, trỏ đề xuất sang `bo-don-hang.html` hoặc `bo-san-pham-danh-sach.html`.
- **Fatigue Alert (Ads Fatigue):** Cảnh báo bão hòa TikTok Ads, trỏ sang `bo-chi-phi.html`.

---

## 3. Cập nhật Field Labels Matrix
- Tất cả field sử dụng đều đã có mặt trong `field-labels.md`.

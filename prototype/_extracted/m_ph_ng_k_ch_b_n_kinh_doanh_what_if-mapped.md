# Ánh xạ ERD: Phòng Thí Nghiệm Kịch Bản Kinh Doanh What-If
**File nguồn UI**: `stitch_ai_business_copilot_platform/m_ph_ng_k_ch_b_n_kinh_doanh_what_if/`
**File đích**: `prototype/screens/bo-ai-mo-phong-whatif.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Doanh thu thuần (GMV) | `sales_orders` | `totalAmount` | Có | Doanh số cơ sở & mô phỏng |
| Giá vốn hàng bán (COGS) | `products` / `inventory_batches` | `costPrice` | Có | Chi phí giá vốn SKU |
| Chi phí Marketing / Ads | `expenses` | `amount`, `category` | Có | ERD có entity expenses |
| Lợi nhuận ròng | Computed | `totalAmount - expenses - cogs` | Có | Công thức chuẩn P&L |
| Khuyến nghị AI / Kịch bản | `ai_recommendations` | `title`, `description`, `actionType` | Có | Đề xuất tối ưu kinh doanh |
| Tạo đơn đặt hàng NCC | `purchase_orders` | `orderNumber`, `quantityOrdered`, `status` | Có | Nút Tạo PO kết nối sang PO |

## 2. Xử lý field
- Các tham số độ co giãn cung cầu và tỷ lệ tăng trưởng là biến số mô phỏng thuật toán AI dựa trên lịch sử bán lẻ.
- Lưu kịch bản và áp dụng kế hoạch được ánh xạ sang cấu hình mục tiêu kinh doanh của doanh nghiệp.

# Ánh xạ ERD: Báo cáo Tổng quan Chủ Cửa hàng (Store Overview)
**File nguồn UI**: `stitch_ai_business_copilot_platform/b_o_c_o_t_ng_quan_ch_c_a_h_ng/`
**File đích**: `prototype/screens/bo-tong-quan-cua-hang.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Tên chủ shop / nhân sự | `users` | `name`, `email` | Có | "Nguyễn Thị Mai" |
| Doanh thu thuần | `sales_orders` | `totalAmount`, `paymentStatus` | Có | Tổng doanh thu đơn hoàn tất |
| Chi phí phát sinh | `expenses` | `amount`, `status` | Có | Tổng chi phí APPROVED/PAID |
| Lợi nhuận ròng | Computed | `totalAmount - expenses` | Có | Tính toán từ order & expense |
| Giá trị tồn kho | `inventory_batches` | `quantityOnHand * costPrice` | Có | Định giá tồn kho vốn lưu động |
| Sản phẩm bán chạy (Top SKU) | `products` / `order_items` | `name`, `sku`, `price`, `quantity` | Có | Lấy từ order_items |
| Cảnh báo hạn dùng / tồn | `inventory_batches` | `batchCode`, `quantityOnHand`, `expiresAt`, `status` | Có | FEFO cảnh báo |
| Ngưỡng tồn an toàn | `products` | `lowStockThreshold` | Có | ERD có |
| Đơn hàng live stream | `sales_orders` | `orderNumber`, `customerName`, `totalAmount`, `paymentStatus`, `createdAt` | Có | Đơn hàng gần nhất |
| Khuyến nghị AI | `ai_recommendations` | `title`, `description`, `actionType`, `priority`, `status` | Có | Khuyến nghị hành động |

## 2. Loại bỏ / Điều chỉnh theo ERD
- Stitch có đề cập một số khái niệm camera AI theo dõi khách vào cửa hàng -> Không có trong ERD, loại bỏ hoàn toàn.
- Giữ nguyên các metrics tài chính, top sản phẩm, lô hàng hạn dùng, đơn hàng mới nhất và hành động AI.

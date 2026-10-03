# Ánh xạ ERD: Dự Báo Cầu & Gợi Ý Nhập Hàng AI
**File nguồn UI**: `stitch_ai_business_copilot_platform/d_b_o_c_u_g_i_nh_p_h_ng_ai/`
**File đích**: `prototype/screens/bo-ai-du-bao-goi-y-nhap.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Tên sản phẩm, SKU | `products` | `name`, `sku`, `price`, `costPrice` | Có | Thông tin SKU |
| Ngưỡng tồn an toàn | `products` | `lowStockThreshold` | Có | Đã đối chiếu ERD |
| Tồn kho hiện tại | `inventory_batches` | `quantityOnHand` | Có | Tổng tồn các lô |
| Nhà cung cấp | `suppliers` | `name`, `code`, `contactName` | Có | Klairs VN, Merzy VN... |
| Đề xuất nhập PO | `purchase_orders` / `po_items` | `orderNumber`, `quantityOrdered`, `status` | Có | Khởi tạo đơn đặt hàng NCC |
| Khuyến nghị AI / Dự báo | `ai_recommendations` | `title`, `description`, `actionType`, `priority` | Có | Dự báo nhu cầu & gộp đơn |
| Biến thể sản phẩm (Size S/M/L) | `products` / `product_variants` | `name`, `sku`, `attributes` | Có | Đầm Dạ Hội size M |

## 2. Xử lý field
- Các chỉ số thống kê toán học (DOI - Days of Inventory, CI - Confidence Interval, Lead time, ROP) là kết quả phân tích AI tính từ dữ liệu `sales_orders` và `inventory_batches`, hoàn toàn phù hợp nghiệp vụ.
- Đề xuất tạo PO sẽ điều hướng sang `se-nhap-kho.html` hoặc mở modal `bo-modal-po-draft-preview-1.html`.

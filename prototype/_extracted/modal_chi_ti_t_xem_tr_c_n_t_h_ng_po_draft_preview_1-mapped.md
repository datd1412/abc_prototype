# Ánh xạ ERD: Xem Trước & Phê Duyệt Đơn Đặt Hàng (PO Draft Preview 1)
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_1/`
**File đích**: `prototype/screens/bo-modal-po-draft-preview-1.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã đơn PO | `purchase_orders` | `orderNumber` | Có | #PO-20261028-KL01 |
| Nhà cung cấp | `suppliers` | `name`, `code`, `contactName`, `phone`, `email` | Có | Klairs VN, Trần Minh Quân |
| Địa điểm nhận hàng | `inventory_batches` | `warehouseId` (hoặc `notes`) | Có | Kho Logistics Tân Bình |
| Mặt hàng & SKU | `products` / `po_items` | `productId`, `sku`, `name` | Có | Serum Midnight, Kem Phyto |
| Số lượng đặt hàng | `po_items` | `quantityOrdered` | Có | 200 chai, 150 hộp |
| Đơn giá & Thành tiền | `po_items` | `unitPrice`, `subtotal` | Có | 252.200 ₫, 88.270.000 ₫ |
| Chiết khấu đơn hàng | `purchase_orders` | `discountAmount` | Có | Chiết khấu gộp sỉ |
| Điều khoản thanh toán | `purchase_orders` | `paymentTerms`, `dueDate` | Có | Net 0, Net 15 ngày |
| Trạng thái đơn | `purchase_orders` | `status` | Có | DRAFT, APPROVED, SENT |
| Ngày dự kiến nhận | `purchase_orders` | `expectedDeliveryDate` | Có | 29/10/2026 |

## 2. Xử lý field
- Các field đầy đủ, khớp 100% với entity `purchase_orders` và `po_items` trong ERD.
- Giao diện thiết kế theo chuẩn Odoo Purchase Order Form View (Breadcrumbs, Statusbar: Draft -> Confirmed -> Sent -> Received, Notebook Tabs, Footer fixed actions).

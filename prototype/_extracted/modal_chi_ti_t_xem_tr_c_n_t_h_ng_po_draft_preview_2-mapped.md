# Ánh xạ ERD: Xem Trước & Phê Duyệt PO Dự Báo Mega 11.11 (PO Draft Preview 2)
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_2/`
**File đích**: `prototype/screens/bo-modal-po-draft-preview-2.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã đơn PO 01 / PO 02 | `purchase_orders` | `orderNumber` | Có | #PO-20261028-KL01, #PO-20261028-BL02 |
| Nhà cung cấp xưởng may | `suppliers` | `name`, `code`, `contactName`, `phone` | Có | Xưởng May May Mặc Bloom |
| Mặt hàng & SKU biến thể size | `products` / `po_items` | `name`, `sku` | Có | Đầm Dạ Hội Silk Maxi Size M |
| Số lượng đặt may | `po_items` | `quantityOrdered` | Có | 50 chiếc |
| Đơn giá sản xuất & Thành tiền | `po_items` | `unitPrice`, `subtotal` | Có | 490.000 ₫, 24.500.000 ₫ |
| Điều khoản đặt cọc | `purchase_orders` | `paymentTerms` | Có | Cọc 30%, 70% khi nhận |
| Ngày giao hàng cam kết | `purchase_orders` | `expectedDeliveryDate` | Có | 27/10/2026 |

## 2. Xử lý field
- Khớp 100% với entity `purchase_orders`, `po_items`, `suppliers` trong ERD.
- Giao diện có nút chuyển Tab qua lại giữa PO 01 và PO 02 để quản lý duyệt hàng loạt trước thềm chiến dịch Mega 11.11.

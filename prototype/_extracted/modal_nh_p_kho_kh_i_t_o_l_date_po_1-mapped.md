# Ánh xạ ERD: Tạo Phiếu Nhập Kho & Khởi Tạo Lô Date PO 1
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_nh_p_kho_kh_i_t_o_l_date_po_1/`
**File đích**: `prototype/screens/bo-modal-nhap-kho-po-1.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã PO | `purchase_orders` | `orderNumber` | Có | #PO-202610-088 |
| Nhà cung cấp | `suppliers` | `name`, `code` | Có | Klairs VN |
| Sản phẩm & SKU | `products` | `name`, `sku`, `costPrice` | Có | Serum Midnight, Kem Phyto |
| Mã lô nhập | `inventory_batches` | `batchCode` | Có | LOT-KLAIRS-202610 |
| Ngày sản xuất (NSX) | `inventory_batches` | `manufactureDate` (hoặc `createdAt`) | Có | 15/09/2026 |
| Hạn sử dụng (HSD) | `inventory_batches` | `expiresAt` | Có | 15/09/2029 |
| Số lượng nhập | `inventory_batches` | `quantityOnHand` | Có | 120 chai, 80 hộp |
| Giá nhập hàng | `po_items` / `inventory_batches` | `unitPrice` | Có | 210.000 ₫, 195.000 ₫ |
| Tổng tiền nhập | `purchase_orders` | `totalAmount` | Có | 40.800.000 ₫ |
| Trạng thái lô | `inventory_batches` | `status` | Có | ACTIVE |

## 2. Xử lý field
- Khớp 100% với entity `inventory_batches` và `purchase_orders` trong ERD.
- Giao diện thiết kế theo chuẩn Odoo Stock Picking / Inward Goods Intake Form View.

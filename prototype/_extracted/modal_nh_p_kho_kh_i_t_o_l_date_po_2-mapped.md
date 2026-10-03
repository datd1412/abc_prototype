# Ánh xạ ERD: Tạo Phiếu Nhập Kho & Khởi Tạo Lô Date PO 2 (Tách Nhiều Lô Date)
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_nh_p_kho_kh_i_t_o_l_date_po_2/`
**File đích**: `prototype/screens/bo-modal-nhap-kho-po-2.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã PO | `purchase_orders` | `orderNumber` | Có | #PO-202610-088 |
| SKU sản phẩm | `products` | `sku`, `name` | Có | Serum Midnight |
| Mã lô tách A & B | `inventory_batches` | `batchCode` | Có | LOT-KLAIRS-202610-A, B |
| Ngày sản xuất (NSX) | `inventory_batches` | `manufactureDate` | Có | 15/09/2026, 20/10/2026 |
| Hạn sử dụng (HSD) | `inventory_batches` | `expiresAt` | Có | 15/09/2029, 20/10/2029 |
| Số lượng từng lô | `inventory_batches` | `quantityOnHand` | Có | 80 chai + 40 chai = 120 |
| Trạng thái lô | `inventory_batches` | `status` | Có | ACTIVE |

## 2. Xử lý field
- Trong ERD, 1 sản phẩm (`productId`) có quan hệ 1-N với `inventory_batches`, nên việc 1 dòng PO tách thành nhiều bản ghi batch khác nhau trong `inventory_batches` hoàn toàn chuẩn xác với mô hình dữ liệu.

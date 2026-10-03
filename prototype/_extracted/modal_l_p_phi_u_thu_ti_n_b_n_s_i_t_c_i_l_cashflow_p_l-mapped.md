# Ánh xạ ERD: Lập Phiếu Thu Tiền Bán Sỉ & Đối Tác Đại Lý
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_l_p_phi_u_thu_ti_n_b_n_s_i_t_c_i_l_cashflow_p_l/`
**File đích**: `prototype/screens/bo-modal-phieu-thu-ban-si.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã phiếu thu | `bank_transactions` / `sales_orders` | `referenceNumber` (hoặc `id`) | Có | #PT-202610-89 |
| Số tiền thu | `sales_orders` / `bank_transactions` | `amount`, `paidAmount` | Có | 42.500.000 ₫ |
| Khách hàng / Đại lý | `customers` (hoặc `sales_orders.customerName`) | `name`, `phone`, `email` | Có | An Nhiên Beauty Đà Nẵng |
| Chứng từ đơn hàng xuất sỉ | `sales_orders` | `orderNumber`, `totalAmount` | Có | #SO-B2B-202610-042 |
| Phương thức thanh toán | `sales_orders` | `paymentMethod`, `paymentStatus` | Có | VIETQR / BANK_TRANSFER |
| Ngày thu tiền | `sales_orders` | `updatedAt` / `createdAt` | Có | 02/10/2026 |
| Số dư sau thu | `bank_transactions` | `balance` | Có | Tăng số dư dòng tiền |

## 2. Xử lý field
- Khớp 100% với các entity `sales_orders`, `bank_transactions` trong ERD.
- Giao diện thiết kế theo chuẩn Odoo Receipt Voucher Form View với mã VietQR nạp động và tùy chọn hạch toán kế toán tự động.

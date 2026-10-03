# Ánh xạ ERD: Lập Phiếu Chi Tiền & Thanh Toán VietQR B2B
**File nguồn UI**: `stitch_ai_business_copilot_platform/modal_l_p_phi_u_chi_ti_n_qu_t_vietqr_b2b_cashflow_p_l/`
**File đích**: `prototype/screens/bo-modal-phieu-chi-vietqr.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã phiếu chi | `expenses` | `expenseNumber` (hoặc `id`) | Có | #PC-202610-09 |
| Số tiền chi | `expenses` | `amount` | Có | 34.515.000 ₫ |
| Phân loại chi phí | `expenses` | `category` | Có | SUPPLIER_PAYMENT / OPEX |
| Ngày lập phiếu | `expenses` | `expenseDate` | Có | 02/10/2026 |
| Người nhận / Nhà cung cấp | `suppliers` | `name`, `bankAccount`, `bankName` | Có | Klairs VN |
| Chứng từ PO đính kèm | `purchase_orders` | `id`, `orderNumber` | Có | #PO-202610-088 |
| Phương thức thanh toán | `expenses` | `paymentMethod` | Có | BANK_TRANSFER / VIETQR |
| Trạng thái phiếu | `expenses` | `status` | Có | PENDING, APPROVED, PAID |
| Biến động số dư ngân hàng | `bank_transactions` | `amount`, `balance` | Có | Ghi nhận sổ phụ |

## 2. Xử lý field
- Khớp 100% với các entity `expenses`, `suppliers`, `purchase_orders` và `bank_transactions` trong ERD.
- Giao diện thiết kế theo chuẩn Odoo Expense Payment Form View với drawer/modal chi tiết, hiển thị mã VietQR B2B động và cảnh báo thanh khoản an toàn từ Copilot AI.

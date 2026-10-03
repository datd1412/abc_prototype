# Ánh xạ ERD: Mô Phỏng Kịch Bản What-If Dòng Tiền & Thanh Khoản
**File nguồn UI**: `stitch_ai_business_copilot_platform/m_ph_ng_k_ch_b_n_what_if_d_ng_ti_n_p_l_c_thanh_kho_n/`
**File đích**: `prototype/screens/bo-ai-mo-phong-dong-tien.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Dòng tiền thu từ bán lẻ | `sales_orders` | `totalAmount`, `paymentStatus` | Có | Tiền thu bán hàng |
| Dòng tiền chi NCC (PO) | `purchase_orders` / `expenses` | `totalAmount`, `status`, `paymentTerms` | Có | Công nợ nhà cung cấp |
| Dòng tiền chi vận hành / Lương | `expenses` | `amount`, `category`, `status` | Có | Chi phí OPEX |
| Giao dịch ngân hàng / Ví | `bank_transactions` | `amount`, `transactionType`, `balance` | Có | Biến động số dư |
| Khuyến nghị dòng tiền AI | `ai_recommendations` | `title`, `description`, `actionType` | Có | Cảnh báo đáy tiền mặt |
| Lịch hẹn trả PO | `purchase_orders` | `dueDate`, `paymentStatus` | Có | Hạn thanh toán công nợ |

## 2. Xử lý field
- Điểm đáy tiền mặt (Cash dip) và thời gian tồn tại (Runway) là các chỉ số tài chính tính toán từ dòng tiền thu chi thực tế, khớp hoàn toàn với bản chất thực chi trong ERD.

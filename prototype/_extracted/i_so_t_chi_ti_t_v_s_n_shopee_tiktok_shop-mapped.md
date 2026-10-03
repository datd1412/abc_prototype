# Ánh xạ ERD: Đối Soát Chi Tiết Ví Sàn TMĐT
**File nguồn UI**: `stitch_ai_business_copilot_platform/i_so_t_chi_ti_t_v_s_n_shopee_tiktok_shop/`
**File đích**: `prototype/screens/bo-thanh-toan-doi-soat-san.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Mã đơn hàng sàn | `sales_orders` | `orderNumber`, `channel` | Có | Kênh Shopee, TikTok |
| Khách hàng, sản phẩm | `sales_orders` / `order_items` | `customerName`, `productName` | Có | Thông tin đơn hàng |
| Doanh số (GMV) | `sales_orders` | `totalAmount` | Có | Tổng tiền khách trả |
| Trợ giá / Giảm giá | `sales_orders` | `discountAmount` | Có | Chiết khấu sàn/shop |
| Phí sàn / Chi phí trừ | `expenses` hoặc computed | `amount`, `category` | Có | Phí sàn TMĐT |
| Thực nhận ví | Computed | `totalAmount - fees` | Có | Doanh thu ròng sau phí |
| Trạng thái thanh toán | `sales_orders` | `paymentStatus` | Có | PAID, RECONCILED, DISPUTED |
| Rút tiền về ngân hàng | `bank_transactions` / `expenses` | `amount`, `referenceNumber`, `status` | Có | Lệnh chuyển tiền về Bank |

## 2. Xử lý field
- Biểu phí take-rate và bóc tách voucher là đặc thù sàn TMĐT, được ánh xạ vào chi phí bán hàng và chiết khấu đơn hàng trong ERD.
- Giữ nguyên các chức năng giải trình phí và khiếu nại để phục vụ đối soát tài chính đa kênh.

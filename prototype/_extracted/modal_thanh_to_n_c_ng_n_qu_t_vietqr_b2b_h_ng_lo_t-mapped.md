# Bảng Ánh Xạ ERD: Thanh Toán Công Nợ Đối Tác & Lập Lệnh VietQR B2B Hàng Loạt

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `purchase_orders`, `suppliers`, `expenses`.
- Đối chiếu:
  - `suppliers.name`: "Cty TNHH Mỹ phẩm Quốc tế Klairs VN", "Xưởng May Bloom Studio", "Xưởng Bao Bì EcoPack"
  - `suppliers.phone`: Số liên hệ
  - `purchase_orders.poNumber`: `#PO-202410-088`, `#PO-BLAZER-02`, `#PO-ECO-102`
  - `purchase_orders.totalAmount`: Giá trị nợ gốc đơn hàng
  - `purchase_orders.status`: `pending` / `completed`
  - `expenses.amount`: 73.215.000 ₫ (Tổng thực chi sau cấn trừ)
  - `expenses.category`: `purchases` / `supplier_payment`
  - `expenses.paymentMethod`: `bank_transfer` (VietQR)
  - `expenses.referenceId`: Mã giao dịch ngân hàng / PO batch ref

## 2. Component Contract
- Modal 2 cột (Desktop B2B payment layout):
  - Cột trái (58%): Danh sách các chứng từ / công nợ cần thanh toán kèm checkbox, chi tiết nợ gốc, chiết khấu / cấn trừ, thực chi, và thẻ tổng hợp chi phí.
  - Cột phải (42%): Cổng VietQR Pro B2B hiển thị mã QR động, thông tin tài khoản thụ hưởng, cú pháp nội dung chuyển khoản tự động, và các nút tiện ích (Sao chép, In UNC).
- Bottom Action bar: "Hủy bỏ / Quay lại" + "Đã Chuyển Khoản - Xác Nhận & Giảm Trừ Sổ Nợ".

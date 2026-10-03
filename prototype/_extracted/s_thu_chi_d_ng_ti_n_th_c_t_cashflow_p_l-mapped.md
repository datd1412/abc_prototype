# Bảng Ánh Xạ ERD: Sổ Thu Chi & Quản Trị Dòng Tiền Thực Tế

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `expenses`, `orders`, `suppliers`, `businesses`.
- Đối chiếu các trường:
  - `expenses.id`, `expenses.amount`: Giá trị thu/chi
  - `expenses.category`: `purchases`, `marketing`, `rent`, `salary`, `utilities`
  - `expenses.paymentMethod`: `cash`, `bank_transfer`, `card`
  - `expenses.referenceId`: Mã phiếu liên quan (`PC-202410-09`, `PO-088`,...)
  - `expenses.status`: `completed`, `pending`
  - `orders.totalAmount`, `orders.finalAmount`, `orders.paymentMethod`, `orders.paymentStatus`
  - `suppliers.name`
- Loại bỏ theo Rule 3:
  - Bỏ OCR hóa đơn (Rule 3 cấm vì không có trong ERD).
  - Không có field ngoài ERD.

## 2. Component Contract
- Page Shell: Sidebar trái + Topbar (tên màn hình, role hiện tại) kèm `nav-owner.js`.
- 4 KPI Cards:
  - Tổng Tiền Vào Inflow (+284.5M)
  - Tổng Tiền Ra Outflow (-198.85M)
  - Dòng Tiền Thuần Net FCF (+85.65M)
  - Số Dư Khả Dụng Runway (96.785M)
- AI Insight Strip: Cảnh báo thanh khoản và nhắc rút tiền từ ví sàn Shopee/TikTok trước hạn thanh toán PO 31/10.
- Nhật Ký Thu Chi Quản Trị Table: Mã phiếu, Hạng mục, Đối tác, Kênh TT, Số tiền, Trạng thái, Thao tác.
- Bottom Box: Phân tích Chênh lệch Kế toán dồn tích (Accrual P&L) vs Dòng tiền thực tế (Cashflow).

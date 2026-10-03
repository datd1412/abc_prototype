# Bảng Ánh Xạ ERD: Quản Lý Nhà Cung Cấp & Công Nợ Đơn Hàng

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `suppliers`, `purchase_orders`, `expenses`.
- Đối chiếu:
  - `suppliers.name`: Tên nhà cung cấp (Cty Klairs VN, NPP Merzy, Xưởng Bloom Studio,...)
  - `suppliers.phone`: Số điện thoại đầu mối
  - `suppliers.email`: Email liên hệ
  - `suppliers.address`: Địa chỉ cơ sở nhà cung cấp
  - `suppliers.status`: Trạng thái hợp tác (`active`, `suspended`)
  - `purchase_orders.supplierId`: Khóa ngoại trỏ tới supplier
  - `purchase_orders.totalAmount`: Tổng tiền lũy kế / đơn hàng PO
  - `purchase_orders.status`: `completed`, `pending`
  - `expenses.amount`: Số tiền đã chi trả / phiếu chi công nợ
  - `expenses.category`: `purchases` / `supplier_payment`
- Loại bỏ theo Rule 3:
  - Không có OCR hay field ngoài ERD.

## 2. Component Contract
- Page Shell: Sidebar trái + Topbar (tên màn hình, role hiện tại) kèm `nav-owner.js`.
- 4 KPI Cards:
  - Tổng công nợ phải trả NCC: 148.650.000 ₫
  - Đến hạn thanh toán < 7 ngày: 42.800.000 ₫
  - Giá trị nhập hàng tháng: 215.400.000 ₫
  - Chiết khấu tích lũy đạt được: 12.850.000 ₫
- AI Insight Strip: Cơ hội chiết khấu sớm 2.5% cho Klairs VN và cảnh báo trễ hẹn giao hàng Bloom Studio.
- Tabs & Filter Bar: Phân loại NCC theo trạng thái nợ, ô tìm kiếm NCC.
- List View Table:
  - Cột: Nhà Cung Cấp & Đầu Mối, Ngành Hàng & SKU Chủ Lực, Uy Tín & Hiệu Suất, Giao Dịch Lũy Kế, Công Nợ & Kỳ Hạn, Hạn Mức & Điều Khoản, Thao Tác.
  - Quick action nút "Thanh toán VietQR" trỏ sang `bo-modal-thanh-toan-cong-no-vietqr.html`.
- Pagination Footer.

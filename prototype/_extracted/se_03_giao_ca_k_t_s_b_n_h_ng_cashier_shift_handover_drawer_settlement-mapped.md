# SE-03: Giao Ca & Kết Sổ Bán Hàng — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.totalAmount` / `orders.finalAmount` → Tổng doanh thu ca trực (24.850.000 ₫)
- `orders.paymentMethod` → Phân bổ theo phương thức thanh toán (Tiền mặt, Chuyển khoản VietQR, Thẻ/Ví)
- `orders.paymentStatus` → Trạng thái thanh toán (Đã thanh toán)
- `orders.code` → Mã hóa đơn bán lẻ phát sinh trong ca
- `orders.createdAt` → Thời điểm giao dịch trong khung giờ ca trực
- `expenses.amount` → Các khoản chi tiền mặt tại két (-300.000 ₫)
- `expenses.category` → Danh mục chi phí (Văn phòng phẩm / Vận hành quầy)
- `expenses.paymentMethod` → Hình thức thanh toán (Tiền mặt / Cash)
- `expenses.status` → Trạng thái duyệt chi (approved)
- `users.fullName` → Tên thu ngân giao ca, thu ngân nhận ca, quản lý ca trực

## Field LOẠI
- `hạ tầng thiết bị trạm thu ngân (tình trạng máy quét, dây mạng LAN, két cơ)`: Phần cứng không có entity trong ERD.
- `camera két tiền`: Không thuộc ERD.

## Field THIẾU - CẦN BỔ SUNG
- `expenses.category`: Hiển thị rõ mục đích chi tiền mặt tại két để đối soát sổ quỹ.
- `orders.paymentMethod`: Tách rõ tỷ trọng Tiền mặt vs VietQR/Chuyển khoản để khớp chính xác với số dư két thực tế.

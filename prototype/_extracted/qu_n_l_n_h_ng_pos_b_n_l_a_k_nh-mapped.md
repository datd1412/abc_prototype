# Bảng Ánh Xạ ERD: Hub Đơn Hàng & POS Đa Kênh

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `orders`, `order_items`, `customers`, `products`, `product_variants`.
- Đối chiếu các trường:
  - `orders.orderNumber`: Mã đơn hàng `#POS-202410-142`, `#SP-89210492`, `#TT-59021481`, `#B2B-202410-08`
  - `orders.customerId`: Khách hàng
  - `orders.orderType`: `pos` / `retail` / `wholesale` / `ecommerce`
  - `orders.totalAmount`: Tổng tiền đơn hàng
  - `orders.discountAmount`: Chiết khấu
  - `orders.finalAmount`: Số tiền thực thu
  - `orders.paymentMethod`: `cash`, `bank_transfer`, `card`, `cod`
  - `orders.paymentStatus`: `pending`, `paid`, `partial`, `refunded`
  - `orders.status`: Trạng thái đơn (`draft`, `pending`, `processing`, `completed`, `cancelled`)
  - `customers.fullName`, `customers.phoneNumber`, `customers.address`
  - `order_items.productVariantId`, `order_items.quantity`, `order_items.unitPrice`, `order_items.totalPrice`
- Loại bỏ theo Rule 3:
  - Không có OCR hay field ngoài ERD.

## 2. Component Contract
- Page Shell: Sidebar trái (menu module) + Topbar (tên màn hình, role hiện tại).
- KPI Cards hàng ngang (4 cards):
  - Tổng đơn hôm nay (248 đơn, GMV 62.45M)
  - Chờ đóng gói & SLA (42 đơn)
  - Tỷ lệ hoàn hủy (2.1%)
  - Giá trị trung bình đơn AOV (251.8K)
- AI Insight Strip: Phát hiện xung đột tồn kho và đơn gấp sàn TMĐT.
- Filter Bar & Channel Tabs: Tất cả, POS Quầy, Shopee, TikTok Shop, B2B Đại lý.
- List View Table: Mã đơn, Thời gian, Kênh bán, Khách hàng, Sản phẩm, Tổng tiền, Thanh toán, Vận chuyển/Trạng thái, Thao tác.
- Bottom Widgets: Biểu đồ nhịp độ đơn hàng (Sales Velocity) & Phân bổ phương thức thanh toán.

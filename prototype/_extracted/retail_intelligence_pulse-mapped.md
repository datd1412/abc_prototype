# Bảng Ánh Xạ ERD: Retail Intelligence Pulse

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `orders`, `products`, `product_variants`, `inventory_batches`, `suppliers`.
- Đối chiếu:
  - `orders.totalAmount`, `orders.orderType`, `orders.status`
  - `products.name`, `products.categoryId`
  - `product_variants.skuCode`, `product_variants.currentStock`, `product_variants.reorderPoint`, `product_variants.sellingPrice`
  - `inventory_batches.batchNumber`, `inventory_batches.expiresAt`, `inventory_batches.quantity`
  - `suppliers.name`
- Loại bỏ theo Rule 3:
  - Không có OCR hay field ngoài ERD.

## 2. Component Contract
- Page Shell: Sidebar trái + Topbar (tên màn hình, role hiện tại) kèm `nav-owner.js`.
- 4 Pulse KPI Cards:
  - Doanh thu đa kênh (62.450.000 ₫)
  - Vận tốc bán trung bình (18.2 đơn/giờ)
  - Sức khỏe tồn kho (94.2% An toàn)
  - Tỷ lệ hoàn tất & SLA (97.9%)
- 3 Tri-part AI Action Cards:
  - Card 1: Khuyến nghị nhập thêm Son Merzy V6
  - Card 2: Xử lý lô cận date Serum Klairs B5
  - Card 3: Chiết khấu thanh toán sớm đơn hàng PO Klairs
- Bảng Ma trận SKU Velocity:
  - Cột: Sản phẩm, Kênh chủ lực, Tồn khả dụng, Tốc độ bán, Dự báo hết hàng, Trạng thái AI Pulse, Thao tác.
- Pagination Footer.

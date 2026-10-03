# Bảng Ánh Xạ ERD: Quản Lý Sản Phẩm, Biến Thể & Kho Lô Mỹ Phẩm

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `products`, `product_variants`, `inventory_batches`, `categories`.
- Đối chiếu:
  - `products.name`: Tên sản phẩm ("Serum Phục Hồi B5 Klairs", "Áo Blazer Linen Oversize",...)
  - `products.categoryId`: Danh mục phân loại
  - `product_variants.skuCode`: Mã định danh hàng hóa (`KLAIRS-B5-35`, `BLM-BLAZ-OV`, `PHYTO-SUN-50`,...)
  - `product_variants.costPrice`: Giá vốn
  - `product_variants.sellingPrice`: Giá niêm yết bán lẻ
  - `product_variants.currentStock`: Số lượng tồn kho khả dụng
  - `product_variants.reorderPoint`: Điểm đặt hàng lại (Low stock threshold)
  - `inventory_batches.batchNumber`: Mã lô date FEFO (`LOT-202405-A`, `LOT-202610-C`,...)
  - `inventory_batches.expiresAt`: Ngày hết hạn sử dụng
  - `inventory_batches.quantity`: Số lượng tồn của lô
  - `inventory_batches.status`: Trạng thái lô (`active`, `expired`, `recalled`)
- Loại bỏ theo Rule 3:
  - Bỏ mã vạch Barcode nếu không có trong ERD (dùng `skuCode` làm định danh chính xác).
  - Không có OCR hay field ngoài ERD.

## 2. Component Contract
- Page Shell: Sidebar trái + Topbar (tên màn hình, role hiện tại) kèm `nav-owner.js`.
- 4 KPI Cards:
  - Tổng danh mục hoạt động: 184 SKU (3.420 món)
  - Giá trị vốn lưu kho: 418.900.000 ₫ (+5.4%)
  - Lô cận date (< 60 ngày): 4 Lô hàng (32 hộp, rủi ro 8.5M ₫)
  - Chạm ngưỡng tái đặt: 3 SKU cháy hàng
- AI Insight Strip: Cảnh báo FEFO lô cận date của Serum Klairs và đề xuất Flash Sale giải phóng vốn.
- Filter Bar & Channel Tabs: Tất cả, Theo dõi Lô Date, Cận date / Cháy hàng.
- List View Table:
  - Cột: Sản phẩm, SKU, Biến thể, Giá bán & Vốn, Tồn kho, Lô & Hạn dùng (FEFO), Đánh giá AI, Thao tác.
- Pagination Footer.

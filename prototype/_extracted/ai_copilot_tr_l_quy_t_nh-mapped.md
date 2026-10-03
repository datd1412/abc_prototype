# BO: AI Copilot Trợ Lý Ra Quyết Định Kinh Doanh — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.totalAmount` / `orders.finalAmount` → Phân tích doanh số tuần 41 vs 42 (1.480 giao dịch)
- `orders.createdAt` → Dòng thời gian giao dịch
- `order_items.quantity` / `order_items.price` → Số lượng và đơn giá sản phẩm trong giao dịch bán
- `products.name` → Tên sản phẩm phân tích (Serum Bio-B5 Hydra Max, Kem Phục Hồi Ceramide...)
- `product_variants.sku` → Mã SKU (`MB-SER-B5-01`, `MB-CRM-02`)
- `product_variants.retailPrice` / `product_variants.costPrice` → Biên lợi nhuận sản phẩm
- `inventory.quantity` → Tồn kho thực tế (0 chai - đứt hàng)
- `inventory.lowStockThreshold` → Ngưỡng cảnh báo tồn thấp an toàn
- `purchase_orders.code` → Mã PO đặt hàng khẩn cấp
- `purchase_orders.totalAmount` → Tổng giá trị PO dự kiến (21.600.000 ₫)
- `suppliers.name` → Nhà cung cấp (Dược Mỹ Phẩm Minh Anh)
- `expenses.amount` / `expenses.category` → Chi phí marketing vận hành
- `users.fullName` → Người dùng ra lệnh (Chủ doanh nghiệp Nguyễn Thị Mai)

## Field LOẠI
- `chi nhánh Q.1`: Không có entity multi-branch trong ERD.
- `TikTok Ads / Facebook Ads Campaign`: Kênh quảng cáo bên ngoài, biểu diễn bằng danh mục chi phí marketing trong `expenses`.
- `Zalo ZNS / KiotViet`: Nền tảng bên thứ ba không có entity trong ERD.

## Field THIẾU - CẦN BỔ SUNG
- `purchase_orders.status`: Thể hiện trạng thái PO dự thảo (`draft`) khi nhấn "Tạo PO Đặt Hàng Ngay".
- `inventory.lowStockThreshold`: Hiển thị ngưỡng tồn tối thiểu để giải thích tại sao hệ thống phát hiện đứt hàng kịp thời.

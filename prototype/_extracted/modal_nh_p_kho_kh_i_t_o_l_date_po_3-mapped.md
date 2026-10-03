# Bảng Ánh Xạ ERD: Tạo Phiếu Nhập Kho & Khởi Tạo Lô Date PO 3 (In Mã Vạch Tem Lô)

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `inventory_receipts`, `inventory_receipt_items`, `inventory_batches`, `purchase_orders`, `products`.
- Đối chiếu:
  - `purchase_orders.poNumber`: `#PO-202610-088`
  - `inventory_receipts.receiptNumber`: Mã phiếu nhập kho tương ứng
  - `inventory_receipts.status`: Trạng thái tiếp nhận hàng
  - `inventory_receipt_items.productVariantId`, `inventory_receipt_items.receivedQty`
  - `inventory_batches.batchNumber`: `LOT-KLAIRS-202610-A`, `LOT-KLAIRS-202610-B`, `LOT-PHYTO-202610`
  - `inventory_batches.expiresAt`, `inventory_batches.quantity`
  - Barcode mã vạch lô / SKU: `products.skuCode` / `inventory_batches.batchNumber`
- Không có OCR hay field ngoài ERD.

## 2. Component Contract
- Form Panel / Modal view với backdrop hoặc container modal chuẩn Odoo.
- Header: PO reference + status badge.
- Bảng chi tiết dòng nhập kho: Sản phẩm, Đơn vị, SL Đặt, SL Nhập thực tế, Mã Lô Hạn Dùng, Hạn Sử Dụng (Exp Date), Mã Vạch Lô (Barcode Label), Vị trí lưu kho.
- Khối tổng kết & Action buttons: Hủy bỏ, Lưu nháp, In phiếu & Mã vạch, Xác nhận Nhập kho & Khởi tạo Lô.

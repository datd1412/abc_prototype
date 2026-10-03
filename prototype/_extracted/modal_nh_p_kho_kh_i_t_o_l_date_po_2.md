# Trích xuất Nội dung: Tạo Phiếu Nhập Kho & Khởi Tạo Lô Date PO 2 (Tách Nhiều Lô Date)
**Nguồn**: `stitch_ai_business_copilot_platform/modal_nh_p_kho_kh_i_t_o_l_date_po_2/`

## 1. Tiêu đề & Ngữ cảnh
- Tiêu đề: "Tạo Phiếu Nhập Kho & Quản Lý Lô Hạn Dùng (PO) — Tính Năng Tách Đa Lô (Multi-lot Split)"
- Mã phiếu PO: `#PO-202610-088`
- Trạng thái: Kiểm hàng thực tế & Chia tách lô date

## 2. Chi tiết Nghiệp vụ Tách Lô (Multi-lot Split)
- **SKU 1: Serum Klairs Midnight Blue Calming 30ml** (Tổng nhập: 120 chai)
  - Thùng hàng NCC giao thực tế có 2 hạn sử dụng khác nhau:
    - **Lô 1 con**: `LOT-KLAIRS-202610-A` • NSX: 15/09/2026 • HSD: 15/09/2029 • SL: 80 chai.
    - **Lô 2 con**: `LOT-KLAIRS-202610-B` • NSX: 20/10/2026 • HSD: 20/10/2029 • SL: 40 chai.
  - Nút thao tác: `+ Tách thêm Lô Date cho sản phẩm này`

- **SKU 2: Kem Dưỡng Phyto Calming Cream 50ml** (Tổng nhập: 80 hộp)
  - Lô duy nhất: `LOT-PHYTO-202610` • HSD: 01/10/2029 • SL: 80 hộp.

## 3. Tổng kết & Thao tác
- Tổng số lượng nhập kho: 200 món (3 mã lô ghi nhận)
- Tổng tiền nhập: 40.800.000 ₫
- Actions footer: "Hủy", "Lưu bản nháp", "In phiếu PO", "Xác nhận Nhập kho & Khởi tạo Lô (FEFO)".

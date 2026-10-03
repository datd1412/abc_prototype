# Trích xuất Nội dung: Thêm Nhân Viên Mới & Gán Phân Quyền RBAC
**Nguồn**: `stitch_ai_business_copilot_platform/modal_th_m_nh_n_vi_n_m_i_g_n_ph_n_quy_n_rbac/`

## 1. Tiêu đề & Mục đích
- Tiêu đề: "Thêm Nhân Viên Mới & Thiết Lập Quyền Hạn"
- Mô tả: Khởi tạo tài khoản thành viên doanh nghiệp, cấp quyền truy cập theo vai trò chuẩn RBAC.
- Phiên bản RBAC: RBAC v2.4

## 2. Các khối thông tin
### Phần 1: Thông tin cá nhân & Tài khoản
- Họ và tên nhân viên (`fullName`): ví dụ "Nguyễn Hoàng Long"
- Mã nhân viên / định danh: `NV-024`
- Email đăng nhập công vụ (`email`): `long.nguyen@maisondebloom.vn`
- Số điện thoại liên hệ / OTP: `0987 654 321`
- Ngày bắt đầu công tác: `01/11/2024`
*(Lưu ý: "Địa điểm làm việc / Chi nhánh" trong Stitch bị loại bỏ theo Rule 3 vì ERD không có entity chi nhánh)*

### Phần 2: Chọn vai trò định danh (System / Business Role)
1. **Thu ngân & Bán hàng POS** (`role = 'cashier'`):
   - Tạo đơn, quét mã VietQR động, voucher bán lẻ, kiểm tồn quầy (14 chức năng).
2. **Quản lý Kho & Nhập xuất** (`role = 'warehouse_staff'` / `'inventory_manager'`):
   - Tạo PO nhập hàng, quản lý date lô mỹ phẩm FEFO, kiểm kê hao hụt (22 chức năng).
3. **Kế toán & Dòng tiền** (`role = 'accountant'`):
   - Sổ quỹ thu chi, đối soát công nợ NCC, hạch toán chi phí (30 chức năng).
4. **Vận hành TMĐT (E-com Omnichannel)** (`role = 'staff'`):
   - Đồng bộ Shopee, TikTok Shop, in vận đơn, xử lý đơn hoàn & đổi trả (18 chức năng).
5. **Quyền hạn Tùy Chỉnh (Custom RBAC)**:
   - Dành cho Trưởng ca, granular permissions theo module.

### Phần 3: Cấu hình an ninh dữ liệu & permissions
- Mặt nạ dữ liệu khách hàng (Masking VIP): Ẩn 4 số giữa SĐT khách hàng
- Ẩn Giá Vốn Hàng Bán (COGS & Import Price)
- Giới hạn quyền xem Báo cáo Lãi/Lỗ Tổng hợp (P&L)
- Hạn mức chiết khấu tối đa khi thanh toán (vd: 10% / hóa đơn, vượt mức cần phê duyệt)
- Xác thực 2FA / bảo mật đăng nhập

## 3. Thao tác hành động
- "Hủy bỏ"
- "Lưu bản nháp"
- "Tạo Tài Khoản & Gửi Thư Mời"

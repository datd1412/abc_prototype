# Bảng Ánh Xạ ERD: Thêm Nhân Viên Mới & Thiết Lập Quyền Hạn RBAC

## 1. Nguồn & Đối Chiếu ERD
- Entity chính: `users`, `business_members`, `businesses`.
- Đối chiếu:
  - `users.fullName`: Tên nhân viên
  - `users.email`: Email tài khoản công vụ
  - `users.status`: Trạng thái hoạt động (`active` / `invited` / `pending`)
  - `business_members.businessId`: Doanh nghiệp chủ quản
  - `business_members.userId`: ID người dùng
  - `business_members.role`: Vai trò thành viên (`owner`, `manager`, `cashier`, `warehouse`, `accountant`, `staff`)
  - `business_members.permissions`: JSON cấu hình quyền truy cập chi tiết (granular permissions: maskCustomerPhone, hideCostPrice, allowPnLReport, maxDiscountRate, require2FA)
  - `business_members.status`: Trạng thái thành viên trong doanh nghiệp
- Loại bỏ theo Rule 3:
  - Khái niệm "Chi nhánh làm việc" / "Showroom Quận 1" / "Kho Tân Bình làm chi nhánh": Đã loại bỏ vì ERD SEP490 không có entity/field chi nhánh (chỉ quản lý đa doanh nghiệp `businesses` và kho `warehouses`).
  - Ghi nhận trong `prototype/_notes/removed-fields.md`.

## 2. Component Contract
- Form Panel / Modal view tương ứng với desktop admin panel.
- Header: Breadcrumb / Title "Thêm Nhân Viên Mới & Thiết Lập Quyền Hạn" + Badge "RBAC v2.4".
- Section 1: Thông tin cá nhân & Tài khoản (Họ tên, Mã NV, SĐT, Email công vụ, Ngày bắt đầu).
- Section 2: Chọn vai trò định danh (Radio Cards: Thu ngân POS, Quản lý Kho, Kế toán, Vận hành TMĐT, Quyền Tùy chỉnh).
- Section 3: Cấu hình an ninh dữ liệu & Quyền hạn nhạy cảm (Toggles: Mặt nạ dữ liệu khách hàng, Ẩn Giá Vốn COGS, Khóa Báo cáo Lãi Lỗ P&L, Hạn mức chiết khấu tối đa, Bảo mật 2FA).
- Footer Actions: Hủy bỏ, Lưu nháp, Tạo Tài Khoản & Gửi Thư Mời.

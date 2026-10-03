# Ánh xạ ERD: Quản lý Nhân viên & Ma trận Phân quyền (RBAC)
**File nguồn UI**: `stitch_ai_business_copilot_platform/c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n/`
**File đích**: `prototype/screens/bo-quan-ly-nhan-vien.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Họ tên nhân viên | `users` | `name` | Có | Tên cán bộ nhân viên |
| Email đăng nhập | `users` | `email` | Có | Định danh tài khoản |
| Mã nhân viên (NV-xxx) | `users` | `id` | Có | Định danh nội bộ |
| Vai trò hệ thống | `users` / `roles` | `role` / `roleName` | Có | Owner, Accountant, Cashier, Warehouse Manager... |
| Trạng thái tài khoản | `users` | `status` | Có | ACTIVE, INACTIVE, LOCKED |
| Quyền thao tác | `permissions` / `role_permissions` | `permissionCode`, `description` | Có | Ma trận RBAC |
| Ngày tạo / Cập nhật | `users` | `createdAt`, `updatedAt` | Có | ERD có |
| Lịch sử hành động audit | `audit_logs` | `action`, `entityName`, `userId`, `createdAt` | Có | ERD có entity audit_logs |

## 2. Xử lý field không có trong ERD
- Stitch có nhắc tới "Chi nhánh" -> ERD không có entity Branch/Chi nhánh. Chúng ta chuyển đổi thành "Phạm vi phụ trách / Kho làm việc" (VD: Kho Tổng Logistics, Quầy POS bán lẻ, Bộ phận Tài chính).
- Giữ nguyên các trường xác thực 2FA, ma trận quyền và phân nhóm chức năng để đáp ứng quản trị RBAC chuẩn doanh nghiệp.

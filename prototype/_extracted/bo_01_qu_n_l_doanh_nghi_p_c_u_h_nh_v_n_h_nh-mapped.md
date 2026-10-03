# BO-01: Quản lý Doanh nghiệp & Cấu hình Vận hành — đã đối chiếu ERD/FR & Content Density

Nguồn: `abc-prototype/prototype/_extracted/bo_01_qu_n_l_doanh_nghi_p_c_u_h_nh_v_n_h_nh.md`

## 1. Field GIỮ (Phân loại theo Content Density Rule)

### Primary Fields (Thông tin chính hiển thị trên Form Panel / Section chính):
- `businesses.name` → Tên doanh nghiệp
- `businesses.businessType` → Loại hình doanh nghiệp
- `businesses.taxCode` → Mã số thuế
- `businesses.currency` → Đơn vị tiền tệ
- `businesses.status` → Trạng thái doanh nghiệp
- `business_settings.timezone` → Múi giờ hệ thống
- `business_settings.lowStockDefault` → Ngưỡng tồn kho mặc định
- `business_settings.lowStockAlert` → Cảnh báo tồn kho thấp
- `business_settings.aiEnabled` → Trạng thái kích hoạt AI Copilot

### Secondary Fields (Hiển thị chi tiết khi mở modal/drawer phân quyền nhân sự):
- `users.fullName` → Họ và tên nhân viên
- `users.email` → Email đăng nhập
- `users.avatarUrl` → Ảnh đại diện
- `users.systemRole` → Vai trò hệ thống
- `users.status` → Trạng thái tài khoản
- `business_members.role` → Vai trò trong doanh nghiệp
- `business_members.permissions` → Quyền hạn RBAC (JSON/Text)
- `business_settings.settings` → Cấu hình nâng cao (JSON)

---

## 2. Field LOẠI
- `Chi nhánh cửa hàng`: LOẠI — Không có entity/field chi nhánh cửa hàng trong ERD `SEP490_entities_fields.txt` (chỉ quản lý cấp `businessId`).
- `Zalo ZNS Official / Telegram Push Bot`: LOẠI — Không có field tương ứng trong ERD `business_settings`.

---

## 3. Navigation Placement
- Vị trí IA: Menu **Quản lý** ▾ → Item: **Cấu hình hệ thống** (Portal Business Owner: `bo-quan-ly-doanh-nghiep`).

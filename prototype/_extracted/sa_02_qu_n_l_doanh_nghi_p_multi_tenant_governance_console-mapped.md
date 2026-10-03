# SA-02 Trung Tâm Quản Trị Khách Thuê & Doanh Nghiệp — đã đối chiếu ERD/FR

## Field GIỮ
- `businesses.id` → Mã doanh nghiệp / Tenant ID (TNT-88301)
- `businesses.name` → Tên doanh nghiệp (Maison de Bloom)
- `businesses.businessType` → Gói dịch vụ / Loại doanh nghiệp (Enterprise Pro)
- `businesses.taxCode` → Mã số thuế (0317829102)
- `businesses.status` → Trạng thái hoạt động (Active / Suspended / Terminated)
- `businesses.createdAt` → Ngày đăng ký khởi tạo
- `users.fullName` → Đại diện pháp luật / Chủ doanh nghiệp
- `users.email` → Email liên hệ quản trị

## Field LOẠI
- Mã hóa mật khẩu trực tiếp bằng khóa riêng của Admin (vi phạm Zero-Trust SECURITY rules)

## Field THIẾU - CẦN BỔ SUNG
- `businesses.currency`: Đơn vị tiền tệ hạch toán mặc định của doanh nghiệp (VND)
- `businesses.status`: Cập nhật trạng thái rõ ràng giữa Active, Suspended, Inactive

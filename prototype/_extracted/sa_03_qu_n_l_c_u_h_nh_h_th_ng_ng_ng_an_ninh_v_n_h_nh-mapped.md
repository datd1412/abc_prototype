# SA-03 Cấu Hình Hệ Thống & An Ninh Vận Hành — đã đối chiếu ERD/FR

## Field GIỮ
- `business_settings.timezone` → Múi giờ hệ thống (Asia/Ho_Chi_Minh)
- `business_settings.lowStockDefault` → Ngưỡng cảnh báo tồn kho toàn cục
- `business_settings.settings` → Cấu hình an ninh & Rate Limiting dạng JSON (Rate limits, Session timeout, 2FA Policy)
- `audit_logs.action` → Thao tác cấu hình an ninh (Commit Config, Change Rate Limit, Update Security Level)
- `audit_logs.metadata` → Mã băm SHA-256 & thông tin người phê duyệt kép
- `users.systemRole` → Quyền hạn quản trị an ninh hệ thống

## Field LOẠI
- Tự chế phương thức mã hóa không đúng tiêu chuẩn Zero-Trust FR

## Field THIẾU - CẦN BỔ SUNG
- `audit_logs.metadata`: Lưu vết mã băm SHA-256 của mỗi phiên Commit cấu hình an ninh
- `business_settings.settings`: Tham số cài đặt Rate Limiting API dùng chung

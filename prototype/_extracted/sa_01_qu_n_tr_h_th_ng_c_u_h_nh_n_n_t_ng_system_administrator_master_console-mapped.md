# SA-01 Cấu Hình Hệ Thống Toàn Cục — đã đối chiếu ERD/FR

## Field GIỮ
- `business_settings.timezone` → Múi giờ hệ thống (Asia/Ho_Chi_Minh)
- `business_settings.lowStockDefault` → Mức tồn kho tối thiểu mặc định hệ thống
- `business_settings.lowStockAlert` → Kích hoạt cảnh báo tồn kho tự động
- `business_settings.aiEnabled` → Bật/tắt dịch vụ AI Copilot & Gateway toàn cục
- `business_settings.settings` → Cấu hình lưu trữ dạng JSON (Redis Stream, VietQR Webhook, Session Timeout)
- `users.systemRole` → Vai trò quản trị hệ thống (System Administrator - Root)
- `audit_logs.action` → Thao tác cấu hình hệ thống (Hot Reload, Update Flags, Maintenance Mode)

## Field LOẠI
- Can thiệp thay đổi cấu trúc phần cứng server vật lý trực tiếp (ngoài scope phần mềm FR)

## Field THIẾU - CẦN BỔ SUNG
- `business_settings.aiEnabled`: Cờ bật tắt AI Gateway toàn hệ thống
- `business_settings.lowStockDefault`: Mức ngưỡng mặc định cho toàn bộ doanh nghiệp mới khởi tạo

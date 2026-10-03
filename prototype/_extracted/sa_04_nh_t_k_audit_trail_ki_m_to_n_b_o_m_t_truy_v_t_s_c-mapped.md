# SA-04 Nhật Ký Audit Trail & Kiểm Toán Hệ Thống — đã đối chiếu ERD/FR

## Field GIỮ
- `audit_logs.id` → Mã nhật ký kiểm toán / Event ID (`TRACE-SEC-2024-8849`)
- `audit_logs.userId` → ID người thực hiện (Actor ID)
- `audit_logs.businessId` → ID doanh nghiệp tác động (Tenant ID)
- `audit_logs.action` → Hành động thao tác (Break-Glass Access, Config Update, Role Change)
- `audit_logs.entityType` → Loại đối tượng bị tác động (User, Business, SystemConfig)
- `audit_logs.entityId` → ID đối tượng bị tác động
- `audit_logs.oldData` → Dữ liệu trước thay đổi (JSON snapshot)
- `audit_logs.newData` → Dữ liệu sau thay đổi (JSON snapshot)
- `audit_logs.metadata` → Thông tin bổ sung (IP address HCM, SHA-256 Hash Digest, Severity Level)
- `audit_logs.createdAt` → Thời điểm thực hiện (NTP synchronized timestamp)
- `users.fullName` → Tên người thực hiện (Trần Hoàng Long)
- `users.email` → Email người thực hiện

## Field LOẠI
- Xóa nhật ký kiểm toán khỏi database (vi phạm nguyên tắc WORM Append-Only bất biến)

## Field THIẾU - CẦN BỔ SUNG
- `audit_logs.oldData` & `newData`: Dữ liệu diff chi tiết trước và sau khi chỉnh sửa
- `audit_logs.metadata`: Lưu vết IP nguồn và mã băm SHA-256 Merkle Tree

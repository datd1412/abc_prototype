# Ánh xạ ERD: Trung Tâm Điều Hành Nền Tảng (System Administrator Master Console)
**File nguồn UI**: `stitch_ai_business_copilot_platform/c_ng_qu_n_tr_h_th_ng_to_n_n_ng_system_administrator_sa_console/`
**File đích**: `prototype/screens/sa-master-console.html`
**Trọng tài**: `erd/SEP490_entities_fields.txt`

## 1. Bảng đối chiếu Field UI vs ERD

| Field trên UI | Entity ERD | Field ERD | Hợp lệ? | Ghi chú |
|---|---|---|:---:|---|
| Tên Doanh nghiệp / Tenant | `tenants` (hoặc `companies`) | `name`, `code`, `status`, `createdAt` | Có | Maison de Bloom, FreshMart... |
| Chủ doanh nghiệp | `users` | `name`, `email`, `role` | Có | Đại diện pháp lý tenant |
| Gói cước / Subscription | `subscriptions` | `planName`, `status`, `expiresAt` | Có | Starter, Growth, Enterprise AI Pro |
| Cấu hình tham số AI / Model | `system_configs` | `configKey`, `configValue`, `description` | Có | Cấu hình LLM, Prompt version |
| Audit Trail / Truy vết | `audit_logs` | `action`, `entityName`, `userId`, `createdAt` | Có | Nhật ký kiểm toán bất biến |
| Tải hệ thống / SLA Uptime | Computed / System Metrics | N/A | Có | Metrics hiển thị tầng DevOps nền tảng |

## 2. Xử lý field
- Giữ nguyên các thông số kiến trúc nền tảng chuẩn SaaS Multi-tenant.
- Các module con liên kết trực tiếp tới các màn quản trị chuyên sâu đã build: `sa-cau-hinh-he-thong.html`, `sa-quan-ly-doanh-nghiep.html`, `sa-an-ninh-he-thong.html`, `sa-audit-log.html`.

# SA-02 Trung Tâm Quản Trị Khách Thuê & Doanh Nghiệp (Multi-Tenant Governance Console)
Nguồn: stitch_ai_business_copilot_platform/sa_02_qu_n_l_doanh_nghi_p_multi_tenant_governance_console/code.html

## Field đang hiển thị
- Tổng Doanh Nghiệp (Tenants): 48 Doanh nghiệp (42 Đang hoạt động, 4 Tạm ngưng, 2 Đang onboarding)
- Trạng Thái Hạ Tầng: 100% Schema Isolated (KMS Sharded, khóa mã hóa Envelope KMS)
- Yêu Cầu Hỗ Trợ Vận Hành: 04 Sự cố chờ SA
- Giám Sát Can Thiệp Dữ Liệu: 100% Audit Guard (SHA-256)
- Danh sách Doanh nghiệp (Tenants Table):
  - Tên doanh nghiệp & Tenant ID (Maison de Bloom - TNT-88301)
  - Mã số thuế (MST) & Đại diện pháp luật
  - Gói dịch vụ & Chu kỳ thanh toán (Enterprise Pro, Hạn đến 12/2025)
  - Vùng hạ tầng & Database Schema (`tenant_maison_bloom_prod`, Region HCMC-02)
  - Trạng thái hoạt động (🟢 Đang hoạt động / 🟡 Tạm ngưng / 🔴 Khóa khẩn cấp)
  - Số tài khoản người dùng & Số điểm bán (POS/Franchise)
  - Dung lượng lưu trữ & Token AI đã dùng

## Action/Button
- Cấu Hình Database Sharding
- Xuất Báo Cáo Tuân Thủ SOC2
- + Onboard Doanh Nghiệp Mới
- Mở phiên Break-Glass Session (Xử lý sự cố theo Ticket)
- Khóa khẩn cấp / Tạm ngưng doanh nghiệp
- Cấu hình hạn mức (Quota AI & Storage)

## Ghi chú UX
- Zero-Trust Separation of Duties Banner (Quy tắc cấm can thiệp ngầm dữ liệu khách hàng)
- Filter theo Gói dịch vụ, Trạng thái, Region
- Bảng danh sách Multi-Tenant đi kèm chi tiết Schema & Tình trạng vận hành

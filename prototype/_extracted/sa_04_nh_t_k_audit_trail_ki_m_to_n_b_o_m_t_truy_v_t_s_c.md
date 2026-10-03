# SA-04 Nhật Ký Audit Trail & Kiểm Toán Hệ Thống (Audit Trail & Security Forensics)
Nguồn: stitch_ai_business_copilot_platform/sa_04_nh_t_k_audit_trail_ki_m_to_n_b_o_m_t_truy_v_t_s_c/code.html

## Field đang hiển thị
- Tổng bản ghi (24 Giờ): 18.420 bản ghi (+14.2%, 100% Append-Only)
- Cảnh Báo High / Critical: 03 sự cố cần rà soát (1 Break-Glass, 1 Escalation, 1 PII Export)
- Toàn Vẹn Chuỗi Hash (Chain): 100% Khớp khối (SHA-256 Merkle Tree `f82a...94d1`)
- Kho Lưu Trữ WORM Vault: 14.8 GB (Bảo lưu pháp lý 7 năm)
- Bảng nhật ký kiểm toán (Audit Trail Table):
  - Mã vết (Trace ID & Event ID): `TRACE-SEC-2024-8849`
  - Thời gian (NTP Synchronized Timestamp): `24/10/2024 14:32:05.184`
  - Người thực hiện (Actor ID & User): Trần Hoàng Long (sa-root-01)
  - IP Nguồn & Vị trí (IP Source & Location): `113.161.44.18 (HCM, VN)`
  - Nhóm sự kiện (Event Category): IAM & RBAC / Config / Break-Glass / AI Guardrails
  - Đối tượng tác động (Target Entity & Resource): `Tenant #TK-902 (Sakura Beauty)`
  - Mức độ nghiêm trọng (Severity Level): INFO / LOW / MEDIUM / HIGH / CRITICAL
  - Mã băm toàn vẹn (SHA-256 Hash Digest): `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

## Action/Button
- Xác minh chuỗi Hash (Merkle Tree Chain Verification)
- Truy vết sự cố Forensics
- Xuất Báo Cáo Audit (CSV/JSON/PDF)
- Session Replay (Ghi âm/Phát lại phiên Break-Glass)
- Ngắt phiên lập tức (Emergency Session Kill)

## Ghi chú UX
- SOC 2 Type II & WORM Vault Live Indicators
- Real-time Forensic Alert Ribbon (Break-Glass Warning)
- Filter Matrix nâng cao (Search Actor/Trace ID, Date Range, Category, Severity)

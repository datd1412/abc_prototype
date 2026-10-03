# SA-03 Cấu Hình Hệ Thống, Ngưỡng Cảnh Báo & An Ninh Vận Hành (System Administrator Security & Governance Console)
Nguồn: stitch_ai_business_copilot_platform/sa_03_qu_n_l_c_u_h_nh_h_th_ng_ng_ng_an_ninh_v_n_h_nh/code.html

## Field đang hiển thị
- Tổng Tham Số Toàn Cục: 64 Tham Số (58 Khóa, 6 Động Hot-Reload)
- Ngưỡng Bảo Vệ & An Toàn: 18 Quy Tắc Kích Hoạt (Chặn DDoS/Spam Rate Limiting)
- Bảo Mật & Zero-Trust: L4 Enterprise Grade (mTLS Bắt buộc, 2FA FIDO2 Enforced)
- Thay Đổi Chờ Duyệt: 02 Staged Commits (Yêu cầu chữ ký kép SA + SecOps)
- Các nhóm cấu hình & tham số an ninh:
  - Cấu Hình Dùng Chung (Múi giờ Asia/Ho_Chi_Minh, Ngôn ngữ mặc định vi-VN, Tiền tệ VND)
  - Ngưỡng & Giới Hạn (Rate Limit Login 5 lần/phút, Rate Limit API 100 req/s, Max File Upload 25MB)
  - Vận Hành & Bảo Mật (Session Timeout 30 phút, Khóa tài khoản sau 5 lần sai pass, Bắt buộc 2FA TOTP/FIDO2)
  - Tích Hợp & API Quotas (TikTok Shop Webhook Retry 3 lần, VietQR Napas Timeout 10s)

## Action/Button
- Xuất Bản Snapshot (JSON)
- Xem Lịch Sử Phiên Bản v4.8
- Thêm Tham Số Mới
- Phê Duyệt Ký Kép Commit (SA + SecOps)
- Lưu & Hot-Reload Cấu Hình

## Ghi chú UX
- Global Config Change Governance Banner (Cơ chế Ký Duyệt Kép & Diff SHA-256)
- Tab navigation theo 4 nhóm cấu hình
- Bảng tham số với chỉ báo Status (Lock / Hot-Reload)

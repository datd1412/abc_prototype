# SA-01 Cấu Hình Hệ Thống Toàn Cục (System Administrator Master Console)
Nguồn: stitch_ai_business_copilot_platform/sa_01_qu_n_tr_h_th_ng_c_u_h_nh_n_n_t_ng_system_administrator_master_console/code.html

## Field đang hiển thị
- Cụm Microservices: 24/24 (100% Khả Dụng, CPU Node Cluster 32%)
- Tần Suất Sao Lưu Tự Động: Mỗi 30 phút (RPO 5m, Kích thước bản lưu 1.42 GB)
- Chính Sách Bảo Mật: Cấp Enterprise (2FA/TOTP, Session Idle Timeout 30 phút)
- AI Gateway Quota (24h): 1.45M / 5.0M Tokens (Latency 38ms)
- Cờ tính năng hệ thống (Feature Flags):
  - Đồng bộ tồn kho thời gian thực (Redis Stream)
  - Trợ lý AI Phân tích Đơn hàng & Dự báo Cầu (Copilot v2.4)
  - Cổng VietQR Pro Napas 247 Dynamic & Webhook
  - Chế độ bảo trì hệ thống toàn cục

## Action/Button
- Toggle Chế độ bảo trì hệ thống (Maintenance Mode)
- Xuất JSON Cấu Hình
- Phục Hồi Snapshot
- Hot Reload Cấu Hình
- Lưu & Áp Dụng Cấu Hình Toàn Hệ Thống

## Ghi chú UX
- Chuyển đổi môi trường: PROD / STG / SANDBOX
- Layout dành riêng cho System Admin portal (`sa-`)
- Bảng điều khiển Master Feature Flags & Tần suất sao lưu

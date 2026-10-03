# AI Business Advisor - Cố Vấn Chiến Lược Doanh Nghiệp — đã đối chiếu ERD/FR

## Field GIỮ
- `ai_conversations.title` → Tiêu đề phiên tham vấn chiến lược (Hồ Sơ Quyết Sách C-Level)
- `ai_conversations.status` → Trạng thái phiên tham vấn (Đang hoạt động)
- `ai_messages.role` → Vai trò gửi tin (AI Copilot / C-Level Executive)
- `ai_messages.content` → Nội dung tham vấn & phân tích chiến lược
- `ai_messages.metadata` → Bằng chứng tổng hợp từ BO-01 → BO-10
- `ai_insights.recommendation` → Khuyến nghị điều hành từ AI
- `ai_insights.confidence` → Độ tin cậy tổng hợp (96.4%)
- `ai_tool_executions.toolName` → Công cụ AI đã thực thi (Prophet, Monte Carlo, FEFO Watcher)

## Field LOẠI
- Tự động thay đổi tài khoản ngân hàng chủ doanh nghiệp mà không cần xác thực OTP (ngoài scope FR)

## Field THIẾU - CẦN BỔ SUNG
- `ai_messages.metadata`: Chứa liên kết bằng chứng minh bạch (explainability) trỏ tới các bảng nghiệp vụ gốc
- `ai_conversations.updatedAt`: Thời điểm cập nhật khuyến nghị gần nhất

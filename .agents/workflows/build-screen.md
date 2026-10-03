---
description: 
---

# Workflow: /build-screen <ten_file_mapped>

## Input
- `abc-prototype/prototype/_extracted/<ten_file>-mapped.md` (kết quả của /map-erd)
- `abc-prototype/prototype/tokens.css`
- `.agents/rules/design-system.md` (component contract)
- Tham chiếu bố cục (nếu cần): chỉ trong whitelist addon của `.agents/rules/source-boundaries.md`

## Bước 0 — Tự kiểm tra whitelist có đủ không (BẮT BUỘC, làm trước khi build)

Với entity/tính năng chính của màn hình đang build, chạy:

```bash
grep -ril "<tu_khoa_entity>" odoo-20.0/addons/{<danh_sach_whitelist>}/views/
```

- **Có kết quả** → dùng file match được làm tham chiếu bố cục, sang Bước 1.
- **Không có kết quả** → phân loại:
  - Entity là bảng nghiệp vụ CRUD thông thường (có trong nhóm 01–17, 25, 26 của
    ERD: users, products, orders, expenses, suppliers, customers...) → DỪNG LẠI,
    báo cáo: "grep không tìm thấy pattern cho <entity> trong whitelist hiện tại,
    đề xuất thêm addon <tên>" — KHÔNG tự ý mở rộng, chờ duyệt.
  - Entity là lõi AI (`ai_conversations`, `ai_messages`, `ai_tool_executions`,
    `ai_insights`, `simulations`, `simulation_results`, `forecast_runs`,
    `forecast_results`) → KHÔNG xin thêm addon (Odoo không có pattern tương
    đương), chuyển thẳng sang "Quy trình khi CẦN khuôn mới" trong
    `.agents/rules/design-system.md`.

## Bước 1 — Build
1. Chỉ dùng field trong mục "Field GIỮ" và "Field THIẾU - CẦN BỔ SUNG" của file mapped.
   KHÔNG đưa lại field ở mục "Field LOẠI" vào UI dù có tiện layout hơn.
2. Chọn khuôn phù hợp trong Component Contract (List View / Form Panel / KPI Card...).
3. Viết HTML, link `tokens.css`, dùng đúng class/token đã có.

## Output
`abc-prototype/prototype/screens/<ten-man-hinh>.html`

## Trước khi báo hoàn thành — chạy checklist DoD (AGENTS.md mục 6)
- [ ] Đã chạy Bước 0 (grep) trước khi build, không bỏ qua
- [ ] Chỉ dùng token trong tokens.css
- [ ] Đúng khuôn Component Contract (hoặc đã xin mở rộng đúng quy trình)
- [ ] Mọi field hiển thị nằm trong mục "Field GIỮ"/"THIẾU-BỔ SUNG" của file mapped
- [ ] Không còn dấu vết layout mobile/bottom-nav từ Stitch gốc
- [ ] Đã cập nhật `field-labels.md` nếu có field/label mới xuất hiện lần đầu
- [ ] Nếu màn có AI Insight Strip: đúng format 1 dòng, có link sang bo-ai-phan-tich,
      không phải hero card, nội dung có dữ liệu cụ thể (không mơ hồ)
- [ ] Nếu màn KHÔNG có insight thật: không hiện khối này (không placeholder rỗng)
- [ ] Sau khi 1 màn qua checklist, tick ☑ đúng dòng slug đó trong prototype/_notes/screen-inventory.md


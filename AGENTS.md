# AGENTS.md — ABC Prototype Build Rules

Quy tắc này LUÔN được nạp trước mọi task. Không được bỏ qua hay tự diễn giải khác.

## 1. Ranh giới nguồn (source boundaries) — BẮT BUỘC

| Thư mục | Quyền | Vai trò |
|---|---|---|
| `stitch_ai_business_copilot_platform/` | **READ-ONLY** | Chỉ lấy NỘI DUNG: label tiếng Việt, field đang hiển thị, action/button. KHÔNG lấy layout, màu, CSS, bottom-nav mobile của nó. |
| `odoo-20.0/` | **READ-ONLY**, chỉ trong `addons/product`, `addons/stock`, `addons/sale`, `addons/purchase`, `addons/hr_expense`, `addons/account` | Nguồn BỐ CỤC desktop: cấu trúc list view (search/filter → tree → pagination), form view (breadcrumb → notebook/tabs → statusbar). Không đọc các addons khác (mrp, website, hr, l10n_*...) trừ khi được yêu cầu rõ. |
| `erd/SEP490_entities_fields.txt` | READ-ONLY | TRỌNG TÀI DUY NHẤT cho field hợp lệ. |
| `prototype/` | **READ-WRITE** | Nơi DUY NHẤT được tạo/sửa file output. |

Cấm tuyệt đối: sửa bất kỳ file nào trong `stitch_ai_business_copilot_platform/` hoặc `odoo-20.0/`.

## 2. Nền tảng mục tiêu

**Desktop admin panel.** Không dùng bottom navigation, không tối ưu mobile-first.
Page Shell = Sidebar trái (menu module) + Topbar (tên màn hình, user/role hiện tại).

## 3. Nguyên tắc dữ liệu (data contract)

1. Trước khi đưa BẤT KỲ field nào lên UI, kiểm tra field đó có tồn tại trong
   `erd/SEP490_entities_fields.txt` không.
2. Field có trong Stitch nhưng KHÔNG có trong ERD → **loại bỏ ngay, không hỏi lại,
   không tự thêm vào ERD.** (Ví dụ đã phát hiện: OCR hóa đơn, khái niệm "chi nhánh",
   nhà cung cấp gắn trực tiếp vào expense — đều không có entity/field tương ứng.)
3. Field có trong ERD nhưng Stitch không vẽ (ví dụ `lowStockThreshold`,
   `inventory_batches.expiresAt`) → PHẢI bổ sung vào UI, không được bỏ qua chỉ vì
   Stitch không có.
4. Không tự đặt tên field khác với tên trong ERD (giữ nguyên camelCase gốc khi
   map sang thuộc tính hiển thị).

## 4. Design tokens (bắt buộc dùng, không tự chế giá trị khác)

```css
:root {
  --color-bg: #f6f7f9;
  --color-surface: #ffffff;
  --color-border: #e3e6ea;
  --color-text: #1f2430;
  --color-text-muted: #6b7280;
  --color-primary: #2b59c3;
  --color-success: #1f9d55;
  --color-warning: #b8860b;
  --color-danger: #d64545;
  --space-1: 4px; --space-2: 8px; --space-3: 16px; --space-4: 24px; --space-5: 32px;
  --radius: 6px;
  --shadow-card: 0 1px 2px rgba(0,0,0,0.06);
  --font-base: 14px; --font-title: 20px;
  --font-family: "Inter", "Segoe UI", system-ui, sans-serif;
}
```
File thật: `prototype/tokens.css` — mọi màn hình `<link>` tới file này, không copy giá trị vào từng file riêng.

## 5. Component contract (khuôn bắt buộc)

- **Page Shell**: sidebar + topbar, dùng chung cho mọi màn.
- **List View**: filter bar → table → pagination (tham chiếu cấu trúc tree view của Odoo trong addons tương ứng).
- **Form Panel**: breadcrumb → section theo nhóm field → nút Save/Cancel cố định cuối.
- **KPI Card**: label nhỏ trên, số liệu lớn giữa, chỉ báo tăng/giảm dưới.
- **Status Badge**: chỉ dùng 3 màu trạng thái ở mục 4, không tự phối màu riêng.

Không tự nghĩ layout khác ngoài các khuôn này. Nếu 1 màn hình không khớp khuôn nào có sẵn (vd AI Advisor chat, Simulation) → dừng lại, báo cáo, không tự chế mà không hỏi.

## 6. Checklist Definition of Done (mỗi màn hình)

- [ ] Chỉ dùng token trong `prototype/tokens.css`
- [ ] Đúng khuôn Component Contract tương ứng
- [ ] Mọi field hiển thị đều có trong `erd/SEP490_entities_fields.txt`
- [ ] Không còn dấu vết bottom-nav/mobile layout từ Stitch gốc
- [ ] File nằm đúng trong `prototype/`, không sửa 2 folder read-only

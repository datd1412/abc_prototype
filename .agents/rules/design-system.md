---
trigger: always_on
---

# Rule: Design System

## Nguồn sự thật duy nhất
`abc-prototype/prototype/tokens.css` — mọi màn hình `<link rel="stylesheet" href="../tokens.css">`
tới file NÀY. Cấm copy giá trị màu/spacing thành số cứng vào file HTML riêng.
Nếu `tokens.css` chưa tồn tại, tạo trước với nội dung:

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

## Nền tảng mục tiêu
Desktop admin panel. KHÔNG bottom-navigation, KHÔNG mobile-first.

## Component Contract hiện có (khuôn đóng — dùng lại, không tự chế mới)

| Khuôn | Dùng cho | Cấu trúc bắt buộc |
|---|---|---|
| Page Shell | Mọi màn | Sidebar trái (menu module) + Topbar (tên màn, role hiện tại) |
| List View | Danh sách record | Filter bar → Table → Pagination |
| Form Panel | Tạo/sửa record | Breadcrumb → Section theo nhóm field → Save/Cancel cố định cuối |
| KPI Card | Dashboard | Label nhỏ trên → số liệu lớn giữa → chỉ báo tăng/giảm dưới |
| Status Badge | Trạng thái | Đúng 1 trong 3 màu: success/warning/danger |
| Filter Bar | Trên List View | Tối đa 3-4 filter phổ biến nhất |
| AI Insight Strip | Màn CRUD/Dashboard có insight AI thật liên quan (chi phí, tồn kho, đơn hàng...) | 1 dòng ngang, gọn: icon nhỏ + 1 câu insight ngắn (≤ 2 dòng) + link "Xem phân tích đầy đủ →" dẫn sang `bo-ai-phan-tich`. Đặt ngay dưới hàng KPI, phía trên bảng/danh sách chính. |
| AI Chat Workspace | Trò chuyện tương tác với AI Copilot / Trợ lý số | Cột trái (Lịch sử hội thoại & chủ đề đã ghim) + Khung giữa (Header phiên → Luồng tin nhắn chat với thẻ số liệu bằng chứng / hành động → Prompt gợi ý nhanh → Khung nhập lệnh cố định cuối) |

# Điều kiện áp dụng AI Insight Strip (bắt buộc kiểm tra trước khi thêm vào 1 màn)

1. Chỉ xuất hiện khi có insight THẬT liên quan trực tiếp tới dữ liệu đang xem trên
   màn đó — không tự bịa câu insight chung chung để "cho có". Nếu không có insight
   cụ thể, ẩn hẳn khối này, không hiện placeholder rỗng.
2. Nội dung PHẢI dựa trên dữ liệu có thể trỏ tới được (số liệu, khoảng thời gian,
   nguồn) — theo đúng nguyên tắc Explainability trong Non-Functional Requirements
   (phân biệt fact/calculation/forecast/recommendation, không viết prose mơ hồ
   không kiểm chứng được).
3. KHÔNG được là hero card to, KHÔNG gradient màu nổi bật, KHÔNG có 2 nút hành động
   cạnh tranh với action chính của màn hình — chỉ 1 dòng + 1 link duy nhất.
4. KHÔNG tự viết lại format khác nhau ở mỗi màn — mọi màn dùng insight đều phải
   dùng đúng cấu trúc "icon + 1-2 dòng + 1 link" này, không được sáng tạo riêng.
5. Đây là khuôn TÙY CHỌN (không bắt buộc có ở mọi màn) — chỉ thêm khi bước
   `/map-erd` hoặc `/build-screen` xác nhận có insight thật đáng hiển thị

## Quy trình khi CẦN khuôn mới (vd AI Advisor chat, Simulation compare)

Không tự chế và build luôn. Thực hiện theo thứ tự:
1. Xác nhận không khuôn nào ở trên phù hợp.
2. Viết đề xuất khuôn mới vào cuối file này (thêm 1 dòng bảng: tên khuôn, dùng cho gì,
   cấu trúc bắt buộc) — coi như đang "xin mở rộng contract".
3. Build màn hình theo khuôn vừa thêm.
4. Báo lại cho người dùng: "đã thêm khuôn X vào design-system.md vì chưa có khuôn phù hợp".

Không được bỏ qua bước 2 — mọi khuôn dùng để build phải có mặt trong bảng này,
kể cả khuôn mới, để lần build sau tái sử dụng đúng thay vì chế lại từ đầu.

# Design System — Icon Policy

Lý do đổi: emoji (💰✅⚠⏳🤖) render khác nhau giữa Windows/Mac/Linux, màu sắc
hoạt hình không hợp phong cách admin tool chuyên nghiệp — nhìn giống UI AI tự
chế. Icon-font ngoài (Material Symbols...) vẫn CẤM như rule cũ vì phụ thuộc
mạng. Giải pháp: **inline SVG nét mảnh (stroke-based)**, copy ĐÚNG NGUYÊN VĂN
từ thư viện dưới đây — không tự vẽ path mới, không đổi stroke-width.

## Quy tắc dùng

- Mọi icon: `width="18" height="18" viewBox="0 0 20 20" fill="none"
  stroke="currentColor" stroke-width="1.6" stroke-linecap="round"
  stroke-linejoin="round"` — `currentColor` để icon tự đổi màu theo class cha
  (`.badge-success` icon tự xanh, `.badge-danger` icon tự đỏ...), không cần
  set màu tay cho từng icon.
- Copy nguyên khối `<svg>...</svg>` bên dưới, không chỉnh path.
- Nếu cần ý nghĩa chưa có trong thư viện, chọn icon gần nghĩa nhất bên dưới,
  KHÔNG tự vẽ path mới — báo lại nếu thật sự không có icon nào phù hợp.

## Thư viện icon (copy nguyên văn)

**Thêm / Nhập** (nút "+ Nhập kho", "+ Tạo mới")
```html
<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><line x1="10" y1="4" x2="10" y2="16"/><line x1="4" y1="10" x2="16" y2="10"/></svg>
```

**Bớt / Xuất** (nút "- Xuất kho")
```html
<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><line x1="4" y1="10" x2="16" y2="10"/></svg>
```

**Điều chỉnh** (sliders — nút "± Điều chỉnh")
```html
<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><line x1="4" y1="6" x2="16" y2="6"/><circle cx="12" cy="6" r="1.4" fill="currentColor" stroke="none"/><line x1="4" y1="10" x2="16" y2="10"/><circle cx="7" cy="10" r="1.4" fill="currentColor" stroke="none"/><line x1="4" y1="14" x2="16" y2="14"/><circle cx="14" cy="14" r="1.4" fill="currentColor" stroke="none"/></svg>
```

**Thành công / An toàn** (status badge success)
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="10" r="7.5"/><polyline points="6.5,10.2 9,12.8 13.8,7.5"/></svg>
```

**Cảnh báo** (status badge warning)
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3 L18 17 L2 17 Z"/><line x1="10" y1="8.5" x2="10" y2="12.5"/><circle cx="10" cy="14.5" r="0.9" fill="currentColor" stroke="none"/></svg>
```

**Lỗi / Nguy cấp** (status badge danger)
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="10" cy="10" r="7.5"/><line x1="7.3" y1="7.3" x2="12.7" y2="12.7"/><line x1="12.7" y1="7.3" x2="7.3" y2="12.7"/></svg>
```

**Tìm kiếm** (filter bar)
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="8.5" cy="8.5" r="5"/><line x1="12.3" y1="12.3" x2="17" y2="17"/></svg>
```

**Xuất file / Tải xuống**
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="10" y1="3" x2="10" y2="12.5"/><polyline points="6,9 10,13 14,9"/><line x1="4" y1="16.5" x2="16" y2="16.5"/></svg>
```

**In** (nút "In Phiếu Đóng Gói")
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2.5" width="10" height="5" rx="0.5"/><rect x="3" y="7.5" width="14" height="7" rx="1"/><rect x="6" y="12" width="8" height="5.5" rx="0.5"/></svg>
```

**Đồng bộ / Làm mới**
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10a6 6 0 0 1 10.3-4.2"/><polyline points="14,2.5 14.3,6 10.8,5.7"/><path d="M16 10a6 6 0 0 1-10.3 4.2"/><polyline points="6,17.5 5.7,14 9.2,14.3"/></svg>
```

**Thông tin**
```html
<svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="10" cy="10" r="7.5"/><line x1="10" y1="9" x2="10" y2="14"/><circle cx="10" cy="6" r="0.9" fill="currentColor" stroke="none"/></svg>
```

**Mũi tên điều hướng (dropdown/link "Xem đầy đủ →")**
```html
<svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="10" x2="15" y2="10"/><polyline points="11,6 15,10 11,14"/></svg>
```

**AI Insight Strip (icon mở đầu — thay cho ⚙️/🤖)**
```html
<svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="12" height="9" rx="2"/><line x1="10" y1="6" x2="10" y2="3"/><circle cx="10" cy="2.3" r="0.8" fill="currentColor" stroke="none"/><circle cx="7.3" cy="10.5" r="1" fill="currentColor" stroke="none"/><circle cx="12.7" cy="10.5" r="1" fill="currentColor" stroke="none"/></svg>
```

**Hộp / Tồn kho (icon tiêu đề trang Inventory)**
```html
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 6.5 L10 3 L17.5 6.5 L10 10 Z"/><path d="M2.5 6.5 V14 L10 17.5 L17.5 14 V6.5"/><line x1="10" y1="10" x2="10" y2="17.5"/></svg>
```

**Đơn hàng / Chứng từ (icon tiêu đề trang Order)**
```html
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2.5" width="12" height="15" rx="1.5"/><line x1="7" y1="6.5" x2="13" y2="6.5"/><line x1="7" y1="9.5" x2="13" y2="9.5"/><line x1="7" y1="12.5" x2="10.5" y2="12.5"/></svg>
```

## Checklist bổ sung (build-screen.md)

- [ ] Không dùng emoji (💰✅⚠⏳🤖...) và không dùng icon-font ngoài
- [ ] Icon copy nguyên văn từ thư viện trên, không tự chỉnh path/stroke-width
- [ ] Cùng 1 ý nghĩa dùng đúng 1 icon xuyên suốt mọi màn (không đổi icon khác cho cùng ý nghĩa)

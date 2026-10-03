# Rule: Navigation — Top Nav + Dropdown (thay thế Sidebar)

Ghi đè định nghĩa "Page Shell" cũ trong `design-system.md`. Lý do: sidebar liệt kê
phẳng không scale khi có ~20 màn hình; top-nav ngang + dropdown là pattern thật của
Odoo và là nguyên nhân chính khiến UI của họ gọn.

## Page Shell mới (bắt buộc dùng cho mọi màn từ giờ)

```
Topbar cố định trên cùng:
[Logo ABC] [Mục menu 1] [Mục menu 2] ... [Mục menu N]      [User badge/role]

Click vào 1 mục menu → dropdown xổ xuống các màn con thuộc nhóm đó.
KHÔNG còn sidebar dọc bên trái. Vùng nội dung chiếm toàn bộ chiều ngang còn lại.
```

## Bản đồ IA (Information Architecture) — top-level menu & dropdown con

| Menu chính | Dropdown con | Nguồn (bo_XX / FE) |
|---|---|---|
| **Tổng quan** | (không có dropdown — 1 màn dashboard) | FE-08 |
| **Sản phẩm** | Danh sách sản phẩm · Danh mục · Nhà cung cấp | FE-02, FE-05 |
| **Kho** | Tồn kho · Lô hàng & hạn dùng · Điều chỉnh tồn kho | FE-03, FE-04 |
| **Bán hàng** | Đơn hàng · Khách hàng · Thanh toán | FE-06 |
| **Tài chính** | Chi phí · Dòng tiền | FE-07 |
| **AI Insights** | Copilot · Phân tích kinh doanh · Cảnh báo bất thường · Dự báo nhu cầu · Inventory Intelligence · Mô phỏng What-if | FE-09, 10, 11, 12, 13, 14 |
| **Thông báo** | (icon chuông riêng ở topbar, không cần dropdown) | FE-15 |
| **Quản lý** | Nhân viên & phân quyền · Audit log · Cấu hình hệ thống | FE-01, FE-16, mục 3 |

Mỗi màn hình (`bo_XX`) PHẢI được gán đúng 1 vị trí trong bản đồ này trước khi build
— nếu 1 màn không khớp mục nào ở trên, dừng lại và hỏi, không tự thêm menu mới vào
bảng mà không xác nhận.

## Cập nhật Component Contract

Xóa dòng "Page Shell = Sidebar + Topbar" cũ trong `design-system.md`, thay bằng:

| Khuôn | Cấu trúc bắt buộc |
|---|---|
| Page Shell | Topbar ngang cố định (logo + menu items + user badge). Menu item có dropdown con khi có ≥2 màn con theo bản đồ IA. KHÔNG có sidebar dọc. |

Mọi rule khác (List View, Form Panel, KPI Card, Status Badge, Filter Bar,
content-density) giữ nguyên không đổi.

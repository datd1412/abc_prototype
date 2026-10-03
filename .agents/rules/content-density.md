# Rule: Content Density (Phân cấp thông tin)

Bổ sung cho `.agents/rules/design-system.md` — áp dụng bắt buộc cho MỌI màn hình.

## 1. Primary field vs Secondary field

Mỗi entity có 2 nhóm field, PHẢI phân loại trước khi build:

- **Primary field** (tối đa 5-6, hiển thị trên List View/Card): những field người
  dùng cần liếc mắt là hiểu ngay — tên, mã, giá bán, trạng thái, 1 con số tồn kho
  tổng. KHÔNG hiển thị công thức tính toán, breakdown, hay field kỹ thuật ở đây.
- **Secondary field** (còn lại: costPrice, attributes chi tiết, reservedQty,
  batch info, margin breakdown...): CHỈ hiển thị khi người dùng chủ động mở
  Form Panel/Drawer của 1 record cụ thể. Không được hiện sẵn ngoài List View
  dưới bất kỳ hình thức nào (kể cả dòng phụ nhỏ dưới tên).

Ví dụ áp dụng cho `products`/`product_variants`:
- Primary (List View): tên sản phẩm, SKU, danh mục, giá bán, tồn kho, trạng thái.
- Secondary (Form Panel khi click): giá vốn, biên lợi nhuận, attributes
  (size/màu/dung tích), batch/lô, reservedQty, ngày tạo/sửa.

Khi build 1 màn hình, PHẢI tự hỏi: "field này người dùng cần thấy NGAY khi lướt
danh sách, hay chỉ cần khi họ chủ động xem chi tiết 1 record?" — nếu là vế sau,
đưa vào Form Panel, không đưa vào List View.

## 2. Cấm tự chế thêm khối/widget ngoài Component Contract

Mỗi màn hình build ra CHỈ được ghép từ đúng các khuôn đã duyệt trong
`design-system.md` (Page Shell, List View, Form Panel, KPI Card, Status Badge,
Filter Bar). Các khối như "ma trận phân tích", "simulator tính toán trực tiếp",
"bảng so sánh"... KHÔNG được tự thêm vào 1 màn CRUD thông thường (List/Form) —
những khối này (nếu thật sự cần) thuộc về Dashboard/Simulation, tách màn riêng,
và PHẢI qua quy trình "xin mở rộng contract" ở `design-system.md` trước khi build,
không tự quyết rồi build luôn.

**Quy tắc đơn giản: 1 màn hình = 1 mục đích chính = 1-2 khuôn ghép lại
(vd List View + Filter Bar). Không gộp thêm mục đích thứ 3 (phân tích, mô phỏng)
vào cùng 1 màn CRUD.**

## 3. Cấm tuyệt đối: lộ ghi chú nội bộ (ERD/FR compliance note) ra UI

Mọi nội dung dạng "field này khớp entity nào trong ERD", "đã verify theo data
contract", tên field kỹ thuật camelCase (`costPrice`, `reservedQty`,
`expiresAt`...) — đây là ghi chú NỘI BỘ cho quá trình build, TUYỆT ĐỐI không
được render thành text/card hiển thị cho end-user trong file HTML output.

Ghi chú loại này chỉ được phép nằm ở:
- Comment HTML (`<!-- -->`), không hiển thị khi mở bằng trình duyệt, HOẶC
- File riêng trong `prototype/_notes/`, không phải trong file `.html` của màn hình.

## 4. Checklist bổ sung (thêm vào DoD ở build-screen.md)

- [ ] List View/Card chỉ có tối đa 5-6 primary field, không nhồi thêm dòng phụ
- [ ] Không có khối/widget nào ngoài 6 khuôn đã duyệt, trừ khi đã qua quy trình mở rộng
- [ ] Không có bất kỳ chuỗi text nào là tên field kỹ thuật (camelCase) hay ghi chú
      "khớp ERD/FR" hiển thị trực tiếp trong nội dung UI

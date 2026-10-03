# Workflow: /extract-content <ten_folder_stitch>

Chỉ làm ĐÚNG việc trích nội dung. Không style, không đối chiếu ERD ở bước này.

## Input
1 folder trong `stitch_ai_business_copilot_platform/` (chứa `code.html` + `screen.png`).

## Việc cần làm
Đọc `code.html`, bỏ qua toàn bộ class/style/Tailwind config, chỉ lấy:
- Tên màn hình (tiếng Việt, từ tiêu đề/h1)
- Danh sách field đang hiển thị (tên field + giá trị mẫu nếu có trong HTML)
- Danh sách action/button (tên nút, mục đích)
- Ghi chú UX đặc biệt nếu có (tab, filter, trạng thái, bảng, form...)

## Output
Ghi ra `abc-prototype/prototype/_extracted/<ten_folder>.md` theo mẫu:

```markdown
# <Tên màn hình>
Nguồn: stitch_ai_business_copilot_platform/<ten_folder>/code.html

## Field đang hiển thị
- <label hiển thị>: <giá trị mẫu nếu có>

## Action/Button
- <tên nút>: <mục đích>

## Ghi chú UX
- <mô tả tab/filter/trạng thái nếu có>
```

Không tự đánh giá đẹp/xấu, không đề xuất sửa layout ở bước này.

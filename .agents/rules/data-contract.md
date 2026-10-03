# Rule: Data Contract

## Nguồn trọng tài
- `erd/SEP490_entities_fields.txt` — field nào TỒN TẠI.
- `fr/fr-requirements.md` — chức năng nào NẰM TRONG SCOPE (chú ý mục Limitations LI-1→LI-8).

## Quy trình bắt buộc cho MỖI field trước khi đưa lên UI

1. Tìm tên field (hoặc field gần nghĩa) trong `erd/SEP490_entities_fields.txt`.
2. Không tìm thấy → LOẠI BỎ khỏi UI. Không tự thêm field vào ERD để hợp lý hóa.
   Ghi lại vào `prototype/_notes/removed-fields.md`: tên field, màn hình nào, lý do
   loại (không có trong ERD).
3. Có trong ERD nhưng đối chiếu `fr/` thấy chức năng bị liệt kê trong Limitations
   (LI-1→LI-8) → LOẠI BỎ, ghi chú tương tự bước 2 nhưng lý do là "ngoài scope (LI-x)".
4. Có trong ERD + trong scope nhưng Stitch không vẽ → PHẢI bổ sung vào UI, không bỏ
   qua chỉ vì bản thiết kế gốc thiếu.

## Nhất quán nhãn tiếng Việt (label consistency)

Giữ 1 bảng ánh xạ field ↔ label tại `prototype/_notes/field-labels.md`, cập nhật
MỖI KHI build 1 màn hình mới:

```
| Field (ERD, camelCase) | Label tiếng Việt dùng trên UI | Màn hình dùng đầu tiên |
|---|---|---|
| sellingPrice | Giá bán | product-list |
| costPrice | Giá vốn | product-list |
| lowStockThreshold | Ngưỡng tồn thấp | inventory-list |
```

Trước khi đặt label mới cho 1 field, TRA bảng này trước — nếu field đã có label ở
màn khác, dùng lại y nguyên, không đặt tên khác đi (vd không được vừa gọi
"Giá bán" ở màn Product vừa gọi "Đơn giá" ở màn Order cho cùng field `sellingPrice`).

## Khi phát hiện field ERD có tên mơ hồ hoặc thiếu ngữ cảnh
Không tự suy đoán ý nghĩa và gán label liều. Dừng lại, liệt kê field đó và hỏi người
dùng, hoặc suy ra từ cách nó được dùng trong `fr/fr-requirements.md` nếu có nhắc tới.

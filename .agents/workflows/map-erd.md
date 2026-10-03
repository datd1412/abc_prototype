# Workflow: /map-erd <ten_file_extracted>

Chỉ làm ĐÚNG việc đối chiếu. Không build HTML ở bước này.

## Input
`abc-prototype/prototype/_extracted/<ten_file>.md` (kết quả của /extract-content)

## Việc cần làm
Với MỖI field trong file input, tuân theo `.agents/rules/data-contract.md`:
1. Tra `erd/SEP490_entities_fields.txt` → có/không.
2. Nếu có, tra `fr/fr-requirements.md` → chức năng có bị loại trừ (LI-1→LI-8) không.
3. Đánh dấu kết quả: GIỮ / LOẠI (kèm lý do).
4. Rà thêm chiều ngược lại: entity liên quan trong ERD có field nào QUAN TRỌNG mà
   file extracted đang thiếu không (vd `lowStockThreshold`, `expiresAt`) → đánh dấu
   THIẾU - CẦN BỔ SUNG.

## Output
Ghi ra `abc-prototype/prototype/_extracted/<ten_file>-mapped.md`:

```markdown
# <Tên màn hình> — đã đối chiếu ERD/FR

## Field GIỮ
- <field ERD (camelCase)> → <label tiếng Việt, tra field-labels.md trước khi đặt mới>

## Field LOẠI
- <field/tính năng>: <lý do — không có trong ERD / ngoài scope LI-x>

## Field THIẾU - CẦN BỔ SUNG
- <field ERD>: có trong entity <tên entity> nhưng Stitch không vẽ
```

Cập nhật `prototype/_notes/removed-fields.md` và `prototype/_notes/field-labels.md`
theo đúng rule trong `.agents/rules/data-contract.md`.

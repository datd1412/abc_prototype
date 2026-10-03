# Rule: Source Boundaries

## Ma trận quyền (kiểm tra trước MỌI thao tác ghi file)

| Path | Quyền | Ghi chú |
|---|---|---|
| `stitch_ai_business_copilot_platform/**` | READ-ONLY | Chỉ trích nội dung (label, field hiển thị, action). |
| `odoo-20.0/**` | READ-ONLY, giới hạn whitelist bên dưới | Chỉ tham chiếu bố cục. |
| `erd/**` | READ-ONLY | Trọng tài field. |
| `fr/**` | READ-ONLY | Trọng tài scope/chức năng. |
| `abc-prototype/prototype/**` | READ-WRITE | Nơi DUY NHẤT được tạo/sửa/xóa file. |
| Mọi path khác | KHÔNG ĐỘNG VÀO | Không tạo file ngoài các path trên. |

## Whitelist trong odoo-20.0/ (chỉ được đọc các addon sau)

```
odoo-20.0/addons/product/
odoo-20.0/addons/stock/
odoo-20.0/addons/sale/
odoo-20.0/addons/purchase/
odoo-20.0/addons/hr_expense/
odoo-20.0/addons/account/
```

Không tự ý đọc addon khác (mrp, website, hr, l10n_*, point_of_sale, crm...) trừ khi
người dùng yêu cầu rõ ràng trong prompt của task đó. Nếu thấy cần tham khảo addon
ngoài danh sách này để làm tốt hơn — DỪNG LẠI, hỏi trước, không tự mở rộng phạm vi.

## Quy tắc cứng

1. Trước khi gọi write/edit file, tự kiểm: path có nằm trong
   `abc-prototype/prototype/` không? Nếu không → KHÔNG THỰC HIỆN, báo lỗi ranh giới.
2. Không bao giờ chạy lệnh xóa/sửa hàng loạt (`rm -rf`, format lại thư mục...) chạm
   tới `stitch_ai_business_copilot_platform/` hoặc `odoo-20.0/`.
3. Nếu 1 task yêu cầu mơ hồ có thể hiểu là "sửa Odoo" hoặc "sửa Stitch gốc" — hỏi lại
   để làm rõ ý định trước khi làm, không tự suy diễn theo hướng được phép ghi.

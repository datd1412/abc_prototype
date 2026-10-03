# Rule: Slug Registry (tự động khi vượt quá danh sách đã biết)

Bảng slug tĩnh trong `linking.md` chỉ là VÍ DỤ KHỞI ĐẦU (~23 màn đã biết rõ),
KHÔNG phải danh sách đóng. Với >50 màn hình thật, không liệt kê tay hết — dùng
quy trình này để agent tự đặt tên nhất quán, và `nav-owner.js` / `nav-employee.js`
/ `nav-admin.js` mới là REGISTRY THẬT (nguồn sự thật sống), bảng markdown chỉ để
tham khảo ban đầu, không cần đồng bộ tay theo mỗi màn mới.

## Xác định portal (không mơ hồ — lấy thẳng từ tên folder Stitch)

Folder Stitch có prefix `bo_`/`se_`/`sa_` → map thẳng sang role-prefix `bo-`/`se-`/`sa-`.
Không cần đoán, không cần hỏi — luôn xác định được portal ngay từ tên folder gốc.

## Thuật toán tạo slug cho 1 màn MỚI (chưa có trong nav-*.js)

1. Lấy "Tên màn hình" đã trích ở bước `/extract-content` (tiêu đề tiếng Việt).
2. Bỏ dấu, chuyển thường, nối bằng gạch ngang, tối đa 4 từ có nghĩa
   (bỏ từ đệm như "quản lý", "màn hình", "trang" nếu tên đã đủ rõ nghĩa không cần).
3. Ghép: `<role-prefix>-<ten-da-xu-ly>`.
4. Trước khi dùng slug này, tra trong `nav-<role>.js` xem đã có slug giống hệt
   hoặc gần giống (cùng tiêu đề màn hình) chưa:
   - Đã có → DÙNG LẠI slug cũ, không tạo slug mới cho cùng 1 màn.
   - Trùng tên nhưng nội dung khác nhau thật sự → thêm hậu tố số (`-2`, `-3`).
   - Chưa có → dùng slug mới vừa tạo.

## Tự động đăng ký vào nav-<role>.js (làm NGAY trong cùng lần build, không tách bước riêng)

1. Xác định nhóm menu phù hợp nhất trong các nhóm đã có (Sản phẩm/Kho/Bán hàng/
   Tài chính/AI Insights/Quản lý cho owner; nhóm tương ứng cho employee/admin) —
   so khớp theo entity/chức năng của màn hình với nhóm hiện tại.
2. Nếu khớp 1 nhóm có sẵn → append entry `{ label, slug }` vào đúng `children` của
   nhóm đó trong file `nav-<role>.js`.
3. Nếu KHÔNG nhóm nào phù hợp rõ ràng → thêm vào nhóm `"Khác"` cuối danh sách
   (tạo nhóm này nếu chưa có) — KHÔNG bịa tên nhóm mới tùy tiện mỗi lần, luôn dùng
   đúng 1 nhóm "Khác" gộp chung cho các trường hợp không rõ.
4. Sau khi đăng ký xong mới tạo file `.html` với đúng slug đó.

## Khi nào THẬT SỰ dừng lại hỏi (không tự động hóa được)

- Không xác định được portal (tên folder Stitch không có prefix bo_/se_/sa_ rõ ràng).
- 2 màn hình có vẻ trùng hoàn toàn về slug VÀ nội dung (nghi ngờ bị duplicate
  giống trường hợp `bo_06`/`bo_09`/`bo_11` từng gặp) → hỏi trước khi đăng ký, không
  tự chọn 1 bản rồi bỏ bản kia.
- Sau khi bỏ dấu + rút gọn, tiêu đề màn hình không đủ rõ nghĩa để đặt slug có ý
  nghĩa (hiếm, nhưng nếu gặp thì dừng, hỏi tên gợi ý thay vì tự bịa slug vô nghĩa).

Ngoài 3 trường hợp trên, KHÔNG cần hỏi từng màn một — cứ theo thuật toán mà chạy,
vì mục tiêu là xử lý được 50+ màn mà không phải dừng lại xin duyệt từng cái.

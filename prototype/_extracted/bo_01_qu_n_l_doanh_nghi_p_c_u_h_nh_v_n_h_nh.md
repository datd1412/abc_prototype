# BO-01: Quản lý Doanh nghiệp & Cấu hình Vận hành
Nguồn: stitch_ai_business_copilot_platform/bo_01_qu_n_l_doanh_nghi_p_c_u_h_nh_v_n_h_nh/code.html

## Field đang hiển thị
- Tiêu đề màn hình: Quản lý Doanh nghiệp & Cấu hình Vận hành
- Tên doanh nghiệp: Maison de Bloom
- Loại hình doanh nghiệp: Công ty Cổ phần
- Mã số thuế: 0317892341
- Ngành hàng: Mỹ phẩm & Thời trang
- Email chính thức: contact@maisondebloom.vn
- Hotline: 1900 6886
- Người đại diện: Nguyễn Thị Mai
- Địa chỉ trụ sở: Tầng 5, Bloom Tower, 128 Hai Bà Trưng, P. Đa Kao, Q.1, TP.HCM
- Đơn vị tiền tệ: VND (₫)
- Múi giờ hệ thống: GMT+7
- Ngưỡng tồn kho an toàn mặc định: < 15 Ngày bán
- Cảnh báo hạn sử dụng mỹ phẩm: < 90 Ngày hết hạn
- Thống kê KPI: Doanh thu lũy kế (1.845.200.000 ₫), Đơn hàng đã xử lý (4.280 đơn), Chi phí ghi nhận (412.500.000 ₫), Giá trị tồn kho thực tế (890.400.000 ₫)
- Bảng danh sách nhân sự & Phân quyền RBAC:
  - Họ và tên nhân viên: Nguyễn Thị Mai, Trần Văn Nam, Lê Thị Hương
  - Email / Liên hệ nhân viên: mai.nguyen@maisondebloom.vn, nam.tran@maisondebloom.vn
  - Vai trò (Role): Business Owner, Store Employee, Accountant
  - Phân quyền (Permissions): Full System Access, POS & Sales, Financial Read
  - Trạng thái: Hoạt động / Tạm khóa

## Action/Button
- `Tạo Doanh nghiệp Mới (+)`: Tạo mới hồ sơ doanh nghiệp
- `Lịch sử Cấu hình (Audit)`: Xem nhật ký audit log thay đổi cấu hình
- `Lưu Thay đổi Toàn bộ`: Lưu cập nhật cấu hình doanh nghiệp & tham số
- `Cập nhật Hồ sơ Doanh nghiệp`: Mở form chỉnh sửa thông tin pháp lý
- `Đổi Logo / Nhận diện`: Tải lên logo thương hiệu
- `Thêm Nhân viên Mới (+)`: Mở modal thêm nhân sự và gán vai trò RBAC
- `Chỉnh sửa` / `Gán quyền`: Cập nhật quyền truy cập cho từng nhân viên

## Ghi chú UX
- Layout chia thành các khối card chính: Hồ sơ doanh nghiệp, Tham số vận hành & tiền tệ, Ngưỡng cảnh báo rủi ro, Bảng danh sách nhân sự & RBAC.
- Phân quyền nhân sự theo mô hình RBAC (Role-Based Access Control).

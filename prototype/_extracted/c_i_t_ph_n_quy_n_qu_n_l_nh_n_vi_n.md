# Trích xuất Nội dung: Quản lý Nhân viên & Ma trận Phân quyền (RBAC)
**Nguồn**: `stitch_ai_business_copilot_platform/c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n/`

## 1. Tiêu đề & Điều hướng
- Tiêu đề: "Quản lý Nhân viên & Ma trận Phân quyền (RBAC)"
- Actions hàng trên:
  - "+ Thêm Nhân viên Mới" (Mở modal thêm nhân sự)
  - "+ Thêm Vai trò Mới"
  - "Xuất Nhật ký Audit (.csv)"

## 2. Tabs điều hướng trong trang
- Tab 1: "Danh sách Nhân sự (18)"
- Tab 2: "Ma trận Phân quyền Chi tiết (Role Matrix)"
- Tab 3: "Chính sách Giới hạn & Ngưỡng duyệt"

## 3. Bảng Danh sách Cán bộ Nhân viên
- Cột:
  1. Nhân viên (Họ tên, email, mã NV)
  2. Vai trò Hệ thống (Owner / Super Admin, Kế toán Trưởng, Trưởng Kho, Thu ngân Lead, Vận hành TMĐT, Bán hàng)
  3. Phạm vi phụ trách (Toàn chuỗi, Bộ phận Tài chính, Kho Logistics, Quầy POS 01-02, Gian hàng trực tuyến)
  4. Quyền hạn trọng yếu & Rào chắn dữ liệu (Root Access, Hạn mức chi, Khóa COGS, Khóa giá niêm yết...)
  5. Bảo mật 2FA & Thiết bị (YubiKey, Authenticator, SMS OTP, Zalo OTP...)
  6. Trạng thái (Online, Đang trong ca, Hoạt động gần nhất)
  7. Thao tác (Cấu hình quyền, Xem log truy cập, Khóa/Mở khóa)

## 4. Ma trận Phân quyền (Access Control Matrix)
- Ma trận các phân hệ vs 5 vai trò:
  - Báo cáo Lãi Lỗ P&L & Dòng tiền: Owner (Toàn quyền), Kế toán (Xem & Phân tích), Kho (Khóa), Thu ngân (Khóa), TMĐT (Khóa).
  - Xem Giá Vốn Hàng Nhập (COGS): Owner (Toàn quyền), Kế toán (Toàn bộ SKU), Kho (Ẩn hoàn toàn), Thu ngân (Ẩn), TMĐT (Ẩn).
  - Duyệt Phiếu Chi & Quét VietQR B2B: Owner (Không giới hạn), Kế toán (< 100M VND), Kho (Tạo nháp đề xuất), Thu ngân (Chỉ xem thu), TMĐT (Khóa).
  - Nhập kho & Khởi tạo Lô Date (PO): Owner (Toàn quyền), Kế toán (Đối soát công nợ), Kho (Toàn quyền thực thi), Thu ngân (Khóa), TMĐT (Khóa).
  - POS & Bán lẻ Showroom: Owner (Có), Kế toán (Xem sổ cái POS), Kho (Xem xuất nhập), Thu ngân (Toàn quyền), TMĐT (Xem tồn showroom).
  - Quản lý Ví Sàn & Rút Tiền: Owner (Toàn quyền OTP), Kế toán (Đối soát & Khớp ví), Kho (Khóa), Thu ngân (Khóa), TMĐT (Chỉ đóng đơn).
  - AI Copilot & Mô phỏng: Owner (Toàn quyền), Kế toán (Mô phỏng Dòng tiền), Kho (Dự báo ROP & Tồn), Thu ngân (Khóa), TMĐT (Gợi ý Ads).

## 5. Thẻ Chính sách An ninh & Rào chắn Bổ trợ
- Quy tắc Ngưỡng Phê duyệt Tài chính: Tự động yêu cầu phê duyệt 2 cấp đối với giao dịch chi > 50.000.000 ₫.
- Giới hạn IP & Thiết bị POS: Chỉ cho phép mở ca thu ngân từ các địa chỉ MAC/IP thiết bị quầy đã đăng ký.
- Mặt nạ Dữ liệu Khách hàng (Data Masking): Ẩn 4 số cuối điện thoại & địa chỉ khách đối với tài khoản nhân viên bán lẻ/kho.

# SE-03: Giao Ca & Kết Sổ Bán Hàng (Cashier Shift Handover & Drawer Settlement)
Nguồn: stitch_ai_business_copilot_platform/se_03_giao_ca_k_t_s_b_n_h_ng_cashier_shift_handover_drawer_settlement/code.html

## Field đang hiển thị
- Mã ca trực: #SFT-20241024-AM (Ca Sáng: 08:00 - 16:00)
- Nhân viên giao ca (Cashier Out): Nguyễn Thị Mai (#02)
- Nhân viên nhận ca (Cashier In): Lê Văn Nam (#01)
- Quản lý duyệt bàn giao: Trần Thu Hà (Store Manager)
- Tổng doanh thu ca trực: 24.850.000 ₫ (36 giao dịch thành công)
- Doanh thu không tiền mặt (Số): 18.650.000 ₫
  + VietQR Pro: 14.250.000 ₫ (24 đơn)
  + Thẻ POS & Ví điện tử: 4.400.000 ₫ (8 đơn)
- Tiền mặt theo sổ sách: 6.200.000 ₫
  + Tiền đầu ca (Opening Float): 2.000.000 ₫
  + Doanh thu tiền mặt bán hàng: 4.500.000 ₫
  + Chi tiền mặt trong ca: -300.000 ₫
- Tiền mặt thực tế đếm được trong két: 6.220.000 ₫
- Chênh lệch két: +20.000 ₫ (Tiền tip khách lẻ tích lũy)
- Bảng kiểm đếm mệnh giá tiền mặt:
  + 500.000 ₫: 6 tờ = 3.000.000 ₫
  + 200.000 ₫: 8 tờ = 1.600.000 ₫
  + 100.000 ₫: 10 tờ = 1.000.000 ₫
  + 50.000 ₫: 6 tờ = 300.000 ₫
  + 20.000 ₫: 10 tờ = 200.000 ₫
  + 10.000 ₫: 8 tờ = 80.000 ₫
  + Tiền lẻ (5.000 ₫ & 2.000 ₫): 40.000 ₫
- Tiền mặt để lại két cho ca tiếp theo (Closing Float): 2.000.000 ₫
- Tiền mặt nộp về két sắt / quản lý (Cash Drop): 4.220.000 ₫
- Nhật ký phiếu chi phụ trợ trong ca:
  + Chi mua giấy in bill K80: -200.000 ₫
  + Chi nước đá & phụ phí quầy: -100.000 ₫
- Đối soát cổng thanh toán số (VietQR, Thẻ POS, MoMo)
- Biên bản bàn giao 3 bên & chữ ký điện tử xác nhận

## Action/Button
- Đồng bộ theo sổ sách
- Tăng/Giảm số tờ tiền từng mệnh giá (+ / -)
- In Tạm [F7]
- In Biên Bản Giao Ca [F8]
- Báo Sai Lệch [F11]
- Lưu Nháp Tạm Thời
- XÁC NHẬN BÀN GIAO & KHÓA KÉT [F9]

## Ghi chú UX
- Giao diện kết ca chuyên dụng dành cho thu ngân và quản lý ca quầy POS.
- Đếm tiền mặt trực quan, tự động tính toán tổng tiền két, số tiền nộp về quản lý và chênh lệch so với doanh thu sổ sách.

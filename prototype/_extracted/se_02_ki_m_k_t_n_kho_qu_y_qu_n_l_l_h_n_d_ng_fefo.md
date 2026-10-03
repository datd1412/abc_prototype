# SE-02: Kiểm Kê Tồn Kho Quầy & Quản Lý Lô Hạn Dùng FEFO
Nguồn: stitch_ai_business_copilot_platform/se_02_ki_m_k_t_n_kho_qu_y_qu_n_l_l_h_n_d_ng_fefo/code.html

## Field đang hiển thị
- Mã phiên kiểm kê: #KK-20241024-Q1
- Nhân viên kiểm kê: Nguyễn Thị Mai (Thu ngân #02, Ca Sáng 08:00 - 16:00)
- Vị trí/Khu vực: Quầy Trưng Bày & Tủ Lưu Quầy Flagship Q.1
- Trạng thái phiên: Đang kiểm kê thực địa (Real-time Audit Active)
- Tiến độ kiểm kê: 42 / 68 SKU (61.8%)
- Tồn sổ sách & thực quét: 268 / 412 món (Chênh lệch: -144 món cần quét nốt)
- Giá trị tồn quầy: 168.450.000 ₫ (Sai lệch tạm tính: -420.000 ₫)
- Giám sát lô hạn dùng FEFO: 02 Lô Cận Hạn (Ưu tiên xuất trước 15/11/2024)
- Ô quét Barcode/QR/SKU: Input tìm kiếm quét mã vạch [F1]
- Trạng thái máy quét Barcode: Honeywell Xenon 1900G (Đang đọc liên tục)
- Chế độ đếm: Đếm cộng dồn (+1) / Nhập số lượng / Kiểm Date FEFO
- Tên sản phẩm: Serum Bio-B5 Hydra Max 100ml, Kem Phục Hồi Ceramide Aura Care, Son Kem Velvet #03 Đỏ Gạch, Nước Tẩy Trang Damask Rose 400ml, Phấn Nước Cushion SPF50+, Kem Chống Nắng SunShield 50ml
- Mã SKU: MB-SER-B5-01, MB-CRM-02, MB-LIP-VL-03, MB-CLEAN-01, MB-CUSH-21, MB-SUN-04
- Vị trí kệ: Kệ A1-02, Kệ B2-01, Kệ Mặt Tiền T1, Kệ C1-04, Tủ Kính VIP, Kệ A2-01
- Tồn sổ sách: 35, 18, 42, 24, 15, 29
- Thực đếm: 34, 18, 42, 24, 14, 31 (kèm chênh lệch: Lệch -1, Khớp 100%, Thừa +2)
- Số lô hàng (Lot/Batch): LOT-202410-B5, LOT-202409-CR, LOT-202311-VT, LOT-202408-MC, LOT-202406-CU, LOT-202410-SU
- Hạn sử dụng (FEFO): 10/2026, 09/2026, 11/2024 (còn 21 ngày), 08/2026, 06/2026, 10/2026
- Hàng mẫu thử (Tester): 1 Khui, 1 Có nắp, 2 Thỏi, 1 Chai, Không
- Lý do điều chỉnh / Ghi chú lệch: Khách thử làm đổ / Tester, Hàng hư hỏng vỡ seal, Nghi ngờ thất thoát, Chưa nhập đơn chuyển kho
- Cảnh báo FEFO: Lô Son Velvet #03 còn 4 cây HSD dưới 25 ngày
- Cảnh báo châm hàng kệ: Cảnh báo thiếu hàng mặt tiền (Serum Bio-B5)
- Nhật ký quét gần nhất: Thời gian quét, tên SKU, số lượng cộng dồn
- Tổng kết kiểm kê: 42 SKU đã kiểm tra, 4 Lệch thiếu, 2 Lệch thừa, Hao hụt ròng ước tính: -710.000 ₫

## Action/Button
- Tạm dừng phiên: Tạm dừng phiên kiểm kê quầy
- Lịch sử ca trước: Xem lịch sử kiểm kê các ca làm việc trước
- Cân bằng tức thì: Cân bằng số liệu thực tế và sổ sách
- + Biên Bản Kiểm Kê [F8]: Khởi tạo biên bản kiểm kê mới
- Quét mã vạch [F1]: Focus ô nhập barcode
- Mở máy ảnh quét QR: Kích hoạt camera quét barcode/QR
- Bộ lọc nhanh: Tất cả SKU quầy (68), Khớp chuẩn (36), Lệch thiếu/thừa (6), Cận Date (4), Hàng Tester (8)
- Tăng/Giảm thực đếm (+/-): Tăng giảm số lượng đếm thực tế
- Quét lại SKU: Quét lại barcode sản phẩm trong bảng
- In nhãn barcode kệ: In lại tem mã vạch dán trên kệ
- Báo cáo thất thoát: Ghi nhận sự cố nghi ngờ thất thoát
- Xem phiếu nhập kho liên quan: Xem phiếu chuyển kho chưa nhận
- Tạo Tem Giảm 20%: Tạo nhãn giảm giá xả hàng cận hạn
- Châm 15 chai lên kệ ngay: Ghi nhận chuyển hàng từ tủ quầy lên mặt kệ
- Lập phiếu xuất hao hụt Tester quầy: Mở form ghi nhận hao hụt
- In toàn bộ nhãn Barcode giá kệ mới: In nhãn kệ hàng loạt
- Xuất file Excel / PDF [F6]: Tải biên bản kiểm kê dạng file
- Hủy phiên: Hủy toàn bộ phiên kiểm kê hiện tại
- HOÀN TẤT KIỂM KÊ & GỬI QUẢN LÝ DUYỆT [F9]: Chốt phiên kiểm kê và gửi cấp trên phê duyệt

## Ghi chú UX
- Màn hình thao tác trực tiếp tại quầy thu ngân / kho quầy dành cho Store Employee (SE).
- Tích hợp phím tắt F1 (quét barcode), F6 (xuất file), F8 (biên bản), F9 (hoàn tất).
- Bảng đối soát giữa Tồn sổ sách (`inventory.quantity`) và Thực đếm, tự tính chênh lệch.
- Theo dõi chặt chẽ hạn dùng lô (`inventory_batches.expiresAt`) và phân loại lý do lệch (`inventory_transactions.reason`).

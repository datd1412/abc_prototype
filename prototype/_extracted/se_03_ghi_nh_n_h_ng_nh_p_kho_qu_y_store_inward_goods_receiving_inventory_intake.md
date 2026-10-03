# SE-03: Ghi Nhận Hàng Nhập Kho Quầy (Store Inward Goods Receiving)
Nguồn: stitch_ai_business_copilot_platform/se_03_ghi_nh_n_h_ng_nh_p_kho_qu_y_store_inward_goods_receiving_inventory_intake/code.html

## Field đang hiển thị
- Mã chứng từ nhập GRN: #GRN-20241024-003
- Nguồn điều chuyển / Phiếu xuất: Kho Tổng Tân Bình (Transfer In) - Phiếu #TO-89
- Nhân viên nhận & kiểm đếm: Nguyễn Thị Mai (#02)
- Quản lý duyệt: Trần Thu Hà (Store Manager)
- Tổng danh mục SKU: 04 mặt hàng (4/4 SKU khớp tem, tiến độ 100%)
- Tổng số lượng thực nhận: 150 / 150 sản phẩm (Khớp 100% phiếu xuất, Lệch: 0)
- Giá trị điều chuyển lô: 52.650.000 ₫ (Giá vốn nội bộ kho)
- Kiểm soát FEFO & Date: 100% ĐẠT CHUẨN (HSD trung bình > 34 tháng, Seal nguyên tem)
- Ô quét Barcode/QR/SKU [F1]: Input tìm kiếm quét mã vạch sản phẩm/kiện
- Chế độ quét: Quét từng món (+1) / Nhập số kiện / + Tạo Lô Date mới
- Danh sách mặt hàng tiếp nhận:
  + Tên sản phẩm: Serum Bio-B5 Hydra Max 100ml, Kem Phục Hồi Ceramide Aura Care 50ml, Son Kem Nhung Lì Velvet #03 Đỏ Gạch, Nước Tẩy Trang Damask Rose 400ml
  + Mã SKU: MB-SER-B5-01, MB-CRM-02, MB-LIP-VL-03, MB-CLEAN-01
  + Vị trí kệ lưu: Kệ A1-02 & Tủ 01, Kệ B2-01, Kệ Mặt Tiền T1, Kệ C1-04
  + Số lượng chứng từ (CT): 50, 30, 40, 30
  + Số lượng thực nhập: 50, 30, 40, 30
  + Số lô (LOT/Batch): LOT-202410-B5, LOT-202410-CR, LOT-202410-VT, LOT-202410-MC
  + Hạn sử dụng (FEFO): 10/2027, 10/2027, 11/2027, 09/2027
  + Tồn trước nhập & Sau nhập: Tồn 35 -> 85 (+50), Tồn 18 -> 48 (+30), Tồn 42 -> 82 (+40), Tồn 24 -> 54 (+30)
- Thẩm định FEFO: Khuyến nghị xếp hàng date mới vào mặt sau kệ để ưu tiên xuất lô cũ
- Thông tin vận chuyển: Tài xế Nguyễn Văn Hùng, Biên bản bàn giao #BB-TN-882
- Xác nhận ký duyệt: Tài xế giao, Thu ngân nhận, Cửa hàng trưởng phê duyệt

## Action/Button
- Quét PO/TO: Quét barcode phiếu điều chuyển
- Lịch sử ca: Xem lịch sử nhập ca trước
- In biên bản [F7]: In biên bản giao nhận
- Quét barcode sản phẩm [F1]: Focus ô nhập barcode
- Tăng/Giảm thực nhập (+/-): Điều chỉnh số lượng nhận thực tế
- In Phiếu Nhập [F8]: In phiếu nhập kho
- Lưu Tạm Thời: Lưu tạm dữ liệu kiểm nhận
- XÁC NHẬN NHẬP KHO & CẬP NHẬT TỒN [F9]: Hoàn tất nhập kho và cộng tồn kho tức thì

## Ghi chú UX
- Giao diện nhập kho quầy chuyên dụng cho nhân viên cửa hàng (SE).
- Bảng đối soát số lượng chứng từ (trên phiếu chuyển kho) với số lượng thực nhận.
- Cập nhật số lô (`inventory_batches.batchNumber`) và hạn sử dụng (`inventory_batches.expiresAt`) mới tiếp nhận vào kho quầy.
- Tự động hiển thị tồn kho trước và sau khi nhập tăng.

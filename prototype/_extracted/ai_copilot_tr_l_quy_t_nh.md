# BO: AI Copilot Trợ Lý Ra Quyết Định Kinh Doanh
Nguồn: stitch_ai_business_copilot_platform/ai_copilot_tr_l_quy_t_nh/code.html

## Field đang hiển thị
- Tiêu đề màn hình: ABC Copilot — Trợ Lý Ra Quyết Định Kinh Doanh
- Cột bên trái: Lịch sử hội thoại & chủ đề (Conversations & Topics):
  + Doanh thu tuần 42 giảm 12% (Phân tích đứt hàng Serum B5)
  + Đề xuất nhập Serum B5 cuối năm (Mô phỏng nhu cầu tồn an toàn 45 ngày Tết)
  + Hiệu quả Marketing & Khuyến mãi (Đơn hàng & Tỷ lệ hoàn COD)
  + 12 sản phẩm tồn kho > 90 ngày (Cần xả hàng quay vòng vốn)
- Luồng tin nhắn chat với AI Copilot:
  + Câu hỏi người dùng: "Tại sao tuần này doanh thu của cửa hàng giảm 12% so với tuần trước? Nguyên nhân chính là gì và tôi nên làm gì ngay hôm nay để bù đắp doanh số?"
  + Thẻ tóm lược điều hành: So sánh nhịp doanh thu 7 ngày (Tuần 41: 142.5M vs Tuần 42: 125.4M, đứt hàng Serum B5 từ Thứ 3).
  + Bằng chứng số liệu thực tế:
    * SKU đứt hàng: `MB-SER-B5-01` (Doanh thu tuần này 6.4M giảm 65% so với 18.5M tuần trước, tồn quầy: 0 chai).
    * Sản phẩm bán chậm: Tốc độ bán giảm 18%, tỷ lệ mua thành công giảm từ 32% xuống 21%.
    * Chi phí marketing kém hiệu quả: 9.200.000 ₫ trỏ link vào sản phẩm hết hàng.
  + Phân tích nguyên nhân cốt lõi (Root Cause):
    * Mất hiệu ứng bán chéo (Cross-sell): Giá trị đơn hàng trung bình giảm 35%.
    * Lãng phí chi phí marketing.
  + Kế hoạch hành động đề xuất 1-click:
    * Tạo đơn nhập hàng khẩn cấp PO: 80 chai Serum B5 (NCC Minh Anh, chiết khấu 28%, tổng: 21.600.000 ₫).
    * Tạm ngắt chiến dịch quảng cáo sản phẩm hết hàng để tiết kiệm 1.200.000 ₫/ngày.
    * Mở mô phỏng What-If kích cầu sản phẩm tồn kho lâu ngày.
- Prompt chips gợi ý thông minh:
  + "Dự báo doanh số tuần tới nếu nhập đủ 80 chai Serum B5?"
  + "So sánh giá nhập của 2 nhà cung cấp Serum B5 hiện có"
  + "Đề xuất danh sách khách hàng thân thiết để gửi ưu đãi"

## Action/Button
- Cuộc trò chuyện mới
- Xuất báo cáo PDF
- Gửi Kênh Quản Lý
- Tạo PO Đặt Hàng Ngay (Dẫn tới màn hình PO/Nhập kho)
- Mở Mô Phỏng What-If (Dẫn tới `bo-ai-mo-phong.html`)
- Sao chép tóm tắt / Lưu vào Sổ tay Giám đốc
- Gửi tin nhắn chat / Chọn prompt mẫu

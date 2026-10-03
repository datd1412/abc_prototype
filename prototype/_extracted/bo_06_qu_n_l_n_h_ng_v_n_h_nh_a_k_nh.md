# Extracted Content - BO-06: Quản lý Đơn hàng & Vận hành Đa kênh

**Nguồn:** `stitch_ai_business_copilot_platform/bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh/code.html`  
**Portal:** Business Owner (`bo-`)  
**Slug:** `bo-don-hang`  

---

## 1. Tiêu đề & Action Bar Top
- **Breadcrumb:** Chủ doanh nghiệp (BO) / BO-06: Quản lý Đơn hàng & POS
- **Badge trạng thái:** Auto-Sync Omnichannel Active (Shopee • TikTok Shop • POS Showroom Q.1)
- **Tiêu đề chính:** Quản lý Đơn Hàng & Vận Hành Đa Kênh
- **Mô tả:** Theo dõi toàn trình vòng đời đơn hàng, tự động khóa giữ chỗ (hold stock) và đồng bộ trừ kho tức thì, xử lý hủy/hoàn đơn minh bạch và đối soát các dòng tiền thanh toán số.
- **Nút hành động (Action Buttons):**
  1. `Đồng bộ Sàn TMĐT` (Icon `sync`)
  2. `Xuất Excel` (Icon `download`)
  3. `In Phiếu Đóng Gói Loạt` (Icon `print`)
  4. `+ Tạo Đơn Hàng Mới` (Primary Button)

---

## 2. Real-time Order Pulse KPI Cards (4 Thẻ chỉ số)
1. **Tổng Đơn Hàng (Tháng 10):** `4.280 đơn` (+18.4%) • TikTok Shop 43.2%, Showroom Q.1 33.2%, Shopee Mall 23.6%
2. **Doanh Thu Đơn Hàng Thực Nhận:** `1.845.200.000 ₫` • AOV: 431.120 ₫ • Tỷ lệ hoàn COD: 1.8%
3. **Chờ Đóng Gói & Xuất Kho:** `34 đơn` (Cần xử lý trước 14:00) • TikTok 22 đơn, Shopee 12 đơn
4. **Hủy & Đổi Trả Đã Hoàn Kho:** `18 đơn` (0.42%) • 100% SKU đã đối soát QC và tự động cộng hoàn kho

---

## 3. Bộ lọc & Tab vòng đời đơn hàng (Order Lifecycle Tabs & Filters)
- **Tabs:** `Tất cả đơn hàng (4.280)`, `Chờ xác nhận (12)`, `Chờ đóng gói & xuất kho (34)`, `Đang giao hàng (156)`, `Hoàn thành (4.060)`, `Đã hủy / Hoàn tiền (18)`
- **Search bar:** "Tìm theo mã đơn (ORD-...), tên khách, SĐT, SKU..."
- **Filter Kênh bán:** All, POS Showroom Q.1, TikTok Shop Mall, Shopee Official Store, Bán sỉ đại lý
- **Filter Thanh toán:** All, VietQR Động (MBBank), Tiền mặt tại quầy, Ví ShopeePay/Ví Sàn, Chuyển khoản B2B
- **Filter Tồn kho:** All, Đã trừ kho tự động, Đã giữ chỗ (Reserved), Đã hoàn trả lại kho
- **Filter Khoảng ngày:** Tháng 10/2024

---

## 4. Bảng Quản Lý Đơn Hàng Chi Tiết (Master Order Data Table)
### Các cột hiển thị (6 Primary Columns):
1. `Mã Đơn & Kênh` (Mã ORD-..., Badge kênh bán TikTok/POS/Shopee, Thời gian)
2. `Khách Hàng & Vận Chuyển` (Tên KH, SĐT, Đơn vị vận chuyển J&T/GHTK, Địa chỉ)
3. `Sản Phẩm & Chi Tiết SKU` (Ảnh, Tên SP, SKU, Số lượng)
4. `Tổng Tiền & Thanh Toán` (Thành tiền, Phương thức thanh toán VietQR/Ví sàn, Phí sàn)
5. `Tác Động Tồn Kho` (Badge: Đã giữ chỗ / Đã trừ kho / Đã hoàn kho)
6. `Trạng Thái Đơn` (Badge: Chờ đóng gói / Hoàn thành / Đang giao / Đã hủy)
7. `Thao Tác` (Nút Đóng gói, In vận đơn, Xem chi tiết)

### Dữ liệu mẫu tiêu biểu:
- **ORD-2024-9982 (TikTok Shop):** Khách Trần Ngọc Ánh (Đống Đa, Hà Nội), J&T Express, 2x Serum Bio-B5 100ml, Tổng 1.300.000 ₫ (Ví TikTok Shop), Tồn kho: Đã giữ chỗ Kho Tân Bình (-2), Trạng thái `Chờ đóng gói`.
- **ORD-2024-9980 (Showroom Q.1):** Khách Lê Hoàng Nam (VIP Gold), 1x Kem Rosa + 1x Son Velvet Bloom, Tổng 1.010.000 ₫ (VietQR MBBank), Tồn kho: Đã trừ kho Kệ Q.1, Trạng thái `Hoàn thành`.
- **ORD-2024-9975 (Shopee Mall):** Khách Nguyễn Minh Thảo, GHTK, 1x Tinh chất Tràm Trà SOS, Tổng 420.000 ₫ (Ví ShopeePay), Tồn kho: Đã trừ kho Kho Tân Bình, Trạng thái `Đang giao hàng`.
- **ORD-2024-9968 (Bán sỉ đại lý):** Đại lý An Nhiên, Chành xe Phương Trang, Combo Sỉ 35x SP, Tổng 12.800.000 ₫ (Chuyển khoản B2B), Tồn kho: Đã trừ kho Kho Tân Bình, Trạng thái `Hoàn thành`.

---

## 5. Form Drawer Slide-over (Tạo Đơn Hàng / Chi Tiết Đơn Hàng)
- **Tạo Đơn Hàng Mới:**
  - Chọn Kênh bán (`orders.channel`)
  - Chọn Khách hàng (`orders.customerId`)
  - Thêm sản phẩm & số lượng (`order_items.variantId`, `order_items.quantity`)
  - Phương thức thanh toán (`orders.paymentMethod`)
  - Địa chỉ giao hàng (`orders.shippingAddress`)
- **Chi Tiết Đơn Hàng & Lịch Sử Vận Hành:**
  - Thông tin giữ chỗ kho (`inventory.reservedQty`)
  - Mã vận đơn (`orders.shippingCode`)
  - Lịch sử thay đổi trạng thái

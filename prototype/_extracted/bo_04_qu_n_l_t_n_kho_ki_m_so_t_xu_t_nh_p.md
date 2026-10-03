# Extracted Content - BO-04: Quản lý Tồn kho & Kiểm soát Xuất Nhập Tồn

**Nguồn:** `stitch_ai_business_copilot_platform/bo_04_qu_n_l_t_n_kho_ki_m_so_t_xu_t_nh_p/code.html`  
**Portal:** Business Owner (`bo-`)  
**Slug:** `bo-kho-ton-kho`  

---

## 1. Tiêu đề & Action Bar Top
- **Breadcrumb:** Chủ doanh nghiệp (BO) / BO-04: Quản lý Tồn kho
- **Badge trạng thái hệ thống:** Real-time Stock Sync & FEFO Active
- **Tiêu đề chính:** Quản lý Tồn kho & Kiểm soát Xuất Nhập Tồn
- **Mô tả:** Giám sát tồn kho thực tế, hạn dùng FEFO, ghi nhận nhập xuất kho, điều chỉnh chênh lệch kiểm kê và cảnh báo nguy cơ đứt hàng dựa trên AI velocity.
- **Nút hành động (Action Buttons):**
  1. `Lịch sử biến động` (Icon `history`)
  2. `+ Nhập kho` (Icon `add_box`, Primary Green)
  3. `- Xuất kho` (Icon `indeterminate_check_box`, Danger Red)
  4. `± Lệch kiểm kê` (Icon `tune`)
  5. `+ Tạo Phiếu Mới` (Primary Blue button)

---

## 2. KPI Summary Cards (4 Thẻ chỉ số)
1. **Tổng Giá Trị Tồn Kho (FIFO)**
   - Số liệu: `890.400.000 ₫`
   - Phụ đề: `142 SKU` • `3.840 sp tại 3 kho`
   - Tiến độ: `78%`
2. **SKU An Toàn / Bình Thường**
   - Số liệu: `128 / 142 SKU`
   - Phụ đề: `90.1% danh mục` • `Quay vòng TB 22 ngày`
   - Tiến độ: `90%`
3. **Nguy cơ Đứt Hàng (Stock-out)**
   - Số liệu: `6 SKU cấp bách`
   - Phụ đề: `4 SKU < Min Stock` • `2 SKU cạn 3-5 ngày`
   - Tiến độ: `35%` (Màu đỏ danger)
4. **Cận Hạn FEFO (<90 Ngày)**
   - Số liệu: `8 Lô Date`
   - Phụ đề: `Trị giá 64.200.000 ₫` • `Cần ưu tiên xả`
   - Tiến độ: `45%` (Màu warning)

---

## 3. AI Inventory Intelligence & Burn-Rate Banner (AI Insights)
- **Model:** Velocity-V4
- **Tiêu đề:** AI Inventory Intelligence & Dự Báo Tiêu Thụ Tự Động
- **Mô tả:** Phân tích tốc độ bán ra thực tế (Burn-rate 7 ngày), thời gian giao hàng nhà cung cấp (Lead-time) và ngày cạn hàng ước tính.
- **Dữ liệu 3 Card gợi ý AI:**
  1. **Serum Phục Hồi Bio-B5 Hydra Max (SKU-SKN-001)**
     - Trạng thái: `Nguy cấp: Hết trong 2.9 ngày`
     - Tồn thực tế: `18 hộp` | Min stock: `30 hộp` | Burn-rate: `6.2 /ngày`
     - Lý do: Tốc độ bán tăng vọt +85% do Livestream TikTok. Lead-time Cty DermaLab là 5 ngày. Đứt hàng từ 27/10 gây thiệt hại ~19.500.000 ₫.
     - Action: `Tạo PO Nhập 150 hộp`
  2. **Kem Dưỡng Tái Sinh Rosa Damascena (SKU-CRM-012)**
     - Trạng thái: `Cảnh báo: Cạn sau 3.8 ngày`
     - Tồn thực tế: `8 hộp` | Min stock: `25 hộp` | Burn-rate: `2.1 /ngày`
     - Lý do: Kho Tân Bình cạn nhanh, đơn Pháp trễ 2 ngày. Showroom Q.1 dư an toàn 28 hộp.
     - Action: `Chuyển 15 hộp từ Q.1`
  3. **Son Lụa Dưỡng Ẩm Velvet Bloom #04 (SKU-LIP-004)**
     - Trạng thái: `FEFO: 68 ngày đến hạn`
     - Tồn Lô #24B: `42 cây` | Hạn dùng: `31/12/24` | Burn-rate: `0.5 /ngày`
     - Khuyến nghị: Tốc độ bán chậm làm dư 22 cây hết hạn. Đề xuất Bundle "Mua Kem tặng Son -40%".
     - Action: `Áp dụng Bundle Xả Hàng`

---

## 4. Thanh tìm kiếm & Bộ lọc (Toolbar & Filters)
- **Search bar:** "Tìm kiếm theo Tên sản phẩm, Mã SKU, Barcode hoặc Số Lô (Lot #)..."
- **Filter 1 (Chi nhánh Kho):** `Kho: Tất cả chi nhánh`
- **Filter 2 (Trạng thái tồn):** `Trạng thái: Cảnh báo & Cận hạn (14)`
- **Filter 3 (Phân loại):** `Ngành: Skincare & Son`
- **Nút:** `Làm mới bộ lọc` (Refresh), `Xuất File` (Excel Download)

---

## 5. Bảng Dữ Liệu Tồn Kho Chi Tiết (Inventory Data Table)
### Các cột hiển thị trên Stitch gốc:
1. `Sản phẩm & SKU` (Hình ảnh, Tên sản phẩm, SKU, Quy cách, Barcode)
2. `Vị trí kho & Lô Date (FEFO)` (Kho, Kệ, Lot #, Exp Date)
3. `Tồn thực tế` (Số lượng + Đơn vị)
4. `Tồn tối thiểu` (Min Stock)
5. `AI Burn-rate` (Tốc độ tiêu thụ/ngày)
6. `Dự báo cạn (Runway)` (Số ngày còn lại)
7. `Giá trị tồn (FIFO)` (Tổng giá trị + Đơn giá vốn)
8. `Trạng thái` (Badge: Nguy cơ đứt hàng, Dưới Min stock, An toàn, Cận hạn FEFO)
9. `Thao tác` (Nút +Nhập, -Xuất, Điều chỉnh, Lịch sử)

### Dữ liệu mẫu tiêu biểu:
- **Bio-B5 Hydra Max (SKU-SKN-001):** Kho Tân Bình (Kệ A2-04), Lot #24D, Exp 11/2026, Tồn 18 hộp, Min 30, Burn-rate 6.2/ngày, Runway 2.9 ngày, Giá trị 5.040.000 ₫ (Đơn giá vốn 280k), Badge `Nguy cơ đứt hàng`.
- **Rosa Damascena Cream (SKU-CRM-012):** Showroom Q.1 (Tủ VIP), Lot #24C, Exp 08/2026, Tồn 8 hộp, Min 25, Burn-rate 2.1/ngày, Runway 3.8 ngày, Giá trị 5.200.000 ₫ (Đơn giá vốn 650k), Badge `Dưới Min Stock`.
- **Velvet Bloom Lipstick #04 (SKU-LIP-004):** Kho Tân Bình (Kệ B1-02), Lot #24B, Exp 31/12/2024, Tồn 42 cây, Min 15, Burn-rate 0.5/ngày, Runway 84 ngày, Giá trị 6.300.000 ₫ (Đơn giá vốn 150k), Badge `Cận hạn FEFO`.

---

## 6. Slide-over / Form Drawer (Phiếu Nhập/Xuất & Điều chỉnh Kho)
- **Tạo Phiếu Nhập Kho:**
  - Chọn Kho nhận (`inventory.warehouseId`)
  - Sản phẩm (`product_variants.id`)
  - Số lượng nhập (`inventory_transactions.quantity`)
  - Lô sản xuất (`inventory_batches.batchNumber`)
  - Ngày hết hạn (`inventory_batches.expiresAt`)
  - Đơn giá nhập / Giá vốn (`inventory_batches.costPrice`)
- **Tạo Phiếu Xuất Kho:**
  - Chọn Kho xuất (`inventory.warehouseId`)
  - Chọn Sản phẩm & Lô date xuất theo FEFO
  - Lý do xuất (Bán hàng / Chuyển kho / Hủy hàng hư hỏng)
- **Điều chỉnh Tồn Kho (Kiểm kê):**
  - Tồn sổ sách vs Tồn thực tế
  - Lý do chênh lệch

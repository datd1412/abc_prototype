# Rule: Linking (Nối các màn hình thật với nhau)

## 3 portal riêng biệt — KHÔNG dùng chung 1 nav

Theo FR có 3 role tách biệt (Business Owner, Store Employee, System Administrator),
mỗi role có tập màn hình và quyền truy cập khác nhau (đặc biệt FR 2.4 cấm Store
Employee xem tài chính/AI/quản lý). Vì vậy có 3 file nav riêng, KHÔNG gộp chung:

| Portal | File nav dùng chung | Prefix slug/filename |
|---|---|---|
| Business Owner | `_shared/nav-owner.js` | `bo-` |
| Store Employee | `_shared/nav-employee.js` | `se-` |
| System Admin | `_shared/nav-admin.js` | `sa-` |

Mỗi file màn hình chỉ include ĐÚNG 1 trong 3 file nav ở trên, tùy nó thuộc portal
nào — không được include nhầm, không được để 1 màn thấy menu của portal khác.

## Boilerplate BẮT BUỘC (thay `<ten-nav>` bằng nav-owner/nav-employee/nav-admin)

```html
<body data-screen="<slug-cua-man-nay>">
  <div class="app-container">
    <header id="app-topnav"></header>
    <main class="page-body"> ... </main>
  </div>
  <script src="../_shared/<ten-nav>.js"></script>
</body>
```

## Bảng slug — Business Owner (prefix bo-)

| Slug | Màn hình |
|---|---|
| bo-tong-quan | Dashboard tổng quan |
| bo-san-pham-danh-sach | Danh sách sản phẩm |
| bo-san-pham-danh-muc | Danh mục sản phẩm |
| bo-nha-cung-cap | Nhà cung cấp |
| bo-kho-ton-kho | Tồn kho |
| bo-kho-lo-hang | Lô hàng & hạn dùng |
| bo-kho-dieu-chinh | Điều chỉnh tồn kho |
| bo-don-hang | Đơn hàng |
| bo-khach-hang | Khách hàng |
| bo-thanh-toan | Thanh toán |
| bo-chi-phi | Chi phí |
| bo-dong-tien | Dòng tiền |
| bo-ai-copilot | AI Copilot |
| bo-ai-phan-tich | AI Phân tích kinh doanh |
| bo-ai-canh-bao | AI Cảnh báo bất thường |
| bo-ai-du-bao | AI Dự báo nhu cầu |
| bo-ai-ton-kho-thong-minh | AI Inventory Intelligence |
| bo-ai-mo-phong | AI Mô phỏng What-if |
| bo-quan-ly-nhan-vien | Nhân viên & phân quyền (chỉ nhân viên của mình) |

## Bảng slug — Store Employee (prefix se-), theo FR 2.1–2.3

| Slug | Màn hình |
|---|---|
| se-ban-hang | Ghi nhận giao dịch bán (Sales Transaction) |
| se-kiem-ke-ton-kho | Kiểm kê / điều chỉnh tồn kho thực tế |
| se-nhap-kho | Ghi nhận hàng nhập kho |
| se-tra-cuu-san-pham | Tra cứu thông tin sản phẩm (chỉ xem) |

## Bảng slug — System Admin (prefix sa-), theo FR mục 3

| Slug | Màn hình |
|---|---|
| sa-tai-khoan-vai-tro | Quản lý tài khoản & vai trò (3.1) |
| sa-quan-ly-doanh-nghiep | Danh sách & trạng thái doanh nghiệp đăng ký (3.2) |
| sa-cau-hinh-he-thong | Cấu hình hệ thống dùng chung (3.3) |
| sa-audit-log | Audit Log (3.4) |

**Đối chiếu lại với 25 folder Stitch gốc** (`bo_01`→`bo_11`, `se_01`→`se_04`,
`sa_01`→`sa_04`) trước khi build — nếu số lượng/tên slug ở trên chưa khớp đủ với
folder thật bạn có, báo lại để chỉnh bảng, đừng để agent tự đoán thêm/bớt slug.

## Checklist bổ sung (build-screen.md)

- [ ] File đặt đúng tên slug + đúng prefix portal (bo-/se-/sa-)
- [ ] `data-screen` khớp slug
- [ ] Include ĐÚNG 1 file nav tương ứng portal, không lẫn portal khác
- [ ] Không có markup nav viết tay

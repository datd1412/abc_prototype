# ABC Prototype — AI Business Copilot Platform

> **Hệ thống Quản trị Bán lẻ & Trợ lý Ra quyết định Thông minh (Omnichannel Retail Copilot)** dành cho chuỗi thời trang, mỹ phẩm và bán hàng đa kênh (Showroom POS, Shopee Mall, TikTok Shop, B2B Đại lý).

---

## 📌 Giới thiệu dự án

**ABC Prototype** là bản nguyên mẫu giao diện hoàn chỉnh (Desktop Admin Panel & POS Web-based) mô phỏng toàn bộ luồng vận hành kinh doanh thực tế:
- **Quản lý Bán lẻ & POS Quầy**: Quét mã vạch, thanh toán động VietQR Napas 247, xử lý ca bán và giao dịch đổi trả.
- **Quản trị Tồn kho & Lô Date (FEFO)**: Quản lý đợt nhập PO, tách đa lô hạn dùng, cảnh báo cận date (< 60 ngày) và in tem mã vạch nội bộ.
- **Tài chính & Dòng tiền Thực tế**: Sổ thu chi ngân hàng/két quầy, đối soát ví sàn TMĐT Shopee/TikTok COD, phân tích chênh lệch giữa lợi nhuận dồn tích (*Accrual P&L*) và dòng tiền ròng (*Cashflow*).
- **AI Business Copilot**: Phân tích dự báo cầu (ROP), phát hiện bất thường thời gian thực, mô phỏng kịch bản What-If kinh doanh & thanh khoản, hỗ trợ đàm phán chiết khấu nhà cung cấp.

---

## 🗂 Cấu trúc thư mục

```text
abc-prototype/
├── prototype/
│   ├── screens/                  # Toàn bộ 45 màn hình HTML hoàn chỉnh
│   │   ├── bo-*.html             # Màn hình Business Owner (Tổng quan, Đơn hàng, Kho, Tài chính...)
│   │   ├── se-*.html             # Màn hình Nhân viên / Store Employee (POS, Nhập kho, Giao ca...)
│   │   ├── sa-*.html             # Màn hình Quản trị hệ thống / System Administrator
│   │   └── bo-modal-*.html       # Các modal nghiệp vụ (VietQR B2B, PO preview, Tách lô...)
│   ├── _shared/                  # Thành phần dùng chung
│   │   ├── nav-owner.js          # Thanh điều hướng cho Business Owner
│   │   ├── nav-employee.js       # Thanh điều hướng cho Nhân viên cửa hàng
│   │   └── nav-admin.js          # Thanh điều hướng cho System Admin
│   ├── _notes/                   # Tài liệu đối chiếu & kiểm kê
│   │   ├── screen-inventory.md   # Danh mục kiểm kê 45/45 màn hình đã build
│   │   └── removed-fields.md     # Danh sách các trường loại bỏ vì không thuộc ERD
│   ├── _extracted/               # Nội dung nghiệp vụ trích xuất và ánh xạ ERD
│   └── tokens.css                # Nguồn sự thật duy nhất cho Design Tokens (màu sắc, spacing, font)
├── erd/                          # Thực thể & trường dữ liệu trọng tài
│   └── SEP490_entities_fields.txt
├── fr/                           # Tài liệu yêu cầu chức năng (Functional Requirements)
├── AGENTS.md                     # Quy tắc kiến trúc & tiêu chuẩn dự án
└── README.md                     # Hướng dẫn sử dụng & triển khai
```

---

## 🚀 Hướng dẫn cách chạy & sử dụng

Mọi màn hình đều được xây dựng bằng **Vanilla HTML, CSS và JavaScript thuần**, không phụ thuộc build tool phức tạp, có thể mở xem trực tiếp hoặc khởi chạy web server cục bộ.

### Cách 1: Khởi chạy nhanh bằng Python (Khuyên dùng)
Nếu máy bạn đã có sẵn Python:
```bash
# Di chuyển vào thư mục dự án
cd d:/prototype/abc-prototype

# Khởi chạy server local tại cổng 8000
python -m http.server 8000
```
Sau đó mở trình duyệt và truy cập:
- Màn hình chính Business Owner: `http://localhost:8000/prototype/screens/bo-tong-quan.html`
- Quầy bán hàng POS: `http://localhost:8000/prototype/screens/se-ban-hang.html`
- Quản trị viên hệ thống: `http://localhost:8000/prototype/screens/sa-master-console.html`

### Cách 2: Khởi chạy bằng Node.js / npx serve
```bash
cd d:/prototype/abc-prototype
npx serve .
```

### Cách 3: Dùng extension "Live Server" trong VS Code / Antigravity IDE
1. Cài extension **Live Server** trong VS Code.
2. Click chuột phải vào file `prototype/screens/bo-tong-quan.html` và chọn **"Open with Live Server"**.

### Cách 4: Mở trực tiếp trên trình duyệt
Double-click trực tiếp vào bất kỳ file `.html` nào trong thư mục `prototype/screens/` để xem ngay lập tức trên Chrome, Edge, Brave hoặc Firefox.

---

## 🧭 Danh mục màn hình chính & Luồng trải nghiệm

### 1. Phân hệ Chủ Doanh Nghiệp (Business Owner - `bo-`)
- **Tổng quan & Điều hành**:
  - `bo-tong-quan.html`: Dashboard doanh nghiệp tổng hợp.
  - `bo-tong-quan-cua-hang.html`: Vận hành chi tiết điểm bán.
  - `bo-ai-retail-pulse.html`: Bảng điều hành nhịp đập bán lẻ & vận tốc SKU.
- **Sản phẩm & Tồn kho**:
  - `bo-san-pham-danh-sach.html`: Danh sách sản phẩm & giá niêm yết.
  - `bo-san-pham-bien-the-kho.html`: Quản lý biến thể & hạn dùng lô date FEFO.
  - `bo-kho-ton-kho.html`: Quản trị tồn kho, an toàn vốn & đề xuất nhập hàng.
  - `bo-nha-cung-cap-cong-no.html`: Quản lý NCC, hạn mức công nợ & chiết khấu.
- **Đơn hàng & Bán hàng**:
  - `bo-don-hang.html`: Danh sách đơn hàng bán lẻ & thương mại điện tử.
  - `bo-don-hang-pos-da-kenh.html`: Hub quản lý đơn hàng đa kênh (POS, Shopee, TikTok, B2B).
- **Tài chính & Dòng tiền**:
  - `bo-chi-phi.html`: Chi phí quản trị và hạch toán vận hành.
  - `bo-chi-phi-so-thu-chi.html`: Sổ thu chi ngân hàng/két & dòng tiền thực tế.
  - `bo-dong-tien-detail.html`: Báo cáo đối chiếu Accrual P&L vs Cashflow.
  - `bo-thanh-toan-doi-soat-san.html`: Đối soát ví sàn Shopee, TikTok COD.
- **Trợ lý AI & Dự báo**:
  - `bo-ai-copilot-tro-ly.html`: Trợ lý AI đàm thoại & hỗ trợ ra quyết định.
  - `bo-ai-phan-tich.html`: Phân tích sâu hiệu quả kinh doanh.
  - `bo-ai-canh-bao-realtime.html`: Radar phát hiện bất thường thời gian thực.
  - `bo-ai-du-bao-goi-y-nhap.html`: Dự báo nhu cầu cầu hàng & gợi ý ROP.
  - `bo-ai-mo-phong-whatif.html`: Mô phỏng kịch bản kinh doanh What-If.
  - `bo-ai-mo-phong-dong-tien.html`: Mô phỏng áp lực dòng tiền & thanh khoản 30 ngày.

### 2. Phân hệ Nhân Viên Điểm Bán & Kho (Staff / Employee - `se-`)
- `se-ban-hang.html`: Giao diện thu ngân POS tại quầy, quét mã & VietQR.
- `se-tra-cuu-san-pham.html`: Tra cứu thông tin sản phẩm, tồn kho và vị trí kệ.
- `se-nhap-kho.html`: Quy trình tiếp nhận PO, kiểm đếm hàng & khởi tạo lô date.
- `se-kiem-ke-ton-kho.html`: Kiểm kê định kỳ, ghi nhận lệch tồn và quét barcode.
- `se-doi-tra-hang.html`: Xử lý đổi/trả sản phẩm lỗi, hoàn tiền hoặc đổi voucher.
- `se-giao-ca.html`: Kết ca, kiểm đếm két tiền mặt và đối soát doanh thu ca.

### 3. Phân hệ Quản Trị Hệ Thống (System Admin - `sa-`)
- `sa-master-console.html`: Bảng điều khiển toàn năng Master Console SA.
- `sa-quan-ly-doanh-nghiep.html`: Quản lý danh sách tenant/doanh nghiệp trên platform.
- `sa-an-ninh-he-thong.html`: Giám sát an ninh, phiên đăng nhập & phân quyền.
- `sa-cau-hinh-he-thong.html`: Cấu hình tham số hệ thống & tích hợp API.
- `sa-audit-log.html`: Nhật ký kiểm toán thao tác người dùng.

### 4. Các Modal Nghiệp vụ Nổi bật
- `bo-modal-thanh-toan-cong-no-vietqr.html`: Thanh toán gộp công nợ B2B hàng loạt qua VietQR.
- `bo-modal-phieu-chi-vietqr.html`: Lập phiếu chi và xuất lệnh VietQR động.
- `bo-modal-phieu-thu-ban-si.html`: Lập phiếu thu tiền sỉ & đại lý.
- `bo-modal-nhap-kho-po-3.html`: Phiếu nhập kho đa lô tích hợp sinh mã vạch tem nhãn.
- `bo-modal-them-nhan-vien-rbac.html`: Thêm nhân viên và gán phân quyền granular RBAC.

---

## 🎨 Tiêu chuẩn thiết kế & Quy tắc kỹ thuật

1. **Design Tokens thống nhất**: Mọi màn hình đều liên kết tới `prototype/tokens.css` dùng biến CSS chuẩn (`--color-primary`, `--color-surface`, `--color-text`, `--radius`,...).
2. **Icon Policy v2 (Zero Font, Zero Emoji)**: Không phụ thuộc internet vào Material Symbols hoặc Font Awesome CDN; 100% icon sử dụng inline stroke SVG nét mảnh chuyên nghiệp.
3. **Data Grounding với ERD**: 100% trường dữ liệu hiển thị đều được kiểm tra và ánh xạ từ cơ sở dữ liệu `erd/SEP490_entities_fields.txt`.
4. **Desktop First**: Thiết kế chuẩn desktop admin panel tối ưu cho màn hình laptop & máy tính thu ngân/kế toán.

---

## 👨‍💻 Tác giả & Giấy phép
Dự án được phát triển theo tiêu chuẩn SEP490 cho nền tảng quản trị bán lẻ thời trang & mỹ phẩm đa kênh tích hợp AI Copilot.

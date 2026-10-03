# Danh Sách Field & Chức Năng Đã Loại Bỏ

| Field / Tính năng | Màn hình | Lý do loại |
|---|---|---|
| Barcode (`8936014298110`) | BO-03 Quản lý Sản phẩm & Bảng giá | Không có field barcode trong ERD `SEP490_entities_fields.txt` (chỉ quản lý duy nhất bằng `product_variants.sku`) |
| Giá sỉ (≥10) (`520.000 ₫`) | BO-03 Quản lý Sản phẩm & Bảng giá | Không có cấu trúc giá sỉ / giá bán đa cấp trong ERD (chỉ có `sellingPrice`) |
| Chi nhánh cửa hàng (`Chi nhánh Q.1`) | BO-03 Quản lý Sản phẩm & Bảng giá | Không có entity/field chi nhánh cửa hàng trong ERD (chỉ có `businessId`) |
| Hardware Status Máy quét Barcode Honeywell | SE-02 Kiểm Kê Tồn Kho Quầy | Trạng thái thiết bị phần cứng không thuộc entity/field nào trong ERD |
| Camera quét Barcode/QR | SE-02 Kiểm Kê Tồn Kho Quầy | Tính năng camera phần cứng không có entity lưu trữ trong ERD |
| Chi nhánh làm việc (`Showroom Quận 1`) | Modal Thêm Nhân Viên Mới RBAC | Không có entity/field chi nhánh trong ERD SEP490 (chỉ có businesses và warehouses) |

